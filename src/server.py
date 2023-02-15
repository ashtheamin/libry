from flask import Flask, jsonify, request

from database import load_database, add_to_database

app = Flask(__name__, static_url_path=("/static"))
@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/books")
def books():
    return "<p>Book List</p>"

@app.route("/users")
def users():
    return "<p>Users</p>"

@app.route("/bookdb")
def bookdb():
    book_database = load_database()
    return jsonify(book_database)

@app.route("/recievedata", methods=["POST"])
def recievedata():
    print(request.get_json())
    return jsonify("Data Recieved")

@app.route("/admin")
def admin():
    return app.send_static_file("admin.html")

@app.route("/addbook", methods=["POST"])
def addbook():
    book_database = load_database()
    print(book_database)
    id = "0"
    if len(book_database) < 1:
           id = "0"
    else:
        for book in book_database:
            if book['id'] >= id:
                id = book['id']
        id = str(int(id) + 1)

    add_to_database(id , request.form["title"], request.form["year"], request.form["description"])
    return app.send_static_file("admin.html")