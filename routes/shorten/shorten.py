from flask import Blueprint, request, session, jsonify, make_response
from models import Urls
from database import db_session
import uuid

shorten = Blueprint("shorten", __name__)


@shorten.route("/shorten", methods=["POST"])
def shorten_url():
    url = request.form["url"]
    slug = request.form["slug"]
    link_created = "https://127.0.0.1/" + slug
    user_id = str(uuid.uuid4())

    url = Urls(user_id, url, link_created)
    if "url" in session:
        print("user already has a session")
        db_session.add(url)
        db_session.commit()
        pass
    else:
        session.permanent = True
        session["url"] = url
        db_session.add(url)
        db_session.commit()

    # print(f"{url}\n{shorten_url}\n{session['url']}")
    return make_response(jsonify({
        "link": f"{link_created}",
    }), 201)
