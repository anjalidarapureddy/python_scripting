#store logs in a file
import logging

logging.basicConfig(
        filename="app.log",   # logs store ina file without it displays in a terminal
        level=logging.INFO,
        format="%(asctime)s, [%(levelname)s], %(message)s"
        )
logging.info("application started")
logging.error("something is failed")
