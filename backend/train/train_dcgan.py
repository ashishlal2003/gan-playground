import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.utils import save_image
import os
from dotenv import load_dotenv

load_dotenv()

from models.dcgan import Generator, Discriminator

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Hyperparameters
nz = 100  # Size of z latent vector (i.e. size of generator input)
ngf = 64  # Size of feature maps in generator
ndf = 64  # Size of feature maps in discriminator
nc = int(os.getenv("nc"))    # Number of color channels in the training images. For color images this is 3

# Initialize the model
netG = Generator(nz, ngf, nc).to(device)
netD = Discriminator(nc, ndf).to(device)

# Initialize BCELoss function
criterion = nn.BCELoss()

# Create batch of latent vectors that we will use to visualize the progression of the generator
fixed_noise = torch.randn(64, nz, 1, 1, device=device)

# Setup Adam optimizers for both G and D
optimizerD = optim.Adam(netD.parameters(), lr=0.0002, betas=(0.5, 0.999))
optimizerG = optim.Adam(netG.parameters(), lr=0.0002, betas=(0.5, 0.999))

# Load the dataset
transform = transforms.Compose([
    transforms.Resize(64),
    transforms.CenterCrop(64),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])


output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)


# Modify the train_dcgan function to accept dataroot as a parameter
def train_dcgan(dataroot, num_epochs):
    dataset = datasets.ImageFolder(root=dataroot, transform=transform)
    dataloader = DataLoader(dataset, batch_size=128, shuffle=True, num_workers=4)

    for epoch in range(num_epochs):
        for i, data in enumerate(dataloader, 0):
            # (1) Update D network: maximize log(D(x)) + log(1 - D(G(z)))
            ## Train with all-real batch
            netD.zero_grad()
            real_cpu = data[0].to(device)
            b_size = real_cpu.size(0)
            label = torch.full((b_size,), 1, dtype=torch.float, device=device)  # Convert label to float
            output = netD(real_cpu).view(-1)
            errD_real = criterion(output, label)
            errD_real.backward()
            D_x = output.mean().item()

            ## Train with all-fake batch
            noise = torch.randn(b_size, nz, 1, 1, device=device)
            fake = netG(noise)
            label.fill_(0)  # No need to convert again as it's already float
            output = netD(fake.detach()).view(-1)
            errD_fake = criterion(output, label)
            errD_fake.backward()
            D_G_z1 = output.mean().item()
            errD = errD_real + errD_fake
            optimizerD.step()

            # (2) Update G network: maximize log(D(G(z)))
            netG.zero_grad()
            label.fill_(1)
            output = netD(fake).view(-1)
            errG = criterion(output, label)
            errG.backward()
            D_G_z2 = output.mean().item()
            optimizerG.step()

            if i % 50 == 0:
                print(f'[{epoch}/{num_epochs}][{i}/{len(dataloader)}] Loss_D: {errD.item():.4f} Loss_G: {errG.item():.4f} D(x): {D_x:.4f} D(G(z)): {D_G_z1:.4f} / {D_G_z2:.4f}')
        # Save fake images generated at each epoch
                try:
                    save_image(fake.data[:64], os.path.join(output_dir, f'fake_samples_step_{i:03d}.png'), normalize=True)
                except Exception as e:
                    print(f"Error saving image at i {i}: {e}")
        save_image(fake.data[:64], f'output/fake_samples_step_{i:03d}.png', normalize=True)

        # Save models
        torch.save(netG.state_dict(), 'output/netG.pth')
        torch.save(netD.state_dict(), 'output/netD.pth')


def generate_images(num_images, model_path='output/netG.pth'):
    netG = Generator(nz, ngf, nc).to(device)
    netG.load_state_dict(torch.load(model_path))
    netG.eval()
    
    noise = torch.randn(num_images, nz, 1, 1, device=device)
    with torch.no_grad():
        fake_images = netG(noise).detach().cpu()
    return fake_images
