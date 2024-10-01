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

from models.vanilla_gan import Generator, Discriminator

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Hyperparameters
ngf = 64
ndf = 64
nc = int(os.getenv("nc"))

# Output directory
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

transform = transforms.Compose(
    [
        transforms.Resize(64),
        transforms.CenterCrop(64),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
    ]
)


def train_vanilla_gan(
    dataroot,
    num_epochs,
    lr,
    nz,
):

    print(f"{GREEN}Train Vanilla GAN function is called{RESET}")
    dataset = datasets.ImageFolder(root=dataroot, transform=transform)
    dataloader = DataLoader(dataset, batch_size=128, shuffle=True, num_workers=4)

    netG = Generator(nz, ngf, nc).to(device)
    netD = Discriminator(nc, ndf).to(device)

    # Loss function
    criterion = nn.BCELoss()

    # Optimizers
    optimizerD = optim.Adam(netD.parameters(), lr=lr, betas=(0.5, 0.999))
    optimizerG = optim.Adam(netG.parameters(), lr=lr, betas=(0.5, 0.999))

    # Training Loop
    num_epochs = 50
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    for epoch in range(num_epochs):
        for i, data in enumerate(dataloader, 0):
            # Train Discriminator
            netD.zero_grad()
            real_cpu = data[0].to(device)
            b_size = real_cpu.size(0)
            label = torch.full(
                (b_size,), 1, dtype=torch.float, device=device
            )  # Real labels
            output = netD(real_cpu.view(b_size, -1)).view(-1)
            errD_real = criterion(output, label)
            errD_real.backward()

            # Train with all-fake batch
            noise = torch.randn(b_size, nz, device=device)
            fake = netG(noise)
            label.fill_(0)  # Fake labels
            # output = netD(fake.detach().view(b_size, -1)).view(-1)
            output = netD(fake.detach()).view(-1)
            errD_fake = criterion(output, label)
            errD_fake.backward()
            optimizerD.step()

            # Train Generator
            netG.zero_grad()
            label.fill_(1)  # Labels for generator to fool the discriminator
            output = netD(fake.view(b_size, -1)).view(-1)
            errG = criterion(output, label)
            errG.backward()
            optimizerG.step()

            if i % 50 == 0:
                print(
                    f"[{epoch}/{num_epochs}][{i}/{len(dataloader)}] Loss_D: {errD_real.item() + errD_fake.item():.4f} Loss_G: {errG.item():.4f}"
                )

                # Save fake images generated at each epoch
                save_image(
                    fake.data[:64],
                    os.path.join(output_dir, f"fake_samples_epoch_{epoch}.png"),
                    normalize=True,
                )

    # Save models
    torch.save(netG.state_dict(), "output/netG.pth")
    torch.save(netD.state_dict(), "output/netD.pth")
