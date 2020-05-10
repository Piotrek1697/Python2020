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
        data = cursor.fetchall()
        mydb.close()
        return data

    @staticmethod
    def fetch_query_parameters(query, val):
        mydb = connection()

        cursor = mydb.cursor()
        cursor.execute(query, val)
        data = cursor.fetchall()
        mydb.close()
        return data

    @staticmethod
    def execute_query_insert(query, val):
        mydb = connection()

        cursor = mydb.cursor()
        cursor.execute(query, val)
        mydb.commit()
        mydb.close()

    @staticmethod
    def execute_query_insert_many(query, val):
        mydb = connection()

        cursor = mydb.cursor()
        cursor.executemany(query, val)
        mydb.commit()
        mydb.close()

    @staticmethod
    def execute_query_update(query, val):
        mydb = connection()

        cursor = mydb.cursor()
        cursor.execute(query, val)
        mydb.commit()
        rows_affected = cursor.rowcount
        mydb.close()
        return rows_affected
