import logging

logger= logging.getLogger("app")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("app.log")
logger.addHandler(handler)

formatter= logging.Formatter("%(asctime)s - [%(levelname)s] - %(message)s")
handler.setFormatter(formatter)

logger.info("App started")
