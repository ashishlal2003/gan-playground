import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.utils import save_image
from dotenv import load_dotenv
import os

GREEN = "\033[92m"
RESET = "\033[0m"

load_dotenv()

from models.wgan import Generator, Critic

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


ngf = 64
ndf = 64
nc = int(os.getenv("nc"))
clip_value = 0.01


# Load the dataset
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

model_files_dir_wgan = "model_files_dir_wgan"
os.makedirs(model_files_dir_wgan, exist_ok=True)


def weight_clipping(model, clip_value):
    for p in model.parameters():
        p.data.clamp_(-clip_value, clip_value)


def train_wgan(dataroot, num_epochs, lr, nz):

    print(f"{GREEN}Train WGAN function is called{RESET}")
    dataset = datasets.ImageFolder(root=dataroot, transform=transform)
    dataloader = DataLoader(dataset, batch_size=128, shuffle=True, num_workers=4)

    netG = Generator(nz, ngf, nc).to(device)
    netC = Critic(nc, ndf).to(device)

    optimizerC = optim.Adam(netC.parameters(), lr=lr, betas=(0.5, 0.999))
    optimizerG = optim.Adam(netG.parameters(), lr=lr, betas=(0.5, 0.999))

    for epoch in range(num_epochs):
        for i, data in enumerate(dataloader, 0):
            # (1) Update Critic network: maximize D(x) - D(G(z))

            netC.zero_grad()
            real_cpu = data[0].to(device)
            b_size = real_cpu.size(0)

            output_real = netC(real_cpu).view(-1)
            D_real = output_real.mean()

            noise = torch.randn(b_size, nz, 1, 1, device=device)
            fake = netG(noise)
            output_fake = netC(fake.detach()).view(-1)
            D_fake = output_fake.mean()

            # Compute critic loss
            c_loss = D_fake - D_real
            c_loss.backward()
            optimizerC.step()
            weight_clipping(netC, clip_value)

            # (2) Update Generator network: maximize D(G(z))
            if i % 5 == 0:  # Train generator less frequently than the critic
                netG.zero_grad()
                output_fake = netC(fake).view(-1)
                g_loss = (
                    -output_fake.mean()
                )  # Negative because we want to maximize the score
                g_loss.backward()
                optimizerG.step()

            if i % 50 == 0:
                print(
                    f"[{epoch}/{num_epochs}][{i}/{len(dataloader)}] Loss_C: {c_loss.item():.4f} Loss_G: {g_loss.item():.4f} D(x): {D_real:.4f} D(G(z)): {D_fake:.4f}"
                )

            # Save fake images generated at each epoch
            if i % 50 == 0:
                try:
                    save_image(fake.data[:64], os.path.join(output_dir, f'fake_samples_epoch_{epoch:03d}_step_{i:03d}.png'), normalize=True)
                except Exception as e:
                    print(f"Error saving image at i {i}: {e}")

        # Save models
        torch.save(netG.state_dict(), os.path.join(model_files_dir_wgan, 'netG.pth'))
        torch.save(netC.state_dict(), os.path.join(model_files_dir_wgan, 'netC.pth'))



def generate_images(num_images, model_path="model_files_dir_wgan/netG_wgan.pth", nz=100):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    netG = Generator(nz, ngf, nc).to(device)
    netG.load_state_dict(torch.load(model_path))
    netG.eval()

    noise = torch.randn(num_images, nz, 1, 1, device=device)
    with torch.no_grad():
        fake_images = netG(noise).detach().cpu()    
    return fake_images
