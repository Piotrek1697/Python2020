"""
Class that helps execute queries on Order table
"""

from List4.DBconnector import DBconnector
from List4.Entity.OrderEntity import OrderEntity


def _wrap_in_order_list(rows):
    order_list = []
    for (zamowienie_id, odbiorca) in rows:
        order = OrderEntity(zamowienie_id, odbiorca)
        order_list.append(order)
    return order_list


class OrderDAO:

    @staticmethod
    def select_last():
        """
        Select all from Orders table (zamowienia)

        Returns
        -------
        order_list : List[OrderEntity]
        """
        sql = 'SELECT * FROM sprzedaz.zamowienia ORDER by zamowienie_id DESC LIMIT 1;'
        rows = DBconnector.fetch_query(sql)
        return _wrap_in_order_list(rows)

    @staticmethod
    def select_by_id(order_id):
        """
        Select order by ID

        Parameters
        ----------
        order_id : str

        Returns
        -------
        order_list : List[OrderEntity]
        """
        sql = "SELECT * FROM sprzedaz.zamowienia WHERE zamowienie_id = %s;"
        val = (order_id,)
        rows = DBconnector.fetch_query_parameters(sql, val)
        return _wrap_in_order_list(rows)

    @staticmethod
    def add_order(receiver):
        """
        Add new order

        Parameters
        ----------
        receiver : str

        Returns
        -------
        order_list : List[OrderEntity]
        """
        sql = 'INSERT INTO sprzedaz.zamowienia (odbiorca) VALUES (%s);'
        val = (receiver,)
        DBconnector.execute_query_insert(sql, val)

    @staticmethod
    def insert(product_id, product_quantity, order_id):
        """
        Add order if product is available

        Parameters
        ----------
        product_id : str
        product_quantity : str
        order_id : str

        Returns
        -------
        order_list : List[OrderEntity]
        """
        sql = 'add_order_if_can'
        val = [product_id, product_quantity, order_id]
        rows = DBconnector.call_procedure(sql, val)
        return _wrap_in_order_list(rows)
