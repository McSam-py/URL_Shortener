from flask import redirect, Blueprint

redirect = Blueprint("redirect", __name__)


@redirect.route("/<slug>")
def redirect(slug):
    pass
