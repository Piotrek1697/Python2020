"""
Class that helps executing queries on Parcel table (przesylki).

"""

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
        """
        Select all elements from Parcel (przesylki) table

        Returns
        -------
        parcel_list : list[ParcelEntity]
        """
        sql = 'SELECT * FROM dostawy.przesylki'
        rows = DBconnector.fetch_query(sql)
        return _wrap_in_parcel_list(rows)

    @staticmethod
    def select_last():
        """
        Select all elements from Parcel (przesylki) table

        Returns
        -------
        parcel_list : list[ParcelEntity]
        """
        sql = 'SELECT * FROM dostawy.przesylki ORDER by przesylka_ID DESC LIMIT 1;'
        rows = DBconnector.fetch_query(sql)
        return _wrap_in_parcel_list(rows)

    @staticmethod
    def select_by_id(parcel_id):
        """
        Select Parcel by ID.

        Parameters
        ----------
        parcel_id : str

        Returns
        -------
        parcel_list : list[ParcelEntity]
        """
        sql = "SELECT * FROM dostawy.przesylki WHERE przesylka_ID = %s;"
        val = (parcel_id,)
        rows = DBconnector.fetch_query_parameters(sql, val)
        return _wrap_in_parcel_list(rows)

    @staticmethod
    def select_by_sender(sender_name):
        """
        Select Parcels by sender_name

        Parameters
        ----------
        sender_name : str

        Returns
        -------
        parcel_list : list[ParcelEntity]
        """
        sql = "SELECT * FROM dostawy.przesylki WHERE przesylka_nadawca = %s;"
        val = (sender_name,)
        rows = DBconnector.fetch_query_parameters(sql, val)
        return _wrap_in_parcel_list(rows)

    @staticmethod
    def select_by_receiver(receiver_name):
        """
        Select parcels by receiver name

        Parameters
        ----------
        receiver_name : str

        Returns
        -------
        parcel_list : list[ParcelEntity]
        """
        sql = "SELECT * FROM dostawy.przesylki WHERE przesylka_odbiorca = %s;"
        val = (receiver_name,)
        rows = DBconnector.fetch_query_parameters(sql, val)
        return _wrap_in_parcel_list(rows)

    @staticmethod
    def select_by_city(city):
        """
        Select parcels by receive city

        Parameters
        ----------
        city : str
            City where parcel was/will be received

        Returns
        -------
        parcel_list : list[ParcelEntity]
        """
        sql = "SELECT * FROM dostawy.przesylki WHERE przesylka_miastoDostarczenia = %s;"
        val = (city,)
        rows = DBconnector.fetch_query_parameters(sql, val)
        return _wrap_in_parcel_list(rows)

    @staticmethod
    def select_by_sent_date(begin_date, end_date):
        """
        Select parcels by sent date interval

        Parameters
        ----------
        begin_date : date
            interval start date
        end_date : date
            interval stop date

        Returns
        -------
        parcel_list : list[ParcelEntity]
        """
        sql = "SELECT * FROM dostawy.przesylki WHERE przesylka_dataNadania > %s AND przesylka_dataNadania < %s;"
        val = (begin_date, end_date)
        rows = DBconnector.fetch_query_parameters(sql, val)
        return _wrap_in_parcel_list(rows)

    @staticmethod
    def select_by_receive_date(begin_date, end_date):
        """
        Select parcels by receive date interval

        Parameters
        ----------
        begin_date : date
            interval start date
        end_date : date
            interval stop date

        Returns
        -------
        parcel_list : list[ParcelEntity]
        """
        sql = "SELECT * FROM dostawy.przesylki WHERE przesylka_dataDostarczenia > %s AND przesylka_dataDostarczenia < %s;"
        val = (begin_date, end_date)
        rows = DBconnector.fetch_query_parameters(sql, val)
        return _wrap_in_parcel_list(rows)

    @staticmethod
    def select_by_status(status):
        """
        Select parcels by input status ('delivered', 'send', 'passed to courier'). Executes stored procedure that
        distinguish status and returns adequate select

        Parameters
        ----------
        status : str

        Returns
        -------
        parcel_list : list[ParcelEntity]
        """
        sql = 'checkStatus'
        val = [status]
        rows = DBconnector.call_procedure(sql, val)
        for r in rows:
            return _wrap_in_parcel_list(r.fetchall())

    @staticmethod
    def insert(parcel):
        """
        Insert parcel into database

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
        Insert list of parcels into database.
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
        """
        Updates parcel, by setting delivery date to parcel

        Parameters
        ----------
        parcel_id : str
        confirm_date : date

        Returns
        -------
        row_count : int
            count of rows that was affected
        """
        sql = "UPDATE dostawy.przesylki " \
              "SET przesylka_dataDostarczenia = %s WHERE przesylka_ID = %s;"
        val = (confirm_date, parcel_id)
        return DBconnector.execute_query_update(sql, val)
