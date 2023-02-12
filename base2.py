import sqlite3
from pars_file import Get_adjacency_matrix
# Создание таблицы
# c.execute("""CREATE TABLE articles (
#     title text,
#     full_text text,
#     views integer,
#     avtor text
# )""")
graph = 'graph'
# Создание таблицы
# db = sqlite3.connect('itproger2.db')
#     # Create Cursor
# c = db.cursor()
# c.execute(f"""CREATE TABLE {graph} (name text, list text)""")
# c.close()

def add_to_db(name, list):
    db = sqlite3.connect('itproger2.db')
    # Create Cursor
    c = db.cursor()
    c.execute(f"INSERT INTO {graph} VALUES ('{name}', '{list}')")
    db.commit()
    c.close()

def find_db_from_name(name):
    db = sqlite3.connect('itproger2.db')
    # Create Cursor
    c = db.cursor()
    c.execute(f"SELECT * FROM name WHERE name = name")
    db.commit()
    c.close()

def all_db():
    db = sqlite3.connect('itproger2.db')
    # Create Cursor
    c = db.cursor()
    c.execute(f"SELECT * FROM {graph}")
    db.commit()
    print(c.fetchall())
    c.close()

find_db_from_name('graph1')
all_db()
