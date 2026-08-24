from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask!"

@app.route("/api/hello")
def hello():
    return {
        "message": "Hello from Flask API",
        "status": "success"
    }

if __name__ == "__main__":
    app.run(debug=True)