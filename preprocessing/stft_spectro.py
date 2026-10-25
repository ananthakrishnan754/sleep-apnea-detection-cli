import numpy as np
from scipy.signal import stft
import cv2

def ecg_to_spectrogram(ecg, fs=100, nperseg=512, noverlap=256, size=224):
    try:
        f, t, Zxx = stft(ecg, fs=fs, nperseg=nperseg, noverlap=noverlap)
        S = np.abs(Zxx)
        S = np.log1p(S)
        S = (S - S.min()) / (S.max() - S.min() + 1e-8)
        S = (S * 255).astype(np.uint8)
        S = cv2.GaussianBlur(S, (5,5), 0)
        S = cv2.resize(S, (size,size))
        S = np.stack([S,S,S], axis=0).astype(np.float32) / 255.0
        return S
    except Exception:
        return np.zeros((3,size,size), dtype=np.float32)
