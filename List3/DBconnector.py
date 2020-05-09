import mysql.connector


def connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="toor",
        database='dostawy'
    )
    return mydb


class DBconnector:

    @staticmethod
    def fetch_query(query):
        mydb = connection()

        cursor = mydb.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    @staticmethod
    def fetch_query_parameters(query, val):
        mydb = connection()

        cursor = mydb.cursor()
        cursor.execute(query, val)
        return cursor.fetchall()

    @staticmethod
    def execute_query_insert(query, val):
        mydb = connection()

        cursor = mydb.cursor()
        cursor.execute(query, val)
        mydb.commit()

    @staticmethod
    def execute_query_insert_many(query, val):
        mydb = connection()

        cursor = mydb.cursor()
        cursor.executemany(query, val)
        mydb.commit()
