import boto3 # type: ignore
from dotenv import load_dotenv # type: ignore
import os
load_dotenv()

session = boto3.Session(profile_name="powerwatch")
s3 = session.client("s3")

# Define local path and S3 target
local_file = 'data/clean/clean_operational_demand.csv'
bucket_name = os.getenv("S3_BUCKET")
s3_key = os.getenv("S3_KEY")

# Upload the file
s3.upload_file(local_file, bucket_name, s3_key)
print("✅ File uploaded to S3 successfully!")
