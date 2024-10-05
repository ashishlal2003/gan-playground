import torch
import torch.nn as nn

class CGAN_Generator(nn.Module):
    def __init__(self, nz, ngf, nc, n_classes):
        super(CGAN_Generator, self).__init__()
        self.label_embedding = nn.Embedding(n_classes, n_classes)
        self.main = nn.Sequential(
            nn.ConvTranspose2d(nz + n_classes, ngf * 8, 4, 1, 0, bias=False),
            nn.BatchNorm2d(ngf * 8),
            nn.ReLU(True),
            nn.ConvTranspose2d(ngf * 8, ngf * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf * 4),
            nn.ReLU(True),
            nn.ConvTranspose2d(ngf * 4, ngf * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf * 2),
            nn.ReLU(True),
            nn.ConvTranspose2d(ngf * 2, ngf, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf),
            nn.ReLU(True),
            nn.ConvTranspose2d(ngf, nc, 4, 2, 1, bias=False),
            nn.Tanh()
        )

    def forward(self, noise, labels):
        label_embedded = self.label_embedding(labels)  
        noise = noise.view(noise.size(0), noise.size(1), 1, 1)
        label_embedded = label_embedded.view(label_embedded.size(0), label_embedded.size(1), 1, 1)
        input = torch.cat([noise, label_embedded], dim=1)

        return self.main(input)



class CGAN_Discriminator(nn.Module):
    def __init__(self, nc, ndf, n_classes):
        super(CGAN_Discriminator, self).__init__()
        self.label_embedding = nn.Embedding(n_classes, nc) 
        self.main = nn.Sequential(
            nn.Conv2d(nc + nc, ndf, 4, 2, 1, bias=False), 
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(ndf, ndf * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ndf * 2),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(ndf * 2, ndf * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ndf * 4),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(ndf * 4, ndf * 8, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ndf * 8),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(ndf * 8, 1, 4, 1, 0, bias=False),
            nn.Sigmoid()
        )

    def forward(self, img, labels):
        label_embedded = self.label_embedding(labels).unsqueeze(2).unsqueeze(3)
        label_embedded = label_embedded.expand(img.size(0), img.size(1), img.size(2), img.size(3))
        input = torch.cat([img, label_embedded], dim=1)
        return self.main(input)
