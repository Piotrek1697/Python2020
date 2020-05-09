class PrzesylkaEntity:
    ID = 0
    nadawca = ''
    odbiorca = ''
    miasto_doreczenia = ''
    data_nadania = ''
    data_dostarczenia = ''

    def __init__(self, id_przesylka, nadawca, odbiorca, miasto_doreczenia, data_nadania, data_dostarczenia):
        self.ID = id_przesylka
        self.nadawca = nadawca
        self.odbiorca = odbiorca
        self.miasto_doreczenia = miasto_doreczenia
        self.data_nadania = data_nadania
        self.data_dostarczenia = data_dostarczenia
