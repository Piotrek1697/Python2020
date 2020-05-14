from List3.Entity.ParcelEntity import ParcelEntity
from List3.DBconnector import DBconnector


def _wrap_in_parcel_list(rows):
    parcel_list = []
    for (przesylka_ID, przesylka_nadawca, przesylka_odbiorca, przesylka_miastoDostarczenia, przesylka_dataNadania,
         przesylka_dataDostarczenia) in rows:
        p = ParcelEntity(przesylka_ID, przesylka_nadawca, przesylka_odbiorca, przesylka_miastoDostarczenia,
                         przesylka_dataNadania, przesylka_dataDostarczenia)
        parcel_list.append(p)
    return parcel_list


class ParcelDAO:

    @staticmethod
    def select_all():
        sql = 'SELECT * FROM dostawy.przesylki'
        rows = DBconnector.fetch_query(sql)
        return _wrap_in_parcel_list(rows)

    @staticmethod
    def select_by_id(parcel_id):
        sql = "SELECT * FROM dostawy.przesylki WHERE przesylka_ID = %s;"
        val = (parcel_id,)
        rows = DBconnector.fetch_query_parameters(sql, val)
        return _wrap_in_parcel_list(rows)

    @staticmethod
    def select_by_sender(sender_name):
        sql = "SELECT * FROM dostawy.przesylki WHERE przesylka_nadawca = %s;"
        val = (sender_name,)
        rows = DBconnector.fetch_query_parameters(sql, val)
        return _wrap_in_parcel_list(rows)

    @staticmethod
    def select_by_receiver(receiver_name):
        sql = "SELECT * FROM dostawy.przesylki WHERE przesylka_odbiorca = %s;"
        val = (receiver_name,)
        rows = DBconnector.fetch_query_parameters(sql, val)
        return _wrap_in_parcel_list(rows)

    @staticmethod
    def select_by_city(city):
        sql = "SELECT * FROM dostawy.przesylki WHERE przesylka_miastoDostarczenia = %s;"
        val = (city,)
        rows = DBconnector.fetch_query_parameters(sql, val)
        return _wrap_in_parcel_list(rows)

    @staticmethod
    def select_by_sent_date(begin_date, end_date):
        sql = "SELECT * FROM dostawy.przesylki WHERE przesylka_dataNadania > %s AND przesylka_dataNadania < %s;"
        val = (begin_date, end_date)
        rows = DBconnector.fetch_query_parameters(sql, val)
        return _wrap_in_parcel_list(rows)

    @staticmethod
    def select_by_receive_date(begin_date, end_date):
        sql = "SELECT * FROM dostawy.przesylki WHERE przesylka_dataDostarczenia > %s AND przesylka_dataDostarczenia < %s;"
        val = (begin_date, end_date)
        rows = DBconnector.fetch_query_parameters(sql, val)
        return _wrap_in_parcel_list(rows)

    @staticmethod
    def select_by_status(status):
        sql = 'checkStatus'
        val = [status]
        rows = DBconnector.call_procedure(sql, val)
        for r in rows:
            return _wrap_in_parcel_list(r.fetchall())

    @staticmethod
    def insert(parcel):
        """
        Parameters
        -----------
        parcel : ParcelEntity
        """
        if not isinstance(parcel, ParcelEntity):
            raise Exception('Input must be type of ParcelEntity')
        sql = 'INSERT INTO dostawy.przesylki (przesylka_nadawca, przesylka_odbiorca,' \
              'przesylka_miastoDostarczenia, przesylka_dataNadania,' \
              'przesylka_dataDostarczenia) VALUES (%s,%s,%s,%s,%s);'
        val = (parcel.sender, parcel.receiver, parcel.delivery_city,
               parcel.sent_date, parcel.delivery_date)
        DBconnector.execute_query_insert(sql, val)

    @staticmethod
    def insert_many(parcel_list):
        """
        Parameters
        ----------
        parcel_list : list[ParcelEntity]
        """
        values = []
        sql = 'INSERT INTO dostawy.przesylki (przesylka_nadawca, przesylka_odbiorca,' \
              'przesylka_miastoDostarczenia, przesylka_dataNadania,' \
              'przesylka_dataDostarczenia) VALUES (%s,%s,%s,%s,%s);'
        for parcel in parcel_list:
            val = (parcel.sender, parcel.receiver, parcel.delivery_city,
                   parcel.sent_date, parcel.delivery_date)
            values.append(val)
        DBconnector.execute_query_insert_many(sql, values)

    @staticmethod
    def delivery_confirmation(parcel_id, confirm_date):
        sql = "UPDATE dostawy.przesylki " \
              "SET przesylka_dataDostarczenia = %s WHERE przesylka_ID = %s;"
        val = (confirm_date, parcel_id)
        return DBconnector.execute_query_update(sql, val)
