import sqlite3
import os

book_database = []

def init_database():
    if os.path.exists("books.db") == False:
        con = sqlite3.connect('books.db')
        cur = con.cursor()

        cur.execute('''CREATE TABLE books (id text, title text, year text, description text)''')
        
        #cur.execute("INSERT INTO books VALUES ('1', 'The best book ever', '2014', 'The greatest description ever')")

        con.commit()
        con.close()

def load_database():
    if os.path.exists("books.db") == False:
        init_database()

    con = sqlite3.connect('books.db')
    cur = con.cursor()

    book_database = []
    for row in cur.execute('SELECT * FROM books'):
        print(row)
        book = {"id":"","title":"1", "year":"", "description":""}
        book["id"] = row[0]
        book['title'] = row[1]
        book['year'] = row[2]
        book['description'] = row[3]
        book_database.append(book)

    con.commit()
    con.close()
    return book_database

def add_to_database(id, title, year, description):
    if os.path.exists("books.db") == False:
        init_database()
    
    con = sqlite3.connect('books.db')
    cur = con.cursor()

    cur.execute("INSERT INTO books VALUES (?, ?, ?, ?)", (id, title, year, description))

    con.commit()
    con.close()