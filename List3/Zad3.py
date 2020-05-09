import mysql.connector

from List3.PrzesylkaDAO import PrzesylkaDAO
from List3.PrzesylkaEntity import PrzesylkaEntity


def main():
    lista = PrzesylkaDAO.select_all()
    for p in lista:
        print(p.nadawca)

    p = PrzesylkaEntity(1, 'Jan Kowalski', 'Ja', 'Goleniów', '2019-10-11', '2019-10-12')
    PrzesylkaDAO.insert(p)


if __name__ == '__main__':
    main()
