#!/usr/bin/env python3
import argparse
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.baseline import UserProfile
import numpy as np

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--user', required=True)
    ap.add_argument('--hr_json', required=True)
    args = ap.parse_args()
    with open(args.hr_json) as f:
        d = json.load(f)
    hr = d.get('hr_series', d)
    prof = UserProfile(args.user)
    prof.calibrate_from_series(hr)
    print('[CALIBRATE] Done')
    print('baseline_hr:', prof.baseline_hr)
    print('hr_thresh:', prof.hr_thresh)
    print('saved:', prof.path)

if __name__=='__main__':
    main()
