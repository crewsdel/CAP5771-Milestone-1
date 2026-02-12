# CAP5771-Milestone-1
Project Milestone One for Intro to Data Science

## Reproduce Everything Steps:
1. Install deps: pip install -r requirements.txt
2. Download raw data:
   - python scripts/download_cdc_hrd.py
   - python scripts/download_epa_aqi_daily.py
3. Run the notebook milestone_1_code.ipynb to generate
   - cdc_m1.csv
   - aqi_m1.csv
   - merged_m1.csv
   - milestone1.db

## Data Acquisition

EPA Daily AQI data can be downloaded from:
https://aqs.epa.gov/aqsweb/airdata/download_files.html

CDC Weekly Respiratory Data:
[https://data.cdc.gov/...](https://data.cdc.gov/Public-Health-Surveillance/Weekly-Hospital-Respiratory-Data-HRD-Metrics-by-Ju/ua7e-t2fy/about_data)

Raw files are not stored in this repository due to size constraints.

We have included scripts to download the raw data to their appropriate files (see "Reproduce Everything Steps" above).

