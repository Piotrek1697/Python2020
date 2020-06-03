#Zad 1
CREATE DATABASE IF NOT EXISTS sprzedaz;
USE sprzedaz;
CREATE TABLE IF NOT EXISTS produkty (
 produkt_id INT NOT NULL auto_increment,
 nazwa VARCHAR(200) NOT NULL,
 stan INT NOT NULL,
 cena_jednostkowa DECIMAL(8,2),
 PRIMARY KEY(produkt_id)
);

CREATE TABLE IF NOT EXISTS zamowienia (
zamowienie_id INT NOT NULL auto_increment,
odbiorca VARCHAR(100) NOT NULL,
PRIMARY KEY(zamowienie_id)
);

CREATE TABLE IF NOT EXISTS produkty_zamowien(
produkty_zamowien_id INT NOT NULL auto_increment,
zamowienie_id INT NOT NULL,
produkt_id INT NOT NULL,
ilosc INT NOT NULL,
PRIMARY KEY (produkty_zamowien_id),
UNIQUE KEY produkty_zamowien_unique (zamowienie_id, produkt_id),
FOREIGN KEY (zamowienie_id) references zamowienia(zamowienie_id),
FOREIGN KEY (produkt_id) references produkty(produkt_id)
);


INSERT INTO sprzedaz.produkty (nazwa,stan,cena_jednostkowa)
VALUES
('Krokus', 400, 6.99),
('Kontroler bezprzewodowy PS4, czarny', 1000, 179.89),
('DELL P2720DC',30, 1480),
('PS4 PRO', 200, 1560.99),
('Gran Turismo Sport PS4', 40, 59.99),
('Days Gone PS4', 99, 110.59),
('Kabel HDMI', 500, 24.99),
('Kabel RJ45 10m', 200, 25.99),
('Krowa Texas Longhorn', 3, 120000);

INSERT INTO sprzedaz.zamowienia (odbiorca)
VALUES
('Jan Kowalski'),
('Zbigniew Boniek'),
('Cezary Pazura'),
('Józef Nowak'),
('Krzysztof Krawczyk');

INSERT INTO sprzedaz.produkty_zamowien (zamowienie_id, produkt_id, ilosc)
VALUES
(5, 9, 1),
(5, 7, 4),
(2, 4, 1),
(2,5, 1),
(2,7, 3),
(2,8, 5),
(4,1, 23),
(4,3, 2);

SELECT * FROM sprzedaz.produkty;
SELECT * FROM sprzedaz.zamowienia;
SELECT * FROM sprzedaz.produkty_zamowien;

#Zad 2a
SELECT DISTINCT p.produkt_id, p.nazwa, p.stan, p.cena_jednostkowa,
(SELECT count(pz.produkt_id) FROM produkty_zamowien pz WHERE pz.produkt_id = p.produkt_id) AS `Ilość zamówień`
FROM sprzedaz.produkty p;

#Zad 2b
SELECT p.produkt_id, p.nazwa, p.stan, p.cena_jednostkowa, p.stan * p.cena_jednostkowa 
AS `Aktualna wartość produktów`
FROM sprzedaz.produkty p;

#Zad 2c
SELECT p.nazwa, pz.ilosc, z.odbiorca FROM sprzedaz.produkty_zamowien pz
JOIN sprzedaz.produkty p ON p.produkt_id = pz.produkt_id
JOIN sprzedaz.zamowienia z ON z.zamowienie_id = pz.zamowienie_id;

#Zad 2d
SELECT (sum(p.cena_jednostkowa * pz.ilosc)/count(p.produkt_id)) AS `Średnia wartość zamówienia` 
FROM sprzedaz.produkty_zamowien pz
JOIN sprzedaz.produkty p ON p.produkt_id = pz.produkt_id;

CALL add_order_if_can(9,3,'Piotr Janus');