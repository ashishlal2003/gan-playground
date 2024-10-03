import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.utils import save_image
import os
from models.cycleGan import CycleGAN_Generator, CycleGAN_Discriminator  # Import CycleGAN models

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Hyperparameters
ngf = 64  # Size of feature maps in generator
ndf = 64  # Size of feature maps in discriminator
nc = 3    # Number of color channels in images (typically 3 for RGB)

# Load dataset
transform = transforms.Compose([
    transforms.Resize(128),
    transforms.CenterCrop(128),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])

output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

# Initialize loss functions
criterion_GAN = nn.MSELoss()  # For adversarial loss
criterion_cycle = nn.L1Loss()  # For cycle consistency loss
criterion_identity = nn.L1Loss()  # For identity loss

# Initialize CycleGAN model components
def initialize_cyclegan(dataroot_A, dataroot_B, num_epochs, lr, lambda_cycle, lambda_identity):
    dataset_A = datasets.ImageFolder(root=dataroot_A, transform=transform)
    dataset_B = datasets.ImageFolder(root=dataroot_B, transform=transform)

    dataloader_A = DataLoader(dataset_A, batch_size=1, shuffle=True, num_workers=4)
    dataloader_B = DataLoader(dataset_B, batch_size=1, shuffle=True, num_workers=4)

    netG_A2B = CycleGAN_Generator(in_channels=nc, out_channels=nc).to(device)
    netG_B2A = CycleGAN_Generator(in_channels=nc, out_channels=nc).to(device)
    netD_A = CycleGAN_Discriminator(in_channels=nc).to(device)
    netD_B = CycleGAN_Discriminator(in_channels=nc).to(device)

    optimizer_G = optim.Adam(
        list(netG_A2B.parameters()) + list(netG_B2A.parameters()), lr=lr, betas=(0.5, 0.999)
    )
    optimizer_D_A = optim.Adam(netD_A.parameters(), lr=lr, betas=(0.5, 0.999))
    optimizer_D_B = optim.Adam(netD_B.parameters(), lr=lr, betas=(0.5, 0.999))

    return netG_A2B, netG_B2A, netD_A, netD_B, optimizer_G, optimizer_D_A, optimizer_D_B, dataloader_A, dataloader_B


# Training function
def train_cyclegan(dataroot_A, dataroot_B, num_epochs, lr, lambda_cycle=10.0, lambda_identity=0.5):
    netG_A2B, netG_B2A, netD_A, netD_B, optimizer_G, optimizer_D_A, optimizer_D_B, dataloader_A, dataloader_B = initialize_cyclegan(dataroot_A, dataroot_B, num_epochs, lr, lambda_cycle, lambda_identity)
    
    for epoch in range(num_epochs):
        for i, ((real_A, _), (real_B, _)) in enumerate(zip(dataloader_A, dataloader_B)):
            real_A = real_A.to(device)
            real_B = real_B.to(device)
            batch_size = real_A.size(0)

            # Real and fake labels
            real_label = torch.ones((batch_size, 1, 16, 16), device=device)
            fake_label = torch.zeros((batch_size, 1, 16, 16), device=device)

            # (1) Update Generators A2B and B2A
            optimizer_G.zero_grad()

            # Identity loss
            identity_A = netG_B2A(real_A)
            loss_identity_A = criterion_identity(identity_A, real_A) * lambda_identity
            identity_B = netG_A2B(real_B)
            loss_identity_B = criterion_identity(identity_B, real_B) * lambda_identity

            # GAN loss
            fake_B = netG_A2B(real_A)
            pred_fake_B = netD_B(fake_B)
            loss_GAN_A2B = criterion_GAN(pred_fake_B, real_label)

            fake_A = netG_B2A(real_B)
            pred_fake_A = netD_A(fake_A)
            loss_GAN_B2A = criterion_GAN(pred_fake_A, real_label)

            # Cycle consistency loss
            recovered_A = netG_B2A(fake_B)
            loss_cycle_A = criterion_cycle(recovered_A, real_A) * lambda_cycle

            recovered_B = netG_A2B(fake_A)
            loss_cycle_B = criterion_cycle(recovered_B, real_B) * lambda_cycle

            # Total generator loss
            loss_G = (
                loss_identity_A + loss_identity_B
                + loss_GAN_A2B + loss_GAN_B2A
                + loss_cycle_A + loss_cycle_B
            )
            loss_G.backward()
            optimizer_G.step()

            # (2) Update Discriminator A
            optimizer_D_A.zero_grad()

            pred_real_A = netD_A(real_A)
            loss_D_real_A = criterion_GAN(pred_real_A, real_label)

            pred_fake_A = netD_A(fake_A.detach())
            loss_D_fake_A = criterion_GAN(pred_fake_A, fake_label)

            loss_D_A = (loss_D_real_A + loss_D_fake_A) * 0.5
            loss_D_A.backward()
            optimizer_D_A.step()

            # (3) Update Discriminator B
            optimizer_D_B.zero_grad()

            pred_real_B = netD_B(real_B)
            loss_D_real_B = criterion_GAN(pred_real_B, real_label)

            pred_fake_B = netD_B(fake_B.detach())
            loss_D_fake_B = criterion_GAN(pred_fake_B, fake_label)

            loss_D_B = (loss_D_real_B + loss_D_fake_B) * 0.5
            loss_D_B.backward()
            optimizer_D_B.step()

            if i % 100 == 0:
                print(f'Epoch [{epoch}/{num_epochs}], Step [{i}/{len(dataloader_A)}], Loss_G: {loss_G.item():.4f}, Loss_D_A: {loss_D_A.item():.4f}, Loss_D_B: {loss_D_B.item():.4f}')
                
                # Save a few sample images
                save_image(fake_A, os.path.join(output_dir, f'fake_A_{epoch}_{i}.png'), normalize=True)
                save_image(fake_B, os.path.join(output_dir, f'fake_B_{epoch}_{i}.png'), normalize=True)

        # Save model checkpoints at the end of each epoch
        torch.save(netG_A2B.state_dict(), os.path.join(output_dir, 'netG_A2B.pth'))
        torch.save(netG_B2A.state_dict(), os.path.join(output_dir, 'netG_B2A.pth'))
        torch.save(netD_A.state_dict(), os.path.join(output_dir, 'netD_A.pth'))
        torch.save(netD_B.state_dict(), os.path.join(output_dir, 'netD_B.pth'))


# Generate images using trained CycleGAN
def generate_cyclegan_images(image, model_A2B_path, model_B2A_path):
    netG_A2B = CycleGAN_Generator(in_channels=nc, out_channels=nc).to(device)
    netG_B2A = CycleGAN_Generator(in_channels=nc, out_channels=nc).to(device)
    
    netG_A2B.load_state_dict(torch.load(model_A2B_path))
    netG_B2A.load_state_dict(torch.load(model_B2A_path))
    netG_A2B.eval()
    netG_B2A.eval()

    image = image.to(device).unsqueeze(0)

    with torch.no_grad():
        fake_B = netG_A2B(image)
        fake_A = netG_B2A(fake_B)

    return fake_B, fake_A
