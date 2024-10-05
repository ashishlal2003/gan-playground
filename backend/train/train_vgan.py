import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.utils import save_image
import os
from dotenv import load_dotenv

load_dotenv()

from models.vgan import VanillaGAN_Generator, VanillaGAN_Discriminator  # Import Vanilla GAN models

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Hyperparameters
input_size = 784  # For a 28x28 image (adjust based on your image size)
ngf = 256  # Size of feature maps in generator
ndf = 256  # Size of feature maps in discriminator

# Initialize BCELoss function
criterion = nn.BCELoss()
# Load the dataset
transform = transforms.Compose([
    transforms.Resize(64),
    transforms.CenterCrop(64),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])


output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

# Modify the train_vanilla_gan function to accept dataroot as a parameter
def train_vanilla_gan(dataroot, num_epochs, lr, nz):
    dataset = datasets.MNIST(root=dataroot, train=True, download=True,
                             transform=transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))]))
    dataloader = DataLoader(dataset, batch_size=128, shuffle=True, num_workers=4)

    netG = VanillaGAN_Generator(nz, ngf, input_size).to(device)
    netD = VanillaGAN_Discriminator(input_size, ndf).to(device)

    optimizerD = optim.Adam(netD.parameters(), lr=lr, betas=(0.5, 0.999))
    optimizerG = optim.Adam(netG.parameters(), lr=lr, betas=(0.5, 0.999))

    for epoch in range(num_epochs):
        for i, data in enumerate(dataloader, 0):
            images, _ = data
            images = images.view(images.size(0), -1).to(device)

            # (1) Update D network: maximize log(D(x)) + log(1 - D(G(z)))
            netD.zero_grad()
            b_size = images.size(0)
            label_real = torch.full((b_size,), 1, dtype=torch.float, device=device)
            output = netD(images).view(-1)
            errD_real = criterion(output, label_real)
            errD_real.backward()
            D_x = output.mean().item()

            noise = torch.randn(b_size, nz, device=device)
            fake_images = netG(noise)
            label_fake = torch.full((b_size,), 0, dtype=torch.float, device=device)
            output = netD(fake_images.detach()).view(-1)
            errD_fake = criterion(output, label_fake)
            errD_fake.backward()
            D_G_z1 = output.mean().item()
            errD = errD_real + errD_fake
            optimizerD.step()

            # (2) Update G network: maximize log(D(G(z)))
            netG.zero_grad()
            label_real.fill_(1)  # Flip labels for generator loss
            output = netD(fake_images).view(-1)
            errG = criterion(output, label_real)
            errG.backward()
            D_G_z2 = output.mean().item()
            optimizerG.step()

            if i % 50 == 0:
                print(f'[{epoch}/{num_epochs}][{i}/{len(dataloader)}] Loss_D: {errD.item():.4f} Loss_G: {errG.item():.4f} D(x): {D_x:.4f} D(G(z)): {D_G_z1:.4f} / {D_G_z2:.4f}')
                save_image(fake_images.view(b_size, 1, 28, 28).data[:64], os.path.join(output_dir, f'fake_samples_vanilla_gan_{i:03d}.png'), normalize=True)

        # Save models
        torch.save(netG.state_dict(), 'output/netG_vanilla_gan.pth')
        torch.save(netD.state_dict(), 'output/netD_vanilla_gan.pth')


def generate_vanilla_gan_images(num_images,nz, model_path='output/netG_vanilla_gan.pth'):
    netG = VanillaGAN_Generator(nz, ngf, input_size).to(device)
    netG.load_state_dict(torch.load(model_path))
    netG.eval()
    
    noise = torch.randn(num_images, nz, device=device)
    with torch.no_grad():
        fake_images = netG(noise).detach().cpu()
    return fake_images.view(num_images, 1, 28, 28)
