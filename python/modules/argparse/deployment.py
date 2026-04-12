import subprocess
import argparse

parser = argparse.ArgumentParser(description="deploy the app")
parser.add_argument("--env", required=True, choices=["prod", "dev"])
parser.add_argument("--version", required=True)

args = parser.parse_args()

print(f"Deployment version {args.version} to {args.env}")

if args.env == "prod":
    subprocess.run(["echo", "deploy to PROD"], check=True)

else:
    subprocess.run(["echo", "deploy to DEV"], check=True)
