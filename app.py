from flask import Flask, render_template
from routes import shorten

app = Flask(__name__)
app.register_blueprint(shorten)


@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
