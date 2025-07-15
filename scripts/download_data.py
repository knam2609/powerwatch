import requests
from bs4 import BeautifulSoup
import zipfile
import io
import os
from urllib.parse import urljoin

# Step 1: Define source URL
URL = "https://nemweb.com.au/Reports/Current/Operational_Demand/ACTUAL_5MIN/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Find the latest .zip file
links = [a["href"] for a in soup.find_all("a", href=True) if a["href"].endswith(".zip")]
links.sort(reverse=True)  # most recent first
latest_zip_url = urljoin(URL, links[0])
print(f"📦 Downloading: {latest_zip_url}")

# Step 3: Download and extract the single CSV
r = requests.get(latest_zip_url)
z = zipfile.ZipFile(io.BytesIO(r.content))

# Ensure output folder exists
os.makedirs("data/raw", exist_ok=True)
# Extract the only CSV and rename it
for file in z.namelist():
    if file.endswith(".CSV"):
        with z.open(file) as extracted:
            target_path = os.path.join("data/raw", "raw_operational_demand.csv")
            with open(target_path, "wb") as f_out:
                f_out.write(extracted.read())
        print(f"✅ Saved as: {target_path}")
        break