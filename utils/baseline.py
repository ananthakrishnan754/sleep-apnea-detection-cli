import json
import os
import numpy as np

class UserProfile:
    def __init__(self, user_id):
        self.user_id = user_id
        self.calibrated = False
        self.baseline_hr = None
        self.hr_thresh = None
        self.hr_series = []
        self.path = f'data/user_profiles/{user_id}.json'

    def calibrate_from_series(self, hr_series):
        self.hr_series = list(hr_series)
        self.baseline_hr = float(np.mean(hr_series))
        self.hr_thresh = self.baseline_hr + 10.0
        self.calibrated = True
        self.save()

    def save(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path,'w') as f:
            json.dump({
                'user_id': self.user_id,
                'baseline_hr': self.baseline_hr,
                'hr_thresh': self.hr_thresh,
                'calibrated': self.calibrated,
                'count': len(self.hr_series)
            }, f, indent=2)

    def load(self):
        if os.path.exists(self.path):
            with open(self.path) as f:
                d = json.load(f)
            self.baseline_hr = d['baseline_hr']
            self.hr_thresh = d['hr_thresh']
            self.calibrated = d['calibrated']
            return True
        return False
