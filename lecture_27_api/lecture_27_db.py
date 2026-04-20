import sqlite3
from sqlite3 import Error


db = "flask_db.sqlite"


def create_connection(db_file):
    db_conn = None
    try:
        db_conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return db_conn


def create_table(sql_query):
    db_conn = create_connection(db)
    try:
        c = db_conn.cursor()
        c.execute(sql_query)
        db_conn.close()
    except Error as e:
        print(e)


def main():
    sql_query = """CREATE TABLE users (
                            id INTEGER,
                            name TEXT,
                            login TEXT,
                            password TEXT,
                            PRIMARY KEY(id ASC)
                        );"""

    db_conn = create_connection(db)
    if db_conn is not None:
        create_table(sql_query)


def create_user(name, login, password):
    db_conn = create_connection(db)
    sql_query = (f"INSERT INTO users (name, login, password) "
                 f"VALUES ('{name}', '{login}', '{password}');")
    c = db_conn.cursor()
    c.execute(sql_query)
    db_conn.commit()
    db_conn.close()
    return c.lastrowid


def check_user(login, password):
    db_conn = create_connection(db)
    c = db_conn.cursor()
    sql_query = (f"SELECT * FROM users "
                 f"WHERE login = '{login}' AND password = '{password}';")
    c.execute(sql_query)
    user = c.fetchone()
    db_conn.close()
    return user


if __name__ == '__main__':
    main()
    last_id = create_user(name='John', login='john', password='1111')
    print(last_id)
