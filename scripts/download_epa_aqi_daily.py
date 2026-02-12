from pathlib import Path
import zipfile
import urllib.request

BASE = "https://aqs.epa.gov/aqsweb/airdata/"
OUT_DIR = Path("data/raw/AQI")

def download_year(year: int):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    zip_name = f"daily_aqi_by_county_{year}.zip"
    zip_path = OUT_DIR / zip_name
    url = BASE + zip_name

    if zip_path.exists():
        print(f" Already downloaded: {zip_path}")
    else:
        print(f" Downloading: {url} -> {zip_path}")
        urllib.request.urlretrieve(url, zip_path)

    # unzip into the same folder (keep raw data local)
    print(f"Unzipping {zip_path} ...")
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(OUT_DIR)
    print(f"Done year {year}")

def main():
    for y in range(2021, 2026):
        download_year(y)

if __name__ == "__main__":
    main()

