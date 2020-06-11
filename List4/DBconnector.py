"""
Class that helps to manage database connection and executes queries
"""
import mysql.connector


def connection():
    """
    Get connection to specific database. Database info is hard-coded

    Returns
    -------
    mydb : MySQLConnection

    """
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="toor",
        database='sprzedaz'
    )
    return mydb


class DBconnector:

    @staticmethod
    def fetch_query(query):
        """
        Execute query and returns data from query

        Parameters
        ----------
        query : str
            String that represents sql query (SELECT)

        Returns
        -------
        data : list
            List of tuples
        """
        mydb = connection()

        cursor = mydb.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        mydb.close()
        return data

    @staticmethod
    def fetch_query_parameters(query, val):
        """
        Execute query with parameters and returns data from query

        Parameters
        ----------
        query : str
           String that represents sql query (SELECT)
        val : Tuple[str]
            Tuple with parameters to query

        Returns
        -------
        data : list
           List of tuples
        """
        mydb = connection()

        cursor = mydb.cursor()
        cursor.execute(query, val)
        data = cursor.fetchall()
        cursor.close()
        mydb.close()
        return data

    @staticmethod
    def call_procedure(procedure_name, args):
        """
        Call specific stored procedure with arguments and returns results

        Parameters
        ----------
        procedure_name : str
        args : List[str]

        Returns
        -------
        data : List
            List of tuples
        """
        mydb = connection()
        cursor = mydb.cursor()
        cursor.callproc(procedure_name, args)
        data = cursor.stored_results()
        mydb.commit()
        cursor.close()
        mydb.close()
        return data

    @staticmethod
    def execute_query_insert(query, val):
        """
        Executes insert query with parameters, and commits changes

        Parameters
        ----------
        query : str
            Insert query
        val : Tuple[str]
            Parameters to insert
        """
        mydb = connection()

        cursor = mydb.cursor()
        cursor.execute(query, val)
        mydb.commit()
        cursor.close()
        mydb.close()

    @staticmethod
    def execute_query_insert_many(query, val):
        """
        Executes many insert query with parameters, and commits changes

        Parameters
        ----------
        query : str
           Insert query
        val : Tuple[str]
           Parameters to insert
        """
        mydb = connection()

        cursor = mydb.cursor()
        cursor.executemany(query, val)
        mydb.commit()
        cursor.close()
        mydb.close()

    @staticmethod
    def execute_query_update(query, val):
        """
        Executes update query

        Parameters
        ----------
        query : str
            Update query
        val : Tuple[str]
            Parameters to update

        Returns
        -------
        row_affected : int
            Count of rows that was affected
        """
        mydb = connection()

        cursor = mydb.cursor()
        cursor.execute(query, val)
        mydb.commit()
        rows_affected = cursor.rowcount
        cursor.close()
        mydb.close()
        return rows_affected
