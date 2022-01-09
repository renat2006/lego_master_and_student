import sqlite3

con = sqlite3.connect("bd/game_info.db")
cur = con.cursor()


def select_table(table_name, *fields):
    query = f"""SELECT {', '.join(fields)} FROM {table_name}"""
    return cur.execute(query).fetchall()


def update_table(table_name, field, value, field_id, id_name):
    query = f"""UPDATE {table_name}
SET {field}= {value}
WHERE {field_id}= {id_name}"""
    cur.execute(query)
    con.commit()
