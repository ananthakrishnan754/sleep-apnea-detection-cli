#!/usr/bin/env python3
import argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--epochs', type=int, default=10)
    ap.add_argument('--device', default='cpu')
    ap.add_argument('--variant', default='v1_dual')
    args = ap.parse_args()
    print('[TRAIN] Starting', args)
    print('[TRAIN] Order: spectro-only -> rr-only -> dual-view -> fusion+spo2')
    print('[TRAIN] Using inter-patient split from configs/config.yaml')

if __name__=='__main__':
    main()
