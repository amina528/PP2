import psycopg2

conn = psycopg2.connect("dbname=phonebook user=postgres password=твой_пароль")
cur = conn.cursor()

cur.execute("UPDATE contacts SET phone=%s WHERE name=%s", ("54321", "Alice"))

conn.commit()
cur.close()
conn.close()
print("Data updated")