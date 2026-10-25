import torch.nn as nn
from torchvision import models

class SpectroBranch(nn.Module):
    def __init__(self, out_dim=256, pretrained=True):
        super().__init__()
        self.backbone = models.resnet18(weights='IMAGENET1K_V1' if pretrained else None)
        self.backbone.conv1 = nn.Conv2d(1, 64, kernel_size=7, stride=2, padding=3, bias=False)
        self.backbone.fc = nn.Identity()
        self.fc = nn.Linear(512, out_dim)

    def forward(self, x):
        feat = self.backbone(x)
        return self.fc(feat)
