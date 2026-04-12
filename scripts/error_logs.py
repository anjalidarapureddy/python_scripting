import subprocess
result = subprocess.run(["docker", "logs", "silly_buck"], capture_output=True, text=True)
logs = result.stderr.splitlines()
for log in logs:
    if "ERROR" in log:
        print(f"Error found {log}")
