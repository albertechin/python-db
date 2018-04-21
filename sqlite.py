import sqlite3

conn = sqlite3.connect("lite.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
cur.execute("INSERT INTO store VALUES('Akku',1,0.0)")
cur.execute("INSERT INTO store VALUES('Lalla',1,0.0)")
cur.execute("SELECT * FROM store")
rows = cur.fetchall()
print(rows)
print(rows[0][0])
conn.commit()
conn.close()
