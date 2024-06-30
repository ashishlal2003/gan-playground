import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, utils
from torch.utils.data import DataLoader
from dcgan import Generator as DCGANGenerator, Discriminator as DCGANDiscriminator, initialize_weights as dcgan_initialize_weights
from wgan_gp import Generator as WGANGPGenerator, Discriminator as WGANGPDiscriminator, initialize_weights as wgan_gp_initialize_weights

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Constants
BATCH_SIZE = 64
Z_DIM = 100
IMAGE_SIZE = 64
CHANNELS_IMG = 3
FEATURES_D = 64
FEATURES_G = 64
CRITIC_ITERATIONS = 5
LAMBDA_GP = 10
NUM_EPOCHS = 10

# Dataset
transform = transforms.Compose([
    transforms.Resize(IMAGE_SIZE),
    transforms.CenterCrop(IMAGE_SIZE),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])

dataset = datasets.ImageFolder(root="C://Users//ashis//Mirror//Important_files//IIIT//Machine Learning - Personal//Generative Adveserial Networks//DCGAN//celeb_dataset", transform=transform)
dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

# Initialize models
dcgan_generator = DCGANGenerator(Z_DIM, CHANNELS_IMG, FEATURES_G).to(device)
dcgan_discriminator = DCGANDiscriminator(CHANNELS_IMG, FEATURES_D).to(device)
wgan_gp_generator = WGANGPGenerator(Z_DIM, CHANNELS_IMG, FEATURES_G).to(device)
wgan_gp_discriminator = WGANGPDiscriminator(CHANNELS_IMG, FEATURES_D).to(device)

# Initialize model weights
dcgan_initialize_weights(dcgan_generator)
dcgan_initialize_weights(dcgan_discriminator)
wgan_gp_initialize_weights(wgan_gp_generator)
wgan_gp_initialize_weights(wgan_gp_discriminator)

# Optimizers
optimizer_dcgan_discriminator = optim.Adam(dcgan_discriminator.parameters(), lr=0.0002, betas=(0.5, 0.999))
optimizer_dcgan_generator = optim.Adam(dcgan_generator.parameters(), lr=0.0002, betas=(0.5, 0.999))
optimizer_wgan_gp_discriminator = optim.Adam(wgan_gp_discriminator.parameters(), lr=0.0002, betas=(0.5, 0.999))
optimizer_wgan_gp_generator = optim.Adam(wgan_gp_generator.parameters(), lr=0.0002, betas=(0.5, 0.999))

# Loss function
criterion = nn.BCELoss()

# Training loop
for epoch in range(NUM_EPOCHS):
    for batch_idx, (real, _) in enumerate(dataloader):
        real = real.to(device)
        cur_batch_size = real.shape[0]

        # Train DCGAN Discriminator
        dcgan_discriminator.zero_grad()
        z = torch.randn(cur_batch_size, Z_DIM, 1, 1).to(device)
        fake = dcgan_generator(z)
        disc_fake_pred = dcgan_discriminator(fake.detach())
        disc_real_pred = dcgan_discriminator(real)
        loss_dcgan_discriminator = criterion(disc_fake_pred, torch.zeros_like(disc_fake_pred)) + criterion(disc_real_pred, torch.ones_like(disc_real_pred))
        loss_dcgan_discriminator.backward()
        optimizer_dcgan_discriminator.step()

        # Train DCGAN Generator
        dcgan_generator.zero_grad()
        disc_fake_pred = dcgan_discriminator(fake)
        loss_dcgan_generator = criterion(disc_fake_pred, torch.ones_like(disc_fake_pred))
        loss_dcgan_generator.backward()
        optimizer_dcgan_generator.step()

        # Train WGAN-GP Discriminator
        for _ in range(CRITIC_ITERATIONS):
            wgan_gp_discriminator.zero_grad()
            z = torch.randn(cur_batch_size, Z_DIM, 1, 1).to(device)
            fake = wgan_gp_generator(z)
            disc_fake_pred = wgan_gp_discriminator(fake.detach())
            disc_real_pred = wgan_gp_discriminator(real)
            loss_wgan_gp_discriminator = -(torch.mean(disc_real_pred) - torch.mean(disc_fake_pred))
            loss_wgan_gp_discriminator.backward()
            optimizer_wgan_gp_discriminator.step()

            # Clip discriminator parameters
            for p in wgan_gp_discriminator.parameters():
                p.data.clamp_(-0.01, 0.01)

        # Train WGAN-GP Generator
        wgan_gp_generator.zero_grad()
        disc_fake_pred = wgan_gp_discriminator(fake)
        loss_wgan_gp_generator = -torch.mean(disc_fake_pred)
        loss_wgan_gp_generator.backward()
        optimizer_wgan_gp_generator.step()

        # Print losses
        if batch_idx % 100 == 0:
            print(
                f"Epoch [{epoch}/{NUM_EPOCHS}] Batch {batch_idx}/{len(dataloader)} "
                f"Loss DCGAN D: {loss_dcgan_discriminator:.4f}, G: {loss_dcgan_generator:.4f} "
                f"Loss WGAN-GP D: {loss_wgan_gp_discriminator:.4f}, G: {loss_wgan_gp_generator:.4f}"
            )

    # Save generated images
    with torch.no_grad():
        fixed_noise = torch.randn(64, Z_DIM, 1, 1).to(device)
        fake = dcgan_generator(fixed_noise).detach().cpu()
        utils.save_image(fake, f"dcgan_generated_image_epoch_{epoch}.png", normalize=True)

        fake = wgan_gp_generator(fixed_noise).detach().cpu()
        utils.save_image(fake, f"wgan_gp_generated_image_epoch_{epoch}.png", normalize=True)
