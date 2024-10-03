import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.utils import save_image
import os
from dotenv import load_dotenv

load_dotenv()

from models.wgan_gp import Generator, Critic  

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Hyperparameters
ngf = 64  # Size of feature maps in generator
ndf = 64  # Size of feature maps in critic
nc = int(os.getenv("nc"))    # Number of color channels in the training images. For color images this is 3
clip_value = 0.01  # Weight clipping range for WGAN
critic_iters = 5  # Number of Critic updates per Generator update

# Output directory
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

transform = transforms.Compose([
    transforms.Resize(64),
    transforms.CenterCrop(64),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])


def clip_weights(model, clip_value):
    for p in model.parameters():
        p.data.clamp_(-clip_value, clip_value)


def train_wgan(dataroot, num_epochs, lr, nz, clip_value=0.01, critic_iters=5):
    dataset = datasets.ImageFolder(root=dataroot, transform=transform)
    dataloader = DataLoader(dataset, batch_size=128, shuffle=True, num_workers=4)

    netG = Generator(nz, ngf, nc).to(device)
    netC = Critic(nc, ndf).to(device)  # Critic replaces Discriminator

    optimizerC = optim.RMSprop(netC.parameters(), lr=lr)  # WGAN uses RMSProp
    optimizerG = optim.RMSprop(netG.parameters(), lr=lr)

    for epoch in range(num_epochs):
        for i, data in enumerate(dataloader, 0):
            # (1) Update Critic network: maximize Wasserstein distance
            for _ in range(critic_iters):
                netC.zero_grad()
                real_cpu = data[0].to(device)
                b_size = real_cpu.size(0)

                # Train with real data
                real_output = netC(real_cpu).view(-1)
                errC_real = -torch.mean(real_output)

                # Train with fake data
                noise = torch.randn(b_size, nz, 1, 1, device=device)
                fake = netG(noise)
                fake_output = netC(fake.detach()).view(-1)
                errC_fake = torch.mean(fake_output)

                # Critic loss
                errC = errC_real + errC_fake
                errC.backward()
                optimizerC.step()

                # Weight clipping
                clip_weights(netC, clip_value)

            # (2) Update Generator network: minimize -C(G(z))
            netG.zero_grad()
            output = netC(fake).view(-1)
            errG = -torch.mean(output)
            errG.backward()
            optimizerG.step()

            if i % 50 == 0:
                print(f'[{epoch}/{num_epochs}][{i}/{len(dataloader)}] Loss_C: {errC.item():.4f} Loss_G: {errG.item():.4f}')
                
                try:
                    save_image(fake.data[:64], os.path.join(output_dir, f'fake_samples_step_{i:03d}.png'), normalize=True)
                except Exception as e:
                    print(f"Error saving image at i {i}: {e}")

        # Save models
        torch.save(netG.state_dict(), 'output/netG_wgan.pth')
        torch.save(netC.state_dict(), 'output/netC.pth')


def generate_images_wgan(num_images, nz, model_path='output/netG_wgan.pth'):
    netG = Generator(nz, ngf, nc).to(device)
    netG.load_state_dict(torch.load(model_path))
    netG.eval()

    noise = torch.randn(num_images, nz, 1, 1, device=device)
    with torch.no_grad():
        fake_images = netG(noise).detach().cpu()
    return fake_images
