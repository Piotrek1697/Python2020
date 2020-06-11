from List4.DBconnector import DBconnector
from List4.Entity.OrderEntity import OrderEntity
from List4.Entity.OrdesProductsEntity import OrdersProductsEntity
from List4.Entity.ProductEntity import ProductEntity


def _wrap_in_orders_products_list(rows):
    order_products_list = []
    for (produkty_zamowien_id, pz_zamowienie_id, pz_produkt_id, ilosc, p_produkt_id, nazwa, stan, cena_jednostkowa,
         z_zamowienie_id, odbiorca) in rows:
        product = ProductEntity(pz_produkt_id, nazwa, stan, cena_jednostkowa)
        order = OrderEntity(pz_zamowienie_id, odbiorca)
        order_product = OrdersProductsEntity(produkty_zamowien_id, order, product, ilosc)
        order_products_list.append(order_product)
    return order_products_list


class OrdersProductsDAO:

    @staticmethod
    def select_all():
        sql = 'SELECT * FROM sprzedaz.produkty_zamowien pz ' \
              'JOIN sprzedaz.produkty p on pz.produkt_id = p.produkt_id ' \
              'JOIN sprzedaz.zamowienia z on pz.zamowienie_id = z.zamowienie_id'
        rows = DBconnector.fetch_query(sql)
        return _wrap_in_orders_products_list(rows)

    @staticmethod
    def select_last(count):
        sql = 'SELECT * FROM sprzedaz.produkty_zamowien pz ' \
              'JOIN sprzedaz.produkty p on pz.produkt_id = p.produkt_id ' \
              'JOIN sprzedaz.zamowienia z on pz.zamowienie_id = z.zamowienie_id '\
              'ORDER by pz.produkty_zamowien_id DESC LIMIT %s;'
        val = (count,)
        rows = DBconnector.fetch_query_parameters(sql, val)
        return _wrap_in_orders_products_list(rows)
