import psycopg2

conn = psycopg2.connect("dbname=phonebook user=postgres password=твой_пароль")
cur = conn.cursor()

cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", ("Alice", "12345"))
cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", ("Bob", "67890"))

conn.commit()
cur.close()
conn.close()
print("Data inserted")