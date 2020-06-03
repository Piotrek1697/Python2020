from List4.DBconnector import DBconnector
from List4.Entity.ProductEntity import ProductEntity


def _wrap_in_order_list(rows):
    product_list = []
    for (product_id, nazwa, stan, cena_jednostkowa) in rows:
        product = ProductEntity(product_id, nazwa, stan, cena_jednostkowa)
        product_list.append(product)
    return product_list


class ProductDAO:

    @staticmethod
    def select_all():
        sql = 'SELECT * FROM sprzedaz.produkty'
        rows = DBconnector.fetch_query(sql)
        return _wrap_in_order_list(rows)

    @staticmethod
    def select_last():

        sql = 'SELECT * FROM sprzedaz.produkty ORDER by produkt_id DESC LIMIT 1;'
        rows = DBconnector.fetch_query(sql)
        return _wrap_in_order_list(rows)

    @staticmethod
    def select_by_name_like(part_name):
        part_name = '%' + part_name + '%'
        sql = 'SELECT * FROM sprzedaz.produkty WHERE nazwa LIKE %s'
        val = (part_name,)
        rows = DBconnector.fetch_query_parameters(sql, val)
        return _wrap_in_order_list(rows)

    @staticmethod
    def select_by_id(product_id):
        sql = "SELECT * FROM sprzedaz.produkty WHERE produkt_id = %s;"
        val = (product_id,)
        rows = DBconnector.fetch_query_parameters(sql, val)
        return _wrap_in_order_list(rows)

    @staticmethod
    def select_by_name(product_name):

        sql = "SELECT * FROM sprzedaz.produkty WHERE nazwa = %s;"
        val = (product_name,)
        rows = DBconnector.fetch_query_parameters(sql, val)
        return _wrap_in_order_list(rows)