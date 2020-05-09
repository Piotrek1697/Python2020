from List3.PrzesylkaEntity import PrzesylkaEntity
from List3.DBconnector import DBconnector


class PrzesylkaDAO:

    @staticmethod
    def select_all():
        sql = 'SELECT * FROM dostawy.przesylki'
        rows = DBconnector.fetch_query(sql)
        list = []
        for (przesylka_ID, przesylka_nadawca, przesylka_odbiorca, przesylka_miastoDostarczenia, przesylka_dataNadania,
             przesylka_dataDostarczenia) in rows:
            p = PrzesylkaEntity(przesylka_ID, przesylka_nadawca, przesylka_odbiorca, przesylka_miastoDostarczenia,
                                przesylka_dataNadania, przesylka_dataDostarczenia)
            list.append(p)
        return list

    @staticmethod
    def insert(przesylka):
        """
        Parameters
        -----------
        przesylka : PrzesylkaEntity
        """
        if not isinstance(przesylka, PrzesylkaEntity):
            raise Exception('Input must be type of PrzesylkaEntity')
        sql = 'INSERT INTO dostawy.przesylki VALUE (%s,%s,%s,%s,%s,%s);'
        val = (f'{przesylka.ID}', f'{przesylka.nadawca}', f'{przesylka.odbiorca}', f'{przesylka.miasto_doreczenia}',
               f'{przesylka.data_nadania}', f'{przesylka.data_dostarczenia}')
        DBconnector.execute_query_insert(sql, val)
