from flask import Flask, render_template
from routes import shorten
from routes import redirection
# from database import Config
from datetime import timedelta

app = Flask(__name__)
app.register_blueprint(shorten, url_prefix='/link')
app.register_blueprint(redirection)

app.secret_key = "this_is_a_secret_key"
app.permanent_session_lifetime = timedelta(days=1)


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
