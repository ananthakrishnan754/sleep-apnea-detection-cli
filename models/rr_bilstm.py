import torch
import torch.nn as nn

class RRBranch(nn.Module):
    def __init__(self, in_dim=3, hidden=64, out_dim=256):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv1d(in_dim, 32, kernel_size=5, padding=2),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.MaxPool1d(2),
            nn.Conv1d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.MaxPool1d(2),
        )
        self.bilstm = nn.LSTM(64, hidden, batch_first=True, bidirectional=True)
        self.attn = nn.Linear(2*hidden, 1)
        self.fc = nn.Linear(2*hidden, out_dim)

    def forward(self, x):
        # x: (B, L, in_dim) -> (B,in_dim,L)
        x = x.transpose(1,2)
        x = self.conv(x)
        x = x.transpose(1,2)
        out,_ = self.bilstm(x)
        w = torch.softmax(self.attn(out), dim=1)
        ctx = torch.sum(w*out, dim=1)
        return self.fc(ctx)
