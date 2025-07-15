import subprocess

def run_step(description, command):
    print(f"🚀 {description}...")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"❌ Error during: {description}")
        print(result.stderr)
        exit(1)
    print(f"✅ {description} complete.\n")

if __name__ == "__main__":
    # Step 1: Download latest NEM data
    run_step("Downloading NEM data", "python scripts/download_data.py")

    # Step 2: Clean and transform data
    run_step("Cleaning data", "python scripts/clean_data.py")

    # Step 3: Upload cleaned data to S3
    run_step("Uploading to S3", "python scripts/upload_to_s3.py")

    # Step 4: Copy data from S3 to Redshift
    run_step("Copying to Redshift", "python scripts/copy_to_redshift.py")

    # Step 5: Run Soda data quality checks
    run_step("Running Soda scan", "python scripts/run_soda_checks.py")
    
    # Final message
    print("🎉 Pipeline completed successfully!")