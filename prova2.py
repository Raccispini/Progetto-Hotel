import sqlite3

con = sqlite3.connect('database.db')
query = 'select * from Bar GROUP BY Bar.categoria;'
cose = con.execute(query).fetchall()

for i in cose:
	print(i)