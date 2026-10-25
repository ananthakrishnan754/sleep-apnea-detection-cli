import numpy as np
import neurokit2 as nk

def extract_rr(ecg, sampling_rate=100):
    try:
        _, rpeaks = nk.ecg_peaks(ecg, sampling_rate=sampling_rate)
        peaks = rpeaks["ECG_R_Peaks"]
        if len(peaks) < 2:
            return np.array([])
        rr = np.diff(peaks) / sampling_rate * 1000.0  # ms
        # clean
        if len(rr) > 0:
            med = np.median(rr)
            rr = np.where(np.abs(rr-med) > 300, med, rr)
        return rr
    except Exception:
        return np.array([])
