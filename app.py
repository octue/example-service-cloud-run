import time


def run(analysis):
    analysis.logger.info("Started example analysis.")
    time.sleep(10)
    analysis.output_values = [1, 2, 3, 4, 5]
    analysis.logger.info("Finished example analysis.")
