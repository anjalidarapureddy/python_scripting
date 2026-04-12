import logging
import subprocess
from logging.handlers import RotatingFileHandler

#-----------------------
#loggersetup
#----------------------------
def logger():
    logger = logging.getLogger("deloy")
    logger.setLevel(logging.INFO)

    #formatter
    formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - %(message)s ")
   

    #handler
    file_handler = RotatingFileHandler(
            "prod_deploy.log",
            maxBytes = 5 * 1024 * 1024, #5MB
            backupCount =3
            )
    file_handler.setFormatter(formatter)

    #consle handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # attach handler
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
logger = logger()

#----------------------------------
#deplotment
#-------------------------------------------------
commands = [ ["docker", "pull", "mysql"],
            ["docker", "run", "-d", "--name", "mydb", "-p", "3306:3306", "mysql"]
            ]

for cmd in commands:
    try:
        logger.info(f"Running: {''.join(cmd)}")
        result = subprocess.run(cmd, stdout= subprocess.PIPE, stderr= subprocess.STDOUT, text=True, check=True)
        logger.info(result.stdout.strip())
        logger.info("step completed successfully")
    except subprocess.CalledProcessError:
        logger.exception(f"Failed command: {''.join(cmd)}")
        break
