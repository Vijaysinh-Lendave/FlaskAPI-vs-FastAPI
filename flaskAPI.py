from flask import Flask


app = Flask(__name__)

@app.route("/")

def home():
    return "This blog is about FlastAPI and FastAPI"

if __name__ == "__main__":
    app.run(debug=True)