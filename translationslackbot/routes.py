from flask import Blueprint, jsonify
from googletrans import Translator

main = Blueprint("main", __name__)


@main.route("/test")
def test():
    return jsonify({"hello": "world"})


@main.route("/translate/<text>")
def translate_text(text):
    translator = Translator()
    result = translator.translate(text, src="sr", dest="en")
    return result.text
