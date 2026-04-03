from connect import connect
import csv

# ---------------------------
# Upsert (добавить или обновить)
# ---------------------------
def upsert(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL upsert_contact(%s,%s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()


# ---------------------------
# Поиск по шаблону
# ---------------------------
def search(pattern):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    conn.close()


# ---------------------------
# Пагинация
# ---------------------------
def pagination(limit, offset):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_contacts_paginated(%s,%s)", (limit, offset))
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()


# ---------------------------
# Удаление контакта
# ---------------------------
def delete(value):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()
    cur.close()
    conn.close()


# ---------------------------
# Ввод нескольких контактов за раз через запятую
# ---------------------------
def bulk_insert():
    print("Введите несколько контактов через запятую:")
    names_input = input("Имена (через запятую): ")  # пример: Ali, Dana, Aruzhan
    phones_input = input("Телефоны (через запятую): ")  # пример: 777111, abc123, 8700555

    names = [n.strip() for n in names_input.split(",")]
    phones = [p.strip() for p in phones_input.split(",")]

    if len(names) != len(phones):
        print("Ошибка: количество имен и телефонов должно совпадать!")
        return

    for name, phone in zip(names, phones):
        upsert(name, phone)

    print(f"{len(names)} контактов успешно добавлены/обновлены.")


# ---------------------------
# Импорт из CSV
# ---------------------------
def bulk_insert_from_csv(filename="contacts.csv"):
    conn = connect()
    cur = conn.cursor()
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # пропустить заголовок
        for row in reader:
            upsert(row[0], row[1])
    cur.close()
    conn.close()
    print("Контакты из CSV добавлены/обновлены.")


# ---------------------------
# Меню
# ---------------------------
def menu():
    while True:
        print("\n1. Add contact(s) (bulk insert)")
        print("2. Show all contacts (pagination)")
        print("3. Search contacts")
        print("4. Delete contact")
        print("5. Import contacts from CSV")
        print("0. Exit")

        choice = input("Выберите действие: ")

        if choice == "1":
            bulk_insert()

        elif choice == "2":
            limit = int(input("Сколько контактов показать за раз? "))
            offset = int(input("С какого контакта начать? "))
            pagination(limit, offset)

        elif choice == "3":
            pattern = input("Введите часть имени для поиска: ")
            search(pattern)

        elif choice == "4":
            name = input("Введите имя контакта для удаления: ")
            delete(name)

        elif choice == "5":
            bulk_insert_from_csv()

        elif choice == "0":
            print("Выход.")
            break

        else:
            print("Некорректный выбор, попробуйте снова.")


# ---------------------------
# Запуск
# ---------------------------
if __name__ == "__main__":
    menu()