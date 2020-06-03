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
    def select_all():
        sql = 'SELECT * FROM sprzedaz.zamowienia'
        rows = DBconnector.fetch_query(sql)
        return _wrap_in_order_list(rows)

    @staticmethod
    def select_last():
        sql = 'SELECT * FROM sprzedaz.zamowienia ORDER by zamowienie_id DESC LIMIT 1;'
        rows = DBconnector.fetch_query(sql)
        return _wrap_in_order_list(rows)

    @staticmethod
    def select_by_receiver_name_like(part_name):
        part_name = '%' + part_name + '%'
        sql = 'SELECT * FROM sprzedaz.zamowienia WHERE odbiorca LIKE %s'
        val = (part_name,)
        rows = DBconnector.fetch_query_parameters(sql, val)
        return _wrap_in_order_list(rows)

    @staticmethod
    def select_by_id(order_id):
        sql = "SELECT * FROM sprzedaz.zamowienia WHERE zamowienie_id = %s;"
        val = (order_id,)
        rows = DBconnector.fetch_query_parameters(sql, val)
        return _wrap_in_order_list(rows)

    @staticmethod
    def select_by_receiver(receiver_name):
        sql = "SELECT * FROM sprzedaz.zamowienia WHERE odbiorca = %s;"
        val = (receiver_name,)
        rows = DBconnector.fetch_query_parameters(sql, val)
        return _wrap_in_order_list(rows)

    @staticmethod
    def add_order(receiver):
        sql = 'INSERT INTO sprzedaz.zamowienia (odbiorca) VALUES (%s);'
        val = (receiver,)
        DBconnector.execute_query_insert(sql, val)

    @staticmethod
    def insert(product_id, product_quantity, order_id):
        sql = 'add_order_if_can'
        val = [product_id, product_quantity, order_id]
        rows = DBconnector.call_procedure(sql, val)
        return _wrap_in_order_list(rows)