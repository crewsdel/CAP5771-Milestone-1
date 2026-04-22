# CAP5771-Milestone-3
Project Milestone Three for Intro to Data Science

## Overview:
This project integrates U.S. air quality exposure data (EPA AQI) with weekly respiratory hospital admissions (CDC NHSN HRD) to support exploratory analysis of how air quality may relate to respiratory healthcare burden. For Milestone 3, we decided to create and deploy a tool that predicts the number of respiratory-related hospitalizations based on daily AQI values entered by the user.

## Main Question:
How do weekly air quality conditions (AQI) relate to weekly respiratory-related hospital admissions (COVID-19, Influenza, RSV) across U.S. states from 2021–2025?

## Data Sources
- CDC NHSN HRD (Weekly Hospital Respiratory Data): downloaded via script.
- EPA AQS AirData (Daily AQI by county): downloaded via script (annual zip files).

## Repository Structure
- `Code Implementation/`:
    - `milestone_1_code.ipynb`:end-to-end Milestone 1 workflow (acquisition → processing → database → exploration)
    - `data_wrangling.ipynb`: full dataset cleaning, validating, and feature engineering
    - `data_modeling.ipynb`: regression model preprocessing, creation, and results comparisons
    - `data_visualization_static.ipynb`: dashboard visualizations that highlight key findings regarding the relationship between AQI and respiratory-related hospital admissions
- `Model Deployment/`:
    - `csv`: .csv files for the application
    - `models`: our saved models
    - `static`: images and styling for the tool
    - `templates`: HTML files for the structure of the web pages
    - `app.py`: Python file to generate and deploy the complete prediction tool
- `diary/`: milestone documentation
- `data/raw/`: raw datasets (NOT committed; reproducible via scripts)
- `data/processed/`: processed tables + SQLite database (committed)
- `scripts/`: download + documentation artifact generators
- `database schema/schema.png`: database schema image
- `data dictionary/`: contains our data dictionary PDF
- `videos`: two folders containing unlisted links to the Milestone 3 videos

## Database File
There is already a generated .db file in the /data/processed folder!
You can find it there, or generate it yourself via the instructions below.

## Reproduce Everything Steps:
1. Install deps: pip install -r requirements.txt
2. Download raw data:
   - python scripts/download_cdc_hrd.py
   - python scripts/download_epa_aqi_daily.py
3. (Milestone 1 outputs) Run the notebook milestone_1_code.ipynb to generate
   - cdc_m1.csv
   - aqi_m1.csv
   - merged_m1.csv
   - milestone1.db
4. (Milestone 2 outputs) Run the notebooks data_wrangling.ipynb, data_modeling.ipynb, and data_visualization_static to generate
   - modeling_dataset.csv
   - model_predictions.csv
   - feature_importance.csv
   - milestone2.db

## Run Dashboard Notebook (Milestone 2)
Follow the previously mentioned steps for reproducing the file. Once the necessary files have been created, run the data_visualization_static notebook to generate the interactive dashboard.

## Build and Deploy the Prediction Tool (Milestone 3)
To run the tool locally, follow the previously mentioned steps for reproducing the file. After the necessary files have been created, run the app.py file found in the Model Deployment folder. To get the LLM responses locally, ensure you have install the phi3 model on Ollama and have it running.  

Example setup:

Navigate to the model deployment folder.

In one terminal start the application by running:
```
python3 app.py
```

In another terminal run:
```
ollama run phi3
```

After running those commands the prediction tool should start running locally.

## Deployed Tool (Milestone 3)
The online deployed tool can be found at:  

https://respiratory-hospitalization-prediction-tool.up.railway.app/  

NOTE: Since Ollama is designed to run on local machines, it is not able to generate responses on the online version of the prediction tool. That said, all other application functionality is intact. To experience the prediction tool with LLM integration, please follow the previous steps to run the application locally.

## Deployment Videos (Milestone 3)
There are two files with links in the videos/ directory. One video walks through the code implementation of our tool, and the other is a demo of the tool. To watch, simply copy and paste the links into your preferred browser.

## Data Acquisition
EPA Daily AQI data can be downloaded from:
https://aqs.epa.gov/aqsweb/airdata/download_files.html

CDC Weekly Respiratory Data:
[https://data.cdc.gov/...](https://data.cdc.gov/Public-Health-Surveillance/Weekly-Hospital-Respiratory-Data-HRD-Metrics-by-Ju/ua7e-t2fy/about_data)

Raw files are not stored in this repository due to size constraints.

We have included scripts to download the raw data to their appropriate files (see "Reproduce Everything Steps" above).

