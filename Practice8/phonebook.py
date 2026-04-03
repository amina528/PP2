from connect import connect


def upsert(name, phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s,%s)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()


def search(pattern):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()


def pagination(limit, offset):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM get_contacts_paginated(%s,%s)",
        (limit, offset)
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def delete(value):
    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()

    cur.close()
    conn.close()


def bulk_insert():
    conn = connect()
    cur = conn.cursor()

    names = ['Ali', 'Dana', 'Aruzhan']
    phones = ['777111', 'abc123', '8700555']

    cur.execute(
        "CALL insert_many(%s,%s)",
        (names, phones)
    )

    conn.commit()
    cur.close()
    conn.close()


# TEST MENU
if __name__ == "__main__":
    upsert("Amina", "87001234567")
    upsert("Amina", "999999")   # update

    bulk_insert()

    print("\nSearch:")
    search("Am")

    print("\nPagination:")
    pagination(2, 0)

    delete("Dana")