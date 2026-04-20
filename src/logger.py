import logging

logging.basicConfig(
        filename="logs/pipeline.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
        )

def log(msg):
    logging.info(msg)

#logging.info("Im Neha")
