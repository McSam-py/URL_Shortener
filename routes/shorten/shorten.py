from flask import Blueprint, request, jsonify, make_response, flash, render_template
from models import Urls
from database import db_session, Config
import uuid

shorten = Blueprint("shorten", __name__)
app_config = Config()


def create_link(url_db, slug_in_db):
    if slug_in_db:
        flash("Slug is not available!")
        return render_template("home.html")
    else:
        db_session.add(url_db)
        db_session.commit()


@shorten.route("/shorten", methods=["POST"])
def shorten_url():
    url = request.form["url"]
    slug = request.form["slug"]
    link_created = app_config.get_base_url() + slug
    user_id = request.form["user_id"]

    url_db = Urls(user_id, url, link_created)

    slug_in_db = db_session.query(Urls).filter(
        Urls.link_created == link_created).first()

    if user_id is None:
        create_link(url_db, slug_in_db)

    else:
        user_id = str(uuid.uuid4())
        create_link(url_db, slug_in_db)

    # print(f"{url}\n{shorten_url}\n{session['url']}")
    return make_response(jsonify({
        "link": f"{str(link_created)}",
        "user_id": f"{str(user_id)}",
    }), 201)
