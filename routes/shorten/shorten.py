from flask import Blueprint, request

shorten = Blueprint("shorten", __name__)


@shorten.route("/", method=["POST"])
def shorten_url():
    url = request.form["url"]
    shorten_url = request.form["shorten_url"]
    return "<h1>This is a url shortener</h1>"
