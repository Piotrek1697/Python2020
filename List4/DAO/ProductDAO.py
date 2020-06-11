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
    def select_products_order_qunatity():
        sql = "SELECT DISTINCT p.produkt_id, p.nazwa, " \
              "(SELECT SUM(pz.ilosc) FROM produkty_zamowien pz WHERE pz.produkt_id = p.produkt_id) AS `stan_zamowienia`" \
              ", cena_jednostkowa " \
              "FROM sprzedaz.produkty p;"

        rows = DBconnector.fetch_query(sql)
        return _wrap_in_order_list(rows)
