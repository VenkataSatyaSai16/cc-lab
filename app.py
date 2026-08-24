from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """<h1>Welcome to Flask API!</h1>
              <a href='https://rgukt.ac.in'>RGUKT</a>"""

@app.route("/api/hello")
def hello():
    return {
        "message": "<h1>Hello from Flask API!</h1> <a href='https://rgukt.ac.in'>RGUKT</a>",
        "status": "success"
    }

if __name__ == "__main__":
    app.run(debug=True)