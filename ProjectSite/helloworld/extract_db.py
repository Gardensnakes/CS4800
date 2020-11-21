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

def get_game_name(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT Name FROM game_info WHERE Name=?", (game_name,))
    game_items = []
    for row in cur:
        seller = row[0]
    return seller

def get_game_seller(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT Seller FROM game_info WHERE Name=?", (game_name,))
    game_items = []
    for row in cur:
        seller = row[0]
    return seller

def get_game_release(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT game_release FROM game_info WHERE Name=? AND game_release IS NOT NULL", (game_name,))
    game_items = []
    for row in cur:
        seller = row[0]
    return seller

def get_game_original_price(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT original_price FROM game_info WHERE Name=? AND game_release IS NOT NULL", (game_name,))
    game_items = []
    for row in cur:
        seller = row[0]
    return seller

def get_game_current_price(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT current_price FROM game_info WHERE Name=? AND game_release IS NOT NULL", (game_name,))
    game_items = []
    for row in cur:
        seller = row[0]
    return seller

def get_game_platform(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT MacWin FROM game_info WHERE Name=? AND game_release IS NOT NULL", (game_name,))
    game_items = []
    for row in cur:
        seller = row[0]
    return seller

def get_game_launcher(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT launcher FROM game_info WHERE Name=? AND game_release IS NOT NULL", (game_name,))
    game_items = []
    for row in cur:
        seller = row[0]
    return seller

def get_game_savings(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT savings_price FROM game_info WHERE Name=? AND game_release IS NOT NULL", (game_name,))
    game_items = []
    for row in cur:
        seller = row[0]
    return seller

def get_game_developer(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT developer FROM game_info WHERE Name=? AND game_release IS NOT NULL", (game_name,))
    game_items = []
    for row in cur:
        seller = row[0]
    return seller

def get_game_publisher(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT publisher FROM game_info WHERE Name=? AND game_release IS NOT NULL", (game_name,))
    game_items = []
    for row in cur:
        seller = row[0]
    return seller




# sql_path = r"C:\\Users\\TJ\\Desktop\\ProjectSite\\helloworld\\Games.db"
# conn = create_connection(sql_path)
# print(get_game_seller(conn,'Hades'))


#print (get_game_info(conn,'Hades'))
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