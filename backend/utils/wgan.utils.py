import torch.nn as nn

def wgan_gp_initialize_weights(model):
    """
    Initialize weights according to the WGAN-GP paper.
    
    Parameters:
    - model: The neural network model whose weights need to be initialized.
    """
    for m in model.modules():
        if isinstance(m, (nn.Conv2d, nn.ConvTranspose2d)):
            # Initialize convolutional layers with normal distribution
            nn.init.normal_(m.weight.data, 0.0, 0.02)
        elif isinstance(m, nn.BatchNorm2d):
            # Initialize batch norm layers
            nn.init.normal_(m.weight.data, 1.0, 0.02)
            nn.init.constant_(m.bias.data, 0)

