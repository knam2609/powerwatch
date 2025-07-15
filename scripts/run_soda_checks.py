import subprocess

def run_soda_scan():
    print("🚀 Running Soda scan...")

    try:
        result = subprocess.run([
            "soda", "scan",
            "-d", "powerwatch_redshift",
            "-c", "soda/warehouse.yml",
            "-c", "soda/soda_cloud.yml",
            "soda/soda_checks.yml"
        ], capture_output=True, text=True)

        print(result.stdout)

        if result.returncode == 0:
            print("✅ Soda scan completed successfully.")
        else:
            print("❌ Soda scan completed with issues.")
            print(result.stderr)

    except Exception as e:
        print("❌ Failed to run Soda scan:", e)

if __name__ == "__main__":
    run_soda_scan()