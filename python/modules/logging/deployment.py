import logging
import subprocess

commands = [
        ["docker", "pull", "nginx"],
        ["docker", "run", "-d", "--name", "myapp", "-p", "80:80", "nginx"]
        ]
logging.basicConfig(
        filename="deploy.log",
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(message)s"
        )
for cmd in commands:
    try:
        logging.info(f"Running: {''.join(cmd)}")
        subprocess.run(cmd, check=True)
        logging.info("success")
    except subprocess.CalledProcessError:
        logging.error(f"Failed: {''.join(cmd)}")
        break
