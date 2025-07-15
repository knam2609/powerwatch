# ⚡ Powerwatch: Automated NEM Demand Monitoring Pipeline

Powerwatch is an automated data pipeline that:
- Downloads 5-minute operational demand data from AEMO's NEMWeb
- Cleans and processes the data
- Uploads it to AWS S3
- Loads it into Amazon Redshift
- Runs automated data quality checks using Soda Cloud

## 📦 Features

- 🔄 End-to-end automation with a single script (`run_pipeline.py`)
- ☁️ Cloud-native stack: AWS S3 + Redshift + Soda Cloud
- ✅ Data quality checks with alerts and monitoring
- 🛠 Modular scripts for each pipeline stage

---

## 🗂 Repo Structure

```
powerwatch/
├── environment.yml            # Conda environment definition
├── run_pipeline.py            # Master script to run the entire pipeline
├── scripts/                   # Individual pipeline stages
│   ├── download_data.py
│   ├── clean_data.py
│   ├── upload_to_s3.py
│   ├── copy_to_redshift.py
│   └── run_soda_checks.py
├── soda/                      # Soda configuration
│   ├── soda_cloud.yml
│   ├── warehouse.yml
│   └── soda_checks.yml
└── data/                      # Raw and intermediate data files
```

---

## 🚀 How to Run It

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/powerwatch.git
cd powerwatch
```

### 2. Set Up Environment

```bash
conda env create -f environment.yml
conda activate soda310
```

### 3. Configure Secrets

Edit your `soda/soda_cloud.yml` and scripts to add:
- ✅ Soda API key
- ✅ AWS credentials
- ✅ Redshift IAM role and cluster details

### 4. Run the Pipeline

```bash
python run_pipeline.py
```

---

## 📊 Soda Cloud

Your data is validated with [Soda Cloud](https://beta.soda.io), which shows:
- Row counts
- Missing values
- Failed thresholds
- Anomaly flags

---

## 📌 Requirements

- Python 3.10
- AWS account with:
  - S3 bucket
  - Redshift Serverless
  - IAM role for COPY
- Soda Cloud account

---

Made by Nam Nguyen | 2025
