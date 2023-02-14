from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return app.static_url_path('index.html')