import subprocess
def multiple_containers(*images):
    for image in images:
        print(f"deploying {image}...")
        result = subprocess.run(["docker", "run", image])

multiple_containers("postgres", "mysql", "prometheus")
