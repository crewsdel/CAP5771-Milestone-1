# Running this script downloads the CDC data

from pathlib import Path
import pandas as pd

# CDC HRD dataset
CDC_DATASET_ID = "ua7e-t2fy"
CDC_CSV_URL = f"https://data.cdc.gov/resource/{CDC_DATASET_ID}.csv"

def main():
    out_dir = Path("data/raw/CDC")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "cdc_raw.csv"

    print(f"Downloading CDC HRD to {out_path} ...")
    df = pd.read_csv(CDC_CSV_URL)
    df.to_csv(out_path, index=False)
    print("Done. Rows:", len(df), "Cols:", len(df.columns))

if __name__ == "__main__":
    main()
