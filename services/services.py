from flask import Flask, request, jsonify
from loko_extensions.business.decorators import extract_value_args
from loko_extensions.model.components import Component, save_extensions, Arg
from transformers import pipeline

from utils.cache import FSCache

app = Flask("")

c = Component("zs_classifier",
              args=[Arg(name="classes", value="positive, neutral, negative")])

save_extensions([c])

classifier = None


@FSCache("./zscache")
def classify(value, classes):
    return classifier(value, classes)


@app.route("/", methods=["POST"])
@extract_value_args(_request=request)
def test(value, args):
    global classifier
    classes = [x.strip() for x in args.get("classes", "positive, neutral, negative").split(",")]
    if classifier is None:
        classifier = pipeline("zero-shot-classification",
                              model="joeddav/xlm-roberta-large-xnli")
    return jsonify(classify(value=value, classes=classes))


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
