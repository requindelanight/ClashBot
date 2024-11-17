# -*- coding: utf-8 -*-

###########################################
#                libraries                #
###########################################
import mariadb
###########################################

def connection():
    """
    https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
    """
    try:
        conn = mariadb.connect(
            user="clash_admin",
            password="votremotdepasse",
            host="localhost",
            port=3306, #port par défaut
            database="clash_of_clan"
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")

if __name__ == "__main__":
    conn = connection()
    conn.close()