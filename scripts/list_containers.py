import subprocess
def list_containers():
    result = subprocess.run(["docker", "ps", "--format", "{{.Names}}"], capture_output=True, text=True)
    return result.stdout.splitlines()
containers = list_containers()
for i in containers:
    print(f"Running container: {i}")
