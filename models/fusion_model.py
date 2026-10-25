import torch
import torch.nn as nn
from .resnet_ecg import SpectroBranch
from .rr_bilstm import RRBranch
from .spo2_mlp import SpO2Branch

class SleepApneaFusion(nn.Module):
    def __init__(self, use_spo2=True):
        super().__init__()
        self.use_spo2 = use_spo2
        self.spectro = SpectroBranch(out_dim=256)
        self.rr = RRBranch(out_dim=256)
        if use_spo2:
            self.spo2 = SpO2Branch(in_dim=9, out_dim=16)
            in_f = 256+256+16
        else:
            in_f = 256+256
        self.head = nn.Sequential(
            nn.Linear(in_f, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, 2)
        )

    def forward(self, spec=None, rr=None, spo2=None):
        feats = []
        if spec is not None:
            feats.append(self.spectro(spec))
        if rr is not None:
            feats.append(self.rr(rr))
        if self.use_spo2 and spo2 is not None:
            feats.append(self.spo2(spo2))
        x = torch.cat(feats, dim=1)
        return self.head(x)
