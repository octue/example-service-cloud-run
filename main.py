import base64
import json
import os
import logging

from octue.resources.communication.google_pub_sub.service import Service
from octue.resources.communication.service_backends import GCPPubSubBackend
from octue.runner import Runner

from flask import Flask, request

logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    envelope = request.get_json()
    if not envelope:
        message = "No Pub/Sub message received."
        print(f"Error: {message}")
        return f"Bad Request: {message}", 400

    if not isinstance(envelope, dict) or "message" not in envelope:
        message = "Invalid Pub/Sub message format."
        print(f"error: {message}")
        return f"Bad Request: {message}", 400

    pubsub_message = envelope["message"]

    if isinstance(pubsub_message, dict):
        logger.info(pubsub_message)
        logger.info(base64.b64decode(pubsub_message["data"]).decode("utf-8").strip())
        data = json.loads(base64.b64decode(pubsub_message["data"]).decode("utf-8").strip())
        logger.info(data)
        logger.info(type(data))
        question_uuid = pubsub_message["attributes"]["question_uuid"]
        run_analysis(data, question_uuid)
        return ("", 204)


def run_analysis(data, question_uuid, deployment_configuration_path=None):
    """Run an analysis on the given data using the app with the deployment configuration.

    :param dict event: Google Cloud event
    :param google.cloud.functions.Context context: metadata for the event
    :return None:
    """
    print(dict(os.environ))

    with open(deployment_configuration_path or "deployment_configuration.json") as f:
        deployment_configuration = json.load(f)

    runner = Runner(
        app_src=".",
        twine=deployment_configuration.get("twine", "twine.json"),
        configuration_values=deployment_configuration.get("configuration_values", None),
        configuration_manifest=deployment_configuration.get("configuration_manifest", None),
        output_manifest_path=deployment_configuration.get("output_manifest", None),
        children=deployment_configuration.get("children", None),
        skip_checks=deployment_configuration.get("skip_checks", False),
        log_level=deployment_configuration.get("log_level", "INFO"),
        handler=deployment_configuration.get("log_handler", None),
        show_twined_logs=deployment_configuration.get("show_twined_logs", False),
    )

    service = Service(
        id=os.environ["SERVICE_ID"],
        backend=GCPPubSubBackend(project_name=os.environ["PROJECT_ID"], credentials_environment_variable=None),
        run_function=runner.run,
    )

    service.answer(data=data, question_uuid=question_uuid)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
