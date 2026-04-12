import subprocess

def prune():
    print("Remove unused stuff")
    result = subprocess.run(["docker", "system", "prune", "-a"])
def pull_images(image):
    print(f"pulling {image}..")
    result = subprocess.run(["docker", "pull", image], capture_output=True, text=True)
def run_containers(image):
    print(f"{image} is running..")
    result = subprocess.run(["docker", "run", image], capture_output=True, text=True)
def list():
    result =subprocess.run(["docker", "ps"])
prune()
pull_images("nginx")
run_containers("redis")
ls = list()
for i in ls:
    print(i)
