import torch.nn as nn

def initialize_weights(model):
    """
    Initialize weights for the GAN model.
    
    Parameters:
    - model: The neural network model whose weights need to be initialized.
    """
    for m in model.modules():
        if isinstance(m, (nn.Conv2d, nn.ConvTranspose2d)):
            nn.init.normal_(m.weight.data, 0.0, 0.02)
        elif isinstance(m, nn.BatchNorm2d):
            nn.init.normal_(m.weight.data, 1.0, 0.02)
            nn.init.constant_(m.bias.data, 0)
