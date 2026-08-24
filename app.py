from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """<h1>Welcome to Flask API!</h1>
              <p>Visit <a href='/api/hello'>/api/hello</a> to see the hello message.</p>"""

@app.route("/api/hello")
def hello():
    return {
        "message": "<h1>Hello from Flask API!</h1> <a href='rgukt.ac.in'>RGUKT</a>",
        "status": "success"
    }

if __name__ == "__main__":
    app.run(debug=True)