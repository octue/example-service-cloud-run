import logging
import time


logger = logging.getLogger(__name__)


def run(analysis):
    logger.info("Started example analysis.")
    time.sleep(5)
    analysis.output_values = [1, 2, 3, 4, 5]
    logger.info("Finished example analysis.")
