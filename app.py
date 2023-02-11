from flask import Flask, render_template
from routes import shorten
from routes import redirect
from database import Config
from datetime import timedelta

app_config = Config()
app_config.set_app_config(
    db_url="sqlite:///database.sqlite3", base_url="https://127.0.0.1/")

app = Flask(__name__)
app.register_blueprint(shorten)
app.register_blueprint(redirect)

app.secret_key = "this_is_a_secret_key"
app.permanent_session_lifetime = timedelta(days=1)


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
