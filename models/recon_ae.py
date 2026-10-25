import torch
import torch.nn as nn

class RRDenoiseAE(nn.Module):
    def __init__(self, in_ch=3, hidden=32):
        super().__init__()
        self.enc = nn.Sequential(
            nn.Conv1d(in_ch, hidden, 5, padding=2),
            nn.ReLU(),
            nn.Conv1d(hidden, hidden*2, 5, stride=2, padding=2),
            nn.ReLU(),
        )
        self.dec = nn.Sequential(
            nn.ConvTranspose1d(hidden*2, hidden, 4, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv1d(hidden, in_ch, 3, padding=1),
        )
    def forward(self, x):
        # x (B,L,3)
        x = x.transpose(1,2)
        z = self.enc(x)
        y = self.dec(z)
        y = y.transpose(1,2)
        return y
