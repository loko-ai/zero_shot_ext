from loguru import logger
from werkzeug.exceptions import HTTPException

from config.app_config import HF_TOKEN, HF_MODEL
from doc.doc import zeroshot_doc
from flask import Flask, request, jsonify
from loko_extensions.business.decorators import extract_value_args
from loko_extensions.model.components import Component, save_extensions, Arg
from transformers import pipeline

from utils.cache import FSCache

app = Flask("")

c = Component("ZeroShot CLF", icon="RiRadioButtonFill",
              description=zeroshot_doc,
              args=[Arg(name="classes", value="positive, neutral, negative")])

save_extensions([c])

classifier = None


@FSCache("./zscache")
def classify(value, classes):
    return classifier(value, classes)


@app.errorhandler(Exception)
def handle_exception(exception):

    if isinstance(exception, HTTPException):
        logger.error(exception)
        return exception

    e = str(exception)
    j = dict(error=e)
    status_code = getattr(exception, "code", None) or 500
    logger.exception(e)

    return jsonify(j), status_code


@app.route("/", methods=["POST"])
@extract_value_args(_request=request)
def test(value, args):
    global classifier
    classes = [x.strip() for x in args.get("classes", "positive, neutral, negative").split(",")]
    if classifier is None:
        classifier = pipeline("zero-shot-classification",
                              model=HF_MODEL,
                              use_auth_token=HF_TOKEN)
    return jsonify(classify(value=value, classes=classes))


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
