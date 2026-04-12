import logging

logging.basicConfig(                                # It configures how logging behaves globally
                    level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s"
                    )
logging.debug("debug info")
logging.info("app started")
logging.warning("Disk almost full")
logging.error("service failed")
