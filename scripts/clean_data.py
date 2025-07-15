import pandas as pd

# Load the file, skipping the first row which contains weird headers
df = pd.read_csv("data/raw/raw_operational_demand.csv", skiprows=1)

# Rename the columns manually
df.columns = [
    "region_id", "category", "type", "aemo_flag", "region_code",
    "interval_datetime", "demand_mw", "demand_adjustment", "wdr_estimate", "last_changed"
]

# Convert timestamps
df["interval_datetime"] = pd.to_datetime(df["interval_datetime"])
df["demand_mw"] = pd.to_numeric(df["demand_mw"], errors="coerce")

# Save cleaned file
df.to_csv("data/clean/clean_operational_demand.csv", index=False)
print("✅ Cleaned data saved.")
