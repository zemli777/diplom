import sqlite3


# Создание таблицы
# c.execute("""CREATE TABLE articles (
#     title text,
#     full_text text,
#     views integer,
#     avtor text
# )""")
graph = 'graph'
# Создание таблицы
#c.execute(f"""CREATE TABLE {graph} (title text, path text)""")


# Добавление данных
def add_to_db(name, path):
    db = sqlite3.connect('itproger.db')
    # Create Cursor
    c = db.cursor()
    c.execute(f"INSERT INTO {graph} VALUES ('{name}', '{path}')")
    db.commit()
    c.close()

# Удаление данных
def dell_from_db_from_name(name):
    db = sqlite3.connect('itproger.db')
    # Create Cursor
    c = db.cursor()
    c.execute(f"DELETE FROM {graph} WHERE title = '{name}'")
    db.commit()
    c.close()

def dell_from_db_drom_path(path):
    db = sqlite3.connect('itproger.db')
    # Create Cursor
    c = db.cursor()
    c.execute(f"DELETE FROM {graph} WHERE path = '{path}'")
    db.commit()
    c.close()


# Изменение данных
def edit_db_name(name, path):
    db = sqlite3.connect('itproger.db')
    # Create Cursor
    c = db.cursor()
    c.execute(f"UPDATE {graph} SET title = '{name}' WHERE path = '{path}'")
    db.commit()
    c.close()

def edit_db_path(name, path):
    db = sqlite3.connect('itproger.db')
    # Create Cursor
    c = db.cursor()
    c.execute(f"UPDATE {graph} SET path = '{path}' WHERE title = '{name}'")
    db.commit()
    c.close()

# Выборка данных
def find_db_from_name(name):
    db = sqlite3.connect('itproger.db')
    # Create Cursor
    c = db.cursor()
    c.execute(f"SELECT * FROM {graph} WHERE title = {name}")
    db.commit()
    c.close()


def find_db_from_path(path):
    db = sqlite3.connect('itproger.db')
    # Create Cursor
    c = db.cursor()
    c.execute(f"SELECT * FROM {graph} WHERE path = '{path}'")
    db.commit()
    print(c.fetchall())
    c.close()

def all_db():
    db = sqlite3.connect('itproger.db')
    # Create Cursor
    c = db.cursor()
    c.execute(f"SELECT * FROM {graph}")
    db.commit()
    print(c.fetchall())
    c.close()

def clear_db():
    db = sqlite3.connect('itproger.db')
    # Create Cursor
    c = db.cursor()
    c.execute(f"DELETE FROM {graph}")
    db.commit()
    print(c.fetchall())
    c.close()

#name = 'graph3'
#path = 'test.test'
# add_to_db(name, path)
# add_to_db('GG','ANI')
#dell_from_db_from_name(name)
#dell_from_db_from_name('GG')
#clear_db()
#all_db()
#find_db_from_path('ANI')










