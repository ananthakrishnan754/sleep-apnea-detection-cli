import numpy as np
from scipy.signal import butter, filtfilt

def bandpass(ecg, fs=100, low=0.5, high=40, order=4):
    b,a = butter(order, [low/(fs/2), high/(fs/2)], btype='band')
    return filtfilt(b,a, ecg)
