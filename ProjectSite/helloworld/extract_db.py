from django.http import HttpResponse
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def get_game_info(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM game_info WHERE Name=?", (game_name,))
    rows = cur.fetchall()
    game_items = []
    for row in rows:
        game_items.append(row)
    return game_items


# def main():
#     sql_path = r"C:\\Users\\TJ\\Desktop\\ProjectSite\\helloworld\\Games.db"
#     conn = create_connection(sql_path)
#     game_name = "Hades"
#     with conn:
#         game_info = get_game_info(conn, game_name)
#     for entry in game_info:
#        # return HttpResponse(entry)
#        print(entry)


#main()