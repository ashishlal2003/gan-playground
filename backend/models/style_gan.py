import torch
import torch.nn as nn

class MappingNetwork(nn.Module):
    def __init__(self, latent_dim, hidden_dim=512, num_layers=8):
        super(MappingNetwork, self).__init__()
        layers = []
        for _ in range(num_layers):
            layers.append(nn.Linear(latent_dim, hidden_dim))
            layers.append(nn.LeakyReLU(0.2))
        self.mapping = nn.Sequential(*layers)

    def forward(self, z):
        return self.mapping(z)

class SynthesisBlock(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(SynthesisBlock, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=1, padding=1)
        self.adain = nn.InstanceNorm2d(out_channels)
        self.style_mod = nn.Linear(512, out_channels)  # Style modulation

    def forward(self, x, style):
        style_mod = self.style_mod(style).view(-1, style.size(1), 1, 1)  # Reshape to match dimensions
        x = self.conv(x)
        x = self.adain(x) * style_mod  # Apply style modulation
        return x

class SynthesisNetwork(nn.Module):
    def __init__(self, channels):
        super(SynthesisNetwork, self).__init__()
        self.channels = channels
        self.blocks = nn.ModuleList([
            SynthesisBlock(channels[i], channels[i+1])
            for i in range(len(channels) - 1)
        ])

    def forward(self, style):
        x = torch.randn(style.size(0), self.channels[0], 4, 4)  # Start with small noise
        for block in self.blocks:
            x = block(x, style)  # Inject style at each layer
        return x

class StyleGANGenerator(nn.Module):
    def __init__(self, latent_dim, channels):
        super(StyleGANGenerator, self).__init__()
        self.mapping = MappingNetwork(latent_dim)
        self.synthesis = SynthesisNetwork(channels)

    def forward(self, z):
        style = self.mapping(z)  # Map latent vector to style
        img = self.synthesis(style)  # Generate image
        return img

class DiscriminatorBlock(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(DiscriminatorBlock, self).__init__()
        self.block = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=1, padding=1),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1),
            nn.LeakyReLU(0.2, inplace=True),
            nn.AvgPool2d(kernel_size=2)  # Downsample
        )

    def forward(self, x):
        return self.block(x)

class StyleGANDiscriminator(nn.Module):
    def __init__(self, channels):
        super(StyleGANDiscriminator, self).__init__()
        self.blocks = nn.ModuleList([
            DiscriminatorBlock(channels[i], channels[i+1])
            for i in range(len(channels) - 1)
        ])
        self.final_conv = nn.Conv2d(channels[-1], 1, kernel_size=4)  # Final layer to output single scalar

    def forward(self, img):
        x = img
        for block in self.blocks:
            x = block(x)
        x = self.final_conv(x)
        return x.view(-1, 1).squeeze(1)  # Output scalar for each image
