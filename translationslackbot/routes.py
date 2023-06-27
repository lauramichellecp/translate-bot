from flask import Blueprint, jsonify

main = Blueprint("main", __name__)


@main.route("/test")
def test():
    return jsonify({"hello": "world"})
