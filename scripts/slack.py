import requests
import subprocess

def error_logs(container):
    result = subprocess.run(["docker", "logs", container], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    if not result.stdout:
        print("no logs captured!")
    for log in result.stdout.splitlines():
        if "ERROR" in log:
            print(f"error found:", log)

error_logs("silly_buck")


