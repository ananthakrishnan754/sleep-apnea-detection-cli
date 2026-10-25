import json
import os

def load_split(cfg_path='configs/config.yaml'):
    # simple loader
    pass

def enforce_patient_split(windows):
    # windows must have record_id
    seen = set()
    splits = {'train':set(), 'val':set(), 'test':set()}
    # placeholder
    return splits
