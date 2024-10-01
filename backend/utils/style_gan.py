import torch
import torch.nn.functional as F
import torch.nn as nn

def generator_loss(D, fake_imgs):
    logits_fake = D(fake_imgs)
    return F.binary_cross_entropy_with_logits(logits_fake, torch.ones_like(logits_fake))

def discriminator_loss(D, real_imgs, fake_imgs):
    logits_real = D(real_imgs)
    logits_fake = D(fake_imgs)
    loss_real = F.binary_cross_entropy_with_logits(logits_real, torch.ones_like(logits_real))
    loss_fake = F.binary_cross_entropy_with_logits(logits_fake, torch.zeros_like(logits_fake))
    return (loss_real + loss_fake) / 2


def initialize_weights(m):
    if isinstance(m, nn.Conv2d) or isinstance(m, nn.Linear):
        nn.init.xavier_uniform_(m.weight)
        if m.bias is not None:
            nn.init.constant_(m.bias, 0)
