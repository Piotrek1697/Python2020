"""
Class that helps executing queries on Courier table (kurierzy).

"""

from List3.Entity.ParcelEntity import ParcelEntity
from List3.Entity.CourierEntity import CourierEntity
from List3.DBconnector import DBconnector


class CourierDAO:

    @staticmethod
    def select_all():
        """
        Select all elements from Courier (kurierzy) table

        Returns
        -------
        courier_list : list[CourierEntity]
        """
        sql = 'SELECT * FROM dostawy.kurierzy k ' \
              'LEFT JOIN dostawy.przesylki p ' \
              'ON k.kurier_aktualnaPrzesylka = p.przesylka_ID;'
        rows = DBconnector.fetch_query(sql)
        courier_list = []
        for (kurier_ID, kurier_miasto, kurier_czyDostepny, kurier_aktualnaPrzesylka, przesylka_ID, przesylka_nadawca,
             przesylka_odbiorca, przesylka_miastoDostarczenia, przesylka_dataNadania,
             przesylka_dataDostarczenia) in rows:
            p = ParcelEntity(przesylka_ID, przesylka_nadawca, przesylka_odbiorca, przesylka_miastoDostarczenia,
                             przesylka_dataNadania, przesylka_dataDostarczenia)
            c = CourierEntity(kurier_ID, kurier_miasto, kurier_czyDostepny, p)
            courier_list.append(c)
        return courier_list

    @staticmethod
    def select_courier_by_parcel(parcel_id):
        """
        Select Courier by ID.

        Parameters
        ----------
        parcel_id : str

        Returns
        -------
        courier_list : list[CourierEntity]
        """
        sql = 'SELECT * FROM dostawy.kurierzy k ' \
              'LEFT JOIN dostawy.przesylki p ' \
              'ON k.kurier_aktualnaPrzesylka = p.przesylka_ID WHERE kurier_aktualnaPrzesylka = %s;'
        val = (parcel_id,)
        rows = DBconnector.fetch_query_parameters(sql, val)
        courier_list = []
        for (kurier_ID, kurier_miasto, kurier_czyDostepny, kurier_aktualnaPrzesylka, przesylka_ID, przesylka_nadawca,
             przesylka_odbiorca, przesylka_miastoDostarczenia, przesylka_dataNadania,
             przesylka_dataDostarczenia) in rows:
            p = ParcelEntity(przesylka_ID, przesylka_nadawca, przesylka_odbiorca, przesylka_miastoDostarczenia,
                             przesylka_dataNadania, przesylka_dataDostarczenia)
            c = CourierEntity(kurier_ID, kurier_miasto, kurier_czyDostepny, p)
            courier_list.append(c)
        return courier_list

    @staticmethod
    def update_free_courier_parcel(parcel_id):
        """
        Add parcel to first free courier

        Parameters
        ----------
        parcel_id : str

        Returns
        -------
        row_count : int
            Quantity of rows that were updated
        """
        sql = "UPDATE dostawy.kurierzy SET kurier_czyDostepny = 'NIE', kurier_aktualnaPrzesylka = %s " \
              "WHERE kurier_ID = " \
              "(SELECT kurier_ID FROM " \
              "(SELECT kurier_ID FROM dostawy.kurierzy WHERE kurier_czyDostepny = 'TAK' LIMIT 1) as tempTable);"
        val = (parcel_id,)
        return DBconnector.execute_query_update(sql, val)

    @staticmethod
    def update_courier_status(status, parcel_id):
        """
        Updates couriers status (if is available)

        Parameters
        ----------
        status : str
            'Tak' - is available; 'Nie' - is not available
        parcel_id : str
            Parcel ID
        """
        sql = "UPDATE dostawy.kurierzy  SET kurier_czyDostepny = %s, kurier_aktualnaPrzesylka = NULL " \
              "WHERE kurier_ID = " \
              "(SELECT kurier_ID FROM " \
              "(SELECT kurier_ID FROM dostawy.kurierzy WHERE kurier_aktualnaPrzesylka = %s LIMIT 1) as tempTable);"
        val = (status, parcel_id)
        return DBconnector.execute_query_update(sql, val)
