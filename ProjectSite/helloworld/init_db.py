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


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_game(conn, project):
    sql = '''INSERT INTO game_info(name,seller,game_release, original_price, current_price, MacWin, launcher, 
    savings_price, developer, publisher, date_scraped) 
    VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


# def main():
#     name = 'Hades'
#     release_date = '2020-11-17'
#     original_price = 65.99
#     current_price = 69.99
#     platform = 'PS 5'
#     launcher = 'Steam'
#     savings_price = 10.99
#     developer = 'Treyarch'
#     publisher = 'Activision'
#     sql_path = r"C:\\Users\\TJ\\Desktop\\ProjectSite\\helloworld\\Games.db"
#     conn = create_connection(sql_path)
#     game_table = """ CREATE TABLE IF NOT EXISTS game_info (
#                                             Name TEXT PRIMARY KEY,
#                                             release_date TEXT,
#                                             original_price REAL,
#                                             current_price REAL,
#                                             platform TEXT,
#                                             launcher TEXT,
#                                             savings_price REAL,
#                                             developer TEXT,
#                                             publisher TEXT             
#                                         ); """
#     # seller_game = """ CREATE TABLE IF NOT EXISTS game_info (
#     #                                         Seller TEXT PRIMARY KEY,
            
#     #                                         original_price REAL,
#     #                                         current_price REAL,
                                            
#     #                                         savings_price REAL,
                                                  
#     #                                     ); """
#     if conn is not None:
#         create_table(conn, game_table)
#     else:
#         print("Error! cannot create the database connection.")
#     with conn:
#         game = (name, release_date, original_price, current_price, platform, launcher, savings_price, developer, publisher)
#         insert_game(conn, game)


#main()