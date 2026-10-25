#!/usr/bin/env python3
import os
import wfdb

outdir = 'data/raw/apnea-ecg'
os.makedirs(outdir, exist_ok=True)
try:
    wfdb.dl_database('apnea-ecg', dl_dir=outdir, records='all')
    print('[OK] Downloaded')
except Exception as e:
    print('[ERR]', e)
    print('Manual: https://physionet.org/content/apnea-ecg/1.0.0/')
