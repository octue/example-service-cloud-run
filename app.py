import time

from example_package.submodule import do_something


def run(analysis):
    analysis.logger.info("Started example analysis.")
    do_something()
    time.sleep(5)
    analysis.output_values = [1, 2, 3, 4, 5]
    analysis.logger.info("Finished example analysis.")
