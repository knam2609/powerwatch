import pg8000.native # type: ignore
from dotenv import load_dotenv # type: ignore
import os
load_dotenv()

# Redshift credentials
REDSHIFT_USER = os.getenv("REDSHIFT_USER")
REDSHIFT_PASSWORD = os.getenv("REDSHIFT_PASSWORD")
REDSHIFT_HOST = os.getenv("REDSHIFT_HOST")
REDSHIFT_PORT = os.getenv("REDSHIFT_PORT")
REDSHIFT_DB = os.getenv("REDSHIFT_DB")

# S3 and IAM role
S3_BUCKET = os.getenv("S3_BUCKET")
S3_KEY = os.getenv("S3_KEY")
S3_PATH = f"s3://{S3_BUCKET}/{S3_KEY}"
IAM_ROLE_ARN = os.getenv("REDSHIFT_IAM_ROLE_ARN")

# Redshift COPY command
copy_sql = f"""
    COPY public.operational_demand
    FROM '{S3_PATH}'
    IAM_ROLE '{IAM_ROLE_ARN}'
    FORMAT AS CSV
    IGNOREHEADER 1
    TIMEFORMAT 'auto'
    EMPTYASNULL
    BLANKSASNULL
    TRUNCATECOLUMNS;
"""

try:
    print("🔗 Connecting to Redshift via pg8000...")
    conn = pg8000.native.Connection(
        user=REDSHIFT_USER,
        password=REDSHIFT_PASSWORD,
        host=REDSHIFT_HOST,
        port=REDSHIFT_PORT,
        database=REDSHIFT_DB,
        timeout=15
    )

    print("🚀 Running COPY command...")
    conn.run(copy_sql)
    print("✅ Data copied to Redshift successfully.")
    conn.close()

except Exception as e:
    print("❌ Error:", e)