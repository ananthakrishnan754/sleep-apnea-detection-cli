import torch.nn as nn

class SpO2Branch(nn.Module):
    def __init__(self, in_dim=9, out_dim=16):
        super().__init__()
        self.mlp = nn.Sequential(
            nn.Linear(in_dim,out_dim),
            nn.ReLU(),
            nn.Dropout(0.2),
        )
    def forward(self,x):
        return self.mlp(x)
