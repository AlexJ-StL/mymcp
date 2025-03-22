from flask import Flask
from flask_cors import CORS
from api import api_bp

app = Flask(__name__)
CORS(app)
app.register_blueprint(api_bp)


@app.route("/")
def hello():
    return "Hello, Flask!"


if __name__ == "__main__":
    app.run(debug=True)
