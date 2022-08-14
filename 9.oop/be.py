import sqlite3

DB="bookstore"

class Bookstore:
  def __init__(self, file):
    self.conn=sqlite3.connect(file)
    self.cur=self.conn.cursor()
    self.cur.execute("CREATE TABLE IF NOT EXISTS %s (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)" % DB)
    self.conn.commit()

  def insert(self, title, author, year, isbn):
    self.cur.execute("INSERT INTO %s VALUES (NULL,?,?,?,?)" % DB, (title,author, year, isbn))
    self.conn.commit()

  def delete(self, id):
    self.cur.execute("DELETE FROM %s WHERE id=?" % DB, (id))
    self.conn.commit()

  def search(self, title="", author="", year="", isbn=""):
    self.cur.execute("SELECT * FROM %s WHERE title=? OR author=? OR year=? OR isbn=?" % DB, (title,author,year,isbn))
    rows=self.cur.fetchall()
    return rows

  def update(self, id, title, author, year, isbn):
    self.cur.execute("UPDATE %s SET title=?, author=?, year=?, isbn=? WHERE id=?" % DB, (title,author,year,isbn,id))
    self.conn.commit()

  def view(self):
    self.cur.execute("SELECT * FROM %s" % DB)
    rows=self.cur.fetchall()
    return rows

  def __del__(self):
    print("closing DB")
    self.conn.close()