from flask import Flask
from flask_cors import CORS
from api import api_bp

app = Flask(__name__)
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "http://localhost:3000",  # Create React App
            "http://localhost:5173",  # Vite dev server
            "http://localhost:4173"   # Vite preview server
        ],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})
app.register_blueprint(api_bp, url_prefix='/api')

@app.route("/")
def hello():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
