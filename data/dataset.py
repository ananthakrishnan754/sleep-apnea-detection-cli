import os
import json
import torch
from torch.utils.data import Dataset

class ApneaFusionDataset(Dataset):
    def __init__(self, split='train', config='configs/config.yaml'):
        self.split = split
        self.items = []
        # enforce inter-patient: only use records in split
        with open(config) as f:
            pass
    def __len__(self): return len(self.items)
    def __getitem__(self, idx): return self.items[idx]
