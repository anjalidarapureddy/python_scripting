import subprocess
def build_image(image_name):
    print(f"Building {image_name}")
    result = subprocess.run(["docker", "build", "-t", image_name, "."])
def run_cont(image_name):
    print(f"{image_name} is running")
    result = subprocess.run(["docker", "run", "-d", "--name", "myapp", image_name])

build_image("web1")
run_cont("web1")
