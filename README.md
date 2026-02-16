# CAP5771-Milestone-1
Project Milestone One for Intro to Data Science

## Overview:
This project integrates U.S. air quality exposure data (EPA AQI) with weekly respiratory hospital admissions (CDC NHSN HRD) to support exploratory analysis of how air quality may relate to respiratory healthcare burden.

## Main Question:
How do weekly air quality conditions (AQI) relate to weekly respiratory-related hospital admissions (COVID-19, Influenza, RSV) across U.S. states from 2021–2025?

## Data Sources
- CDC NHSN HRD (Weekly Hospital Respiratory Data): downloaded via script.
- EPA AQS AirData (Daily AQI by county): downloaded via script (annual zip files).

## Repository Structure
- `Code Implementation/milestone_1_code.ipynb`: end-to-end Milestone 1 workflow (acquisition → processing → database → exploration)
- `diary/`: milestone documentation (5 stages)
- `data/raw/`: raw datasets (NOT committed; reproducible via scripts)
- `data/processed/`: processed tables + SQLite database (committed)
- `scripts/`: download + documentation artifact generators
- `database schema/schema.png`: database schema image
- `data dictionary/`: contains our data dictionary PDF

## Database File
There is already a generated .db file in the /data/processed folder!
You can find it there, or generate it yourself via the instructions below.

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

