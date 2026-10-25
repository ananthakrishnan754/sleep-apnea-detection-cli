import numpy as np
import pandas as pd

class WatchSim:
    def __init__(self, seed=42):
        np.random.seed(seed)

    def degrade_from_ecg_rr(self, rr_list):
        # simulate watch HR/RR with dropouts
        rr = np.array(rr_list, dtype=float)
        # irregular sampling
        mask = np.random.rand(len(rr)) > 0.05
        rr_w = rr.copy()
        rr_w[~mask] = np.nan
        # simple impute
        s = pd.Series(rr_w)
        s = s.interpolate(limit_direction='both')
        rr_w = s.values
        # add noise
        rr_w = rr_w + np.random.normal(0, 5, len(rr_w))
        return rr_w

    def make_spo2(self, apnea_mask_1min=None, length=60):
        # create plausible desat curve (demo only)
        spo2 = np.ones(length)*96.5 + np.random.normal(0,0.2,length)
        if apnea_mask_1min is not None and apnea_mask_1min > 0.5:
            # drop
            t = np.linspace(-8,-15,15)
            spo2[20:35] += t
        spo2 = np.clip(spo2,88,99)
        return spo2
