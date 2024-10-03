import torch
import torch.nn as nn

class VanillaGAN_Generator(nn.Module):
    def __init__(self, nz, ngf, nc):
        super(VanillaGAN_Generator, self).__init__()
        self.main = nn.Sequential(
            nn.Linear(nz, ngf * 4),
            nn.ReLU(True),
            nn.Linear(ngf * 4, ngf * 8),
            nn.ReLU(True),
            nn.Linear(ngf * 8, ngf * 16),
            nn.ReLU(True),
            nn.Linear(ngf * 16, nc),
            nn.Tanh()
        )

    def forward(self, input):
        return self.main(input)


class VanillaGAN_Discriminator(nn.Module):
    def __init__(self, nc, ndf):
        super(VanillaGAN_Discriminator, self).__init__()
        self.main = nn.Sequential(
            nn.Linear(nc, ndf * 16),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(ndf * 16, ndf * 8),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(ndf * 8, ndf * 4),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(ndf * 4, 1),
            nn.Sigmoid()
        )

    def forward(self, input):
        return self.main(input)
