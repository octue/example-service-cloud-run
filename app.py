import logging
import tempfile
import time

from octue.resources import Datafile, Dataset

from example_package.submodule import do_something


logger = logging.getLogger(__name__)


def run(analysis):
    logger.info("Started example analysis.")
    do_something()
    time.sleep(5)
    analysis.output_values = [1, 2, 3, 4, 5]

    with tempfile.NamedTemporaryFile() as temporary_file:
        with Datafile(temporary_file.name, mode="w") as (datafile, f):
            f.write("This is some example service output.")

        analysis.output_manifest.datasets["example_dataset"] = Dataset(files=[datafile])
        analysis.finalise(upload_output_datasets_to="gs://octue-test-bucket/example_output_datasets")

    logger.info("Finished example analysis.")
