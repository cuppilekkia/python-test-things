import sqlite3

DB="bookstore"

def connect():
  conn=sqlite3.connect("books.db")
  cur=conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS %s (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)" % DB)
  conn.commit()
  conn.close()

def insert(title, author, year, isbn):
  conn=sqlite3.connect("books.db")
  cur=conn.cursor()
  cur.execute("INSERT INTO %s VALUES (NULL,?,?,?,?)" % DB, (title,author, year, isbn))
  conn.commit()
  conn.close()

def delete(id):
  conn=sqlite3.connect("books.db")
  cur=conn.cursor()
  cur.execute("DELETE FROM %s WHERE id=?" % DB, (id))
  conn.commit()
  conn.close()

def search(title="", author="", year="", isbn=""):
  conn=sqlite3.connect("books.db")
  cur=conn.cursor()
  cur.execute("SELECT * FROM %s WHERE title=? OR author=? OR year=? OR isbn=?" % DB, (title,author,year,isbn))
  rows=cur.fetchall()
  conn.close()
  return rows

def update(id, title, author, year, isbn):
  conn=sqlite3.connect("books.db")
  cur=conn.cursor()
  cur.execute("UPDATE %s SET title=?, author=?, year=?, isbn=? WHERE id=?" % DB, (title,author,year,isbn,id))
  conn.commit()
  conn.close()

def view():
  conn=sqlite3.connect("books.db")
  cur=conn.cursor()
  cur.execute("SELECT * FROM %s" % DB)
  rows=cur.fetchall()
  conn.close()
  return rows

connect()
#insert("b", "b", 2020, 112233)
#print(search(title="a"))
#delete("3")
#update(2,"d","a",3434,22)
print(view())