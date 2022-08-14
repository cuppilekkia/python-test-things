import sqlite3


def build_table():
  conn=sqlite3.connect("lite.db")
  cur=conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
  conn.commit()
  conn.close()

def insert_row(item, quantity, price):
  conn=sqlite3.connect("lite.db")
  cur=conn.cursor()
  cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
  conn.commit()
  conn.close()

insert_row("Wine", 10, 5.5)

def view():
  conn=sqlite3.connect("lite.db")
  cur=conn.cursor()
  cur.execute("SELECT * FROM store")
  rows=cur.fetchall()
  conn.close()
  return rows

print(view())