import torch
import torch.nn as nn


# Generator Model
class Generator(nn.Module):
    def __init__(self, nz, ngf, nc):
        super(Generator, self).__init__()
        self.main = nn.Sequential(
            nn.Linear(nz, ngf * 8),  # Fully connected layer
            nn.ReLU(True),
            nn.Linear(ngf * 8, ngf * 4),
            nn.ReLU(True),
            nn.Linear(ngf * 4, ngf * 2),
            nn.ReLU(True),
            nn.Linear(ngf * 2, nc),
            nn.Tanh(),  # Output layer with Tanh activation
        )

    def forward(self, input):
        return self.main(input)


# Discriminator Model
# class Discriminator(nn.Module):
#     def __init__(self, nc, ndf):
#         super(Discriminator, self).__init__()
#         self.main = nn.Sequential(
#             nn.Linear(nc, ndf * 2),  # Fully connected layer
#             nn.LeakyReLU(0.2, inplace=True),
#             nn.Linear(ndf * 2, ndf * 4),
#             nn.LeakyReLU(0.2, inplace=True),
#             nn.Linear(ndf * 4, 1),  # Output layer
#             nn.Sigmoid()  # Sigmoid for binary classification
#         )

#     def forward(self, input):
#         return self.main(input)


class Discriminator(nn.Module):
    def __init__(self, nc, ndf):
        super(Discriminator, self).__init__()
        self.main = nn.Sequential(
            nn.Linear(64 * 64 * nc, ndf * 2),  # Flattened image size as input
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(ndf * 2, ndf * 4),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(ndf * 4, 1),  # Output layer for binary classification
            nn.Sigmoid(),  # Sigmoid for real/fake classification
        )

    def forward(self, input):
        input = input.view(
            input.size(0), -1
        )  # Flatten the input (batch_size, num_features)
        return self.main(input)
