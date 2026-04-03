from connect import connect
import csv

# Создание таблицы
def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20)
    )
    """)

    conn.commit()
    cur.close()
    conn.close()


# Добавление одного контакта
def insert_contact(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()


# Добавление нескольких контактов за раз
def insert_multiple_contacts(contacts):
    conn = connect()
    cur = conn.cursor()
    for name, phone in contacts:
        cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()


# Чтение всех контактов
def get_contacts():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


# Обновление контакта
def update_contact(name, new_phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE contacts SET phone=%s WHERE name=%s", (new_phone, name))
    conn.commit()
    cur.close()
    conn.close()


# Удаление контакта
def delete_contact(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE name=%s", (name,))
    conn.commit()
    cur.close()
    conn.close()


# Импорт из CSV
def import_from_csv():
    conn = connect()
    cur = conn.cursor()
    with open("contacts.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # пропускаем заголовок
        for row in reader:
            cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    cur.close()
    conn.close()


# Меню
def menu():
    create_table()
    while True:
        print("\n1. Add contact(s)")
        print("2. Show contacts")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Import from CSV")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            contacts = []
            while True:
                name = input("Name (или 'stop' для выхода): ")
                if name.lower() == "stop":
                    break
                phone = input("Phone: ")
                contacts.append((name, phone))
            insert_multiple_contacts(contacts)

        elif choice == "2":
            get_contacts()

        elif choice == "3":
            name = input("Name: ")
            phone = input("New phone: ")
            update_contact(name, phone)

        elif choice == "4":
            name = input("Name: ")
            delete_contact(name)

        elif choice == "5":
            import_from_csv()

        elif choice == "0":
            break


if __name__ == "__main__":
    menu()