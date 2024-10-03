import torch
import torch.nn as nn

# Residual Block for Generator
class ResidualBlock(nn.Module):
    def __init__(self, in_channels):
        super(ResidualBlock, self).__init__()
        self.block = nn.Sequential(
            nn.Conv2d(in_channels, in_channels, kernel_size=3, stride=1, padding=1),
            nn.InstanceNorm2d(in_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(in_channels, in_channels, kernel_size=3, stride=1, padding=1),
            nn.InstanceNorm2d(in_channels)
        )
    
    def forward(self, x):
        return x + self.block(x)

# Generator for CycleGAN
class CycleGAN_Generator(nn.Module):
    def __init__(self, in_channels, out_channels, num_residual_blocks=9):
        super(CycleGAN_Generator, self).__init__()

        # Initial convolution block
        model = [
            nn.Conv2d(in_channels, 64, kernel_size=7, stride=1, padding=3, bias=False),
            nn.InstanceNorm2d(64),
            nn.ReLU(inplace=True)
        ]

        # Downsampling
        in_features = 64
        out_features = in_features * 2
        for _ in range(2):
            model += [
                nn.Conv2d(in_features, out_features, kernel_size=3, stride=2, padding=1, bias=False),
                nn.InstanceNorm2d(out_features),
                nn.ReLU(inplace=True)
            ]
            in_features = out_features
            out_features = in_features * 2

        # Residual blocks
        for _ in range(num_residual_blocks):
            model += [ResidualBlock(in_features)]

        # Upsampling
        out_features = in_features // 2
        for _ in range(2):
            model += [
                nn.ConvTranspose2d(in_features, out_features, kernel_size=3, stride=2, padding=1, output_padding=1, bias=False),
                nn.InstanceNorm2d(out_features),
                nn.ReLU(inplace=True)
            ]
            in_features = out_features
            out_features = in_features // 2

        # Output layer
        model += [nn.Conv2d(64, out_channels, kernel_size=7, stride=1, padding=3),
                  nn.Tanh()]

        self.model = nn.Sequential(*model)

    def forward(self, x):
        return self.model(x)

# PatchGAN Discriminator
class CycleGAN_Discriminator(nn.Module):
    def __init__(self, in_channels):
        super(CycleGAN_Discriminator, self).__init__()

        def discriminator_block(in_filters, out_filters, stride):
            return [
                nn.Conv2d(in_filters, out_filters, kernel_size=4, stride=stride, padding=1),
                nn.InstanceNorm2d(out_filters),
                nn.LeakyReLU(0.2, inplace=True)
            ]

        self.model = nn.Sequential(
            *discriminator_block(in_channels, 64, 2),
            *discriminator_block(64, 128, 2),
            *discriminator_block(128, 256, 2),
            *discriminator_block(256, 512, 1),
            nn.Conv2d(512, 1, kernel_size=4, stride=1, padding=1)  # PatchGAN outputs 1x1 patches
        )

    def forward(self, x):
        return self.model(x)

# Initialize generators and discriminators
def initialize_cyclegan_models():
    netG_A2B = CycleGAN_Generator(in_channels=3, out_channels=3)
    netG_B2A = CycleGAN_Generator(in_channels=3, out_channels=3)
    netD_A = CycleGAN_Discriminator(in_channels=3)
    netD_B = CycleGAN_Discriminator(in_channels=3)
    
    return netG_A2B, netG_B2A, netD_A, netD_B
