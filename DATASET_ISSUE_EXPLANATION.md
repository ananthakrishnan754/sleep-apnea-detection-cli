# Dataset Download Issue Explanation

## Summary
The PhysioNet Apnea-ECG dataset (v1.0.0) download is encountering issues, but the project pipeline is fully built and functional with available data.

## What Was Attempted
1. **Direct download from physionet.org** - Used wget, curl, aria2c with various approaches
2. **wfdb Python library** - `wfdb.dl_database()` and `wfdb.dl_files()` methods
3. **Archive extraction** - Downloaded zip/tar files from PhysioNet mirrors
4. **Alternative sources** - Tried Kaggle, GitHub mirrors (no luck due to auth/availability)

## Current State
- **Downloaded files**: 13 .hea, 13 .dat, 11 .apn files (~37 MB)
- **Fully readable records**: 6 records (a05, a06, a07, a08, a09, a10) with all three file types
- **Expected**: 86 records totaling ~580 MB per project specifications
- **Location**: `/home/ananthakrishnan/sleep_apnea_proto/data/raw/apnea-ecg/`

## Root Cause
The downloaded files appear corrupted or incomplete - wfdb cannot read them properly ("Samples were not loaded correctly"). This may be due to:
- Incomplete downloads due to network issues
- File format/version mismatches
- Need for specific file sets (some records need .qrs, .xws files)

## Impact
- Model trained on available data (6 readable records)
- All code, preprocessing, models, backend API, CLI demo, Flutter UI are complete and functional
- System works end-to-end with placeholder/simulated data
- Ready to retrain once complete dataset is obtained

## Solution
The complete dataset needs to be properly downloaded. The official source is https://physionet.org/content/apnea-ecg/1.0.0/ - may require proper authentication or different download method.
