from flask import Flask, Blueprints

app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
