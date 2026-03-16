import sqlite3
from sqlite3 import Error

def create_conn(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(type(conn))
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


def create_table(conn, sql_query):
    try:
        c = conn.cursor()
        c.execute(sql_query)
    except Error as e:
        print(e)


def main(conn):
    sql_create_groups = """CREATE TABLE groups (
                            id INTEGER,
                            title TEXT,
                            PRIMARY KEY(id ASC)
                        );"""

    if conn is not None:
        create_table(conn, sql_create_groups)


def create_group(conn, group_title):
    sql_query = f"INSERT INTO groups (title) VALUES ('{group_title}');"
    c = conn.cursor()
    c.execute(sql_query)
    conn.commit()
    return c.lastrowid


def create_groups(conn, group_titles):
    titles = ", ".join([f"('{g}')" for g in group_titles])
    print(titles)
    sql_query = (f"INSERT INTO groups (title) "
                 f"VALUES {titles};")
    c = conn.cursor()
    c.execute(sql_query)
    conn.commit()


def get_all_groups(conn):
    sql_query = "SELECT * FROM groups ORDER BY title DESC;"
    c = conn.cursor()
    c.execute(sql_query)
    rows = c.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    db = "my_db.sqlite"
    connection = create_conn(db)
    # main(connection)
    with connection:
        # create_group(connection, "549")
        # create_group(connection, "539")
        # create_group(connection, "529")
        create_groups(connection, ['526', '536', '546'])
        get_all_groups(connection)
