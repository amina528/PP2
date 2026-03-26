import psycopg2

conn = psycopg2.connect("dbname=phonebook user=postgres password=твой_пароль")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    phone VARCHAR(20)
)
""")

conn.commit()
cur.close()
conn.close()
print("Table created")