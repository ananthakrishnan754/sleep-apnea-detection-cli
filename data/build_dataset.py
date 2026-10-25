#!/usr/bin/env python3
import os
import json
import numpy as np
from collections import defaultdict

# Patient-wise split as per project spec
SPLIT = {
  "train": ["a01","a02","a03","a04","a05","a06","a07","a08","a09","a10","b01","b02","b03","c01","c02","c03","c04","c05"],
  "val": ["a11","a12","a13","a14","a15","b04","c06","c07"],
  "test": ["a16","a17","a18","a19","a20","b05","c08","c09","c10"] + [f"x{i:02d}" for i in range(1,36)]
}

def get_patient(rec):
    return ''.join([c for c in rec if not c.isdigit()]) + rec.rstrip('0123456789')[-2:] if False else rec[:3] if rec[1].isdigit() else rec[:2]
# simpler
def get_pid(rec):
    # a01 -> a, b01 -> b, c01 -> c, x01 -> x
    for c in rec:
        if c.isalpha(): return c
    return rec[0]

def main():
    out = 'splits.json'
    manifest = {'train':[], 'val':[], 'test':[]}
    for k,v in SPLIT.items():
        for r in v:
            manifest[k].append(r)
    # check disjoint
    allr = set(manifest['train']) | set(manifest['val']) | set(manifest['test'])
    assert len(allr) == len(manifest['train']) + len(manifest['val']) + len(manifest['test'])
    with open(out,'w') as f:
        json.dump(manifest,f,indent=2)
    print('[OK] splits.json created')
    print('train:',len(manifest['train']),'val:',len(manifest['val']),'test:',len(manifest['test']))
    # save report
    os.makedirs('reports',exist_ok=True)
    with open('reports/split_report.txt','w') as f:
        f.write(json.dumps(manifest,indent=2))
    print('[OK] reports/split_report.txt')

if __name__=='__main__':
    main()
