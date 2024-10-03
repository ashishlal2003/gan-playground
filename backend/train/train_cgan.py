import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.utils import save_image
import os
from dotenv import load_dotenv

load_dotenv()

from models.cgan import CGAN_Generator, CGAN_Discriminator  # Import CGAN models

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Hyperparameters
ngf = 64  # Size of feature maps in generator
ndf = 64  # Size of feature maps in discriminator
nc = int(os.getenv("nc"))  # Number of color channels in the training images
n_classes = 10  # Number of classes (adjust as needed)

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

# Modify the train_cgan function to accept dataroot as a parameter
def train_cgan(dataroot, num_epochs, lr, nz):
    dataset = datasets.ImageFolder(root=dataroot, transform=transform)
    dataloader = DataLoader(dataset, batch_size=128, shuffle=True, num_workers=4)

    netG = CGAN_Generator(nz, ngf, nc, n_classes).to(device)
    netD = CGAN_Discriminator(nc, ndf, n_classes).to(device)

    optimizerD = optim.Adam(netD.parameters(), lr=lr, betas=(0.5, 0.999))
    optimizerG = optim.Adam(netG.parameters(), lr=lr, betas=(0.5, 0.999))

    for epoch in range(num_epochs):
        for i, data in enumerate(dataloader, 0):
            images, labels = data
            images, labels = images.to(device), labels.to(device)

            # (1) Update D network: maximize log(D(x)) + log(1 - D(G(z)))
            ## Train with real images
            netD.zero_grad()
            b_size = images.size(0)
            label_real = torch.full((b_size,), 1, dtype=torch.float, device=device)
            output = netD(images, labels).view(-1)
            errD_real = criterion(output, label_real)
            errD_real.backward()
            D_x = output.mean().item()

            ## Train with fake images
            noise = torch.randn(b_size, nz, device=device)
            fake_images = netG(noise, labels)
            label_fake = torch.full((b_size,), 0, dtype=torch.float, device=device)
            output = netD(fake_images.detach(), labels).view(-1)
            errD_fake = criterion(output, label_fake)
            errD_fake.backward()
            D_G_z1 = output.mean().item()
            errD = errD_real + errD_fake
            optimizerD.step()

            # (2) Update G network: maximize log(D(G(z)))
            netG.zero_grad()
            label_real.fill_(1)  # Flip labels for generator loss
            output = netD(fake_images, labels).view(-1)
            errG = criterion(output, label_real)
            errG.backward()
            D_G_z2 = output.mean().item()
            optimizerG.step()

            if i % 50 == 0:
                print(f'[{epoch}/{num_epochs}][{i}/{len(dataloader)}] Loss_D: {errD.item():.4f} Loss_G: {errG.item():.4f} D(x): {D_x:.4f} D(G(z)): {D_G_z1:.4f} / {D_G_z2:.4f}')
                save_image(fake_images.data[:64], os.path.join(output_dir, f'fake_samples_cgan_{i:03d}.png'), normalize=True)

        # Save models
        torch.save(netG.state_dict(), 'output/netG_cgan.pth')
        torch.save(netD.state_dict(), 'output/netD_cgan.pth')


def generate_cgan_images(num_images,nz, labels, model_path='output/netG_cgan.pth'):
    netG = CGAN_Generator(nz, ngf, nc, n_classes).to(device)
    netG.load_state_dict(torch.load(model_path))
    netG.eval()
    
    noise = torch.randn(num_images, nz, device=device)
    labels = torch.tensor(labels, device=device)
    with torch.no_grad():
        fake_images = netG(noise, labels).detach().cpu()
    return fake_images
