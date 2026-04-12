#task is to execute the ci pipeline

import subprocess

steps = [
        ["git", "pull"],
        ["docker", "build", "-t", "myapp", "."],
        ["docker", "stop", "myapp"],
        ["docker", "rm", "myapp"]
        ["docker", "run", "-d", "--name", "myapp", "-p", "80:80", "myapp"]
        ]
for step in steps:
    try:
        subprocess.run(step, check=True) #here check used to if any error occurs it stops, if u dont use check it ignores the error ans continue the next step
        print(f"success: {''.join(step)}")

    except subprocess.CalledProcessorError:
        print(f"failes: {''.join(step)}")
        break
