from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<b>Hello!</b>"

if __name__ == "__main__":
    from waitress import serve
    serve(app, port=8080)