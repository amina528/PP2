import psycopg2

conn = psycopg2.connect("dbname=phonebook user=postgres password=твой_пароль")
cur = conn.cursor()

# Query
cur.execute("SELECT * FROM contacts")
for row in cur.fetchall():
    print(row)

# Delete
cur.execute("DELETE FROM contacts WHERE name=%s", ("Bob",))
conn.commit()

cur.close()
conn.close()
print("Query and delete done")