import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.utils import save_image
import os
from dotenv import load_dotenv

GREEN = "\033[92m"
RESET = "\033[0m"

load_dotenv()

from models.style_gan import StyleGANDiscriminator, StyleGANGenerator
from utils.style_gan import generator_loss, discriminator_loss, initialize_weights

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Hyperparameters
# nz = 100  # Size of z latent vector (i.e. size of generator input)
ngf = 64  # Size of feature maps in generator
ndf = 64  # Size of feature maps in discriminator
nc = int(
    os.getenv("nc")
)  # Number of color channels in the training images. For color images this is 3

criterion = nn.BCELoss()

transform = transforms.Compose(
    [
        transforms.Resize(64),
        transforms.CenterCrop(64),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
    ]
)


output_dir = "output"
os.makedirs(output_dir, exist_ok=True)


def train_style_gan(dataroot, num_epochs, lr):
    nz = 512

    print(f"{GREEN}Train Style GAN function is called{RESET}")
    dataset = datasets.ImageFolder(root=dataroot, transform=transform)
    dataloader = DataLoader(dataset, batch_size=128, shuffle=True, num_workers=4)
    G = StyleGANGenerator(nz, [512, 256, 128, 64, 32, nc]).to(device)
    D = StyleGANDiscriminator([nc, 32, 64, 128, 256, 512]).to(device)

    G.apply(initialize_weights)
    D.apply(initialize_weights)

    optimizer_G = optim.Adam(G.parameters(), lr=lr, betas=(0.0, 0.99))
    optimizer_D = optim.Adam(D.parameters(), lr=lr, betas=(0.0, 0.99))

    for epoch in range(num_epochs):
        for i, (imgs, _) in enumerate(dataloader):
            real_imgs = imgs.to(device)
            batch_size = real_imgs.size(0)

            # Train Discriminator
            z = torch.randn(batch_size, nz, device=device)
            fake_imgs = G(z).detach()
            loss_D = discriminator_loss(D, real_imgs, fake_imgs)
            optimizer_D.zero_grad()
            loss_D.backward()
            optimizer_D.step()

            # Train Generator
            z = torch.randn(batch_size, nz, device=device)
            fake_imgs = G(z)
            loss_G = generator_loss(D, fake_imgs)
            optimizer_G.zero_grad()
            loss_G.backward()
            optimizer_G.step()

        print(
            f"Epoch [{epoch}/{num_epochs}] - Loss D: {loss_D.item():.4f}, Loss G: {loss_G.item():.4f}"
        )
