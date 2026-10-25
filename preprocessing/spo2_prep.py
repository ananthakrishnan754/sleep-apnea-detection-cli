import numpy as np

def spo2_features(spo2_arr):
    spo2 = np.array(spo2_arr)
    if len(spo2) == 0:
        return np.zeros(9)
    feats = [
        np.min(spo2), np.max(spo2), np.mean(spo2), np.std(spo2), np.var(spo2),
        float(np.mean((spo2 - np.mean(spo2))**3)/(np.std(spo2)**3 + 1e-8)),
        np.max(spo2)-np.min(spo2),
        np.sum(spo2 <= 90), np.sum(spo2 <= 94)
    ]
    return np.array(feats, dtype=np.float32)
