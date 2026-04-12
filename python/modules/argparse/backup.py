import subprocess
import argparse

parser = argparse.ArgumentParser(description="backup_script")

parser.add_argument("--source", required=True)
parser.add_argument("--dest", required=True)

args = parser.parse_args()

subprocess.run(["cp", "-r", args.source, args.dest], check=True)

print("Backup completed")

#run  python3 backup.py --source argparse.txt --dest /root/python/modules
