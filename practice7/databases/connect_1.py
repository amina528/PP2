import psycopg2

try:
    conn = psycopg2.connect(
        dbname="phonebook",
        user="postgres",
        password="твой_пароль",
        host="localhost"
    )
    print("Connected to PostgreSQL")
except Exception as e:
    print("Error:", e)
finally:
    if 'conn' in locals():
        conn.close()