from flask import Blueprint, redirect
from database import db_session
from database import Config
from models import Urls

app_config = Config()

redirection = Blueprint("redirection", __name__)


@redirection.route("/<slug>")
def redirect_to(slug):
    shortened_url = app_config.get_base_url() + slug
    orginal_url = db_session.query(Urls).filter(
        Urls.link_created == shortened_url).first()
    print("=================================")
    print(orginal_url.target_url)
    print("================================")
    return redirect(orginal_url.target_url, code=302)
