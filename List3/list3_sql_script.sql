#Zad1a, id oraz nadawca
SELECT przesylka_ID, przesylka_nadawca FROM dostawy.przesylki;

#Zad1b Pobierz z tabeli numery (ID) i miasta dostarczenia przesyłek odebranych w grudniu, posortowane alfabetycznie według miasta
SELECT przesylka_ID, przesylka_miastoDostarczenia FROM dostawy.przesylki 
WHERE MONTH(przesylka_dataDostarczenia) = 12 
ORDER BY przesylka_miastoDostarczenia ASC;

#Zad1c Pobierz z tabeli nazwy odbiorców przesyłek zaczynające się na literę „p”.
SELECT przesylka_odbiorca FROM dostawy.przesylki 
WHERE przesylka_odbiorca LIKE 'p%';

#Zad1d Pobierz z tabeli numery (ID) i daty nadania przesyłek, które nie zostały jeszcze dostarczone (tj. pole przesylka_dataDostarczenia jest puste)
SELECT przesylka_ID, przesylka_dataNadania FROM dostawy.przesylki
WHERE przesylka_dataDostarczenia IS null;

#Zad1e Usuń z tabeli przesyłkę o numerze 123446.
DELETE FROM dostawy.przesylki WHERE przesylka_ID = '988989';

#Zad1f Dodaj do tabeli przesyłkę o następujących danych: numer 988989, nadana przez Jana Nowaka
#do Politechniki Wrocławskiej (Wrocław) w dniu 29/04/2020, dostarczona w dniu 20/05/2020.
INSERT INTO dostawy.przesylki
VALUE ('988989','Jan Nowak','Politechnika Wrocławska','Wrocław','2020-04-29','2020-05-20');

#Zad2
USE dostawy;
CREATE TABLE IF NOT EXISTS kurierzy (
kurier_ID INT NOT NULL auto_increment,
kurier_miasto varchar(100) NOT NULL,
kurier_czyDostepny varchar(3),
kurier_aktualnaPrzesylka int,
PRIMARY KEY (kurier_ID),
FOREIGN KEY (kurier_aktualnaPrzesylka) references przesylki(przesylka_ID)
);

INSERT INTO dostawy.kurierzy
VALUES
('123','Szczecin','NIE','111222'),
('124','Wrocław','TAK', NULL),
('125', 'Wrocław', 'NIE', '137654');

SELECT * FROM dostawy.kurierzy;
SELECT * FROM dostawy.przesylki;