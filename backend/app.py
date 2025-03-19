from flask import Flask
from .api import api_bp

app = Flask(__name__)
app.register_blueprint(api_bp)


@app.route("/")
def hello():
    return "Hello, Flask!"


if __name__ == "__main__":
    app.run(debug=True)
