/* wyswietlanie zlozonych wnioskow */



/* studenci, ktorzy maja co najmniej jeden nowo zlozony wniosek  */
CREATE INDEX student_lastName_Name_index ON Student (lastname, name);
/* Dlaczego sortowanie nie działa? */
/* DROP INDEX student_lastName_Name_index; */


/* studenci, ktorym wygasla karta mieszkanca (nie posiadają aktualnie aktywnej karty)*/


/* Obciazenia studentow */


/* Budynki */
CREATE INDEX floor_in_building_index ON floor (id_building);
CREATE INDEX module_on_floor_index ON module (id_floor);
CREATE INDEX room_in_module_index ON room (id_module);


/* Liczba aktywnych i i niekatywnych studentow */
CREATE INDEX studentstatus_of_student_index ON Student (id_studentstatus);


/* Wyswietlan wszystkich wynajmow*/



/* Wszystkie sumy platnosci i obciazenia studentow - strasznie dlugo */
CREATE INDEX payment_of_student_index ON payment (id_student);
CREATE INDEX charge_of_student_index ON charge (id_student);
/*
AD 1. hash index dodaje za duży overhead i zapytanie jest wtedy powolne.
*/

/* Pracownicy i liczba wnioskow do nich przypisana */

/* Dane budynkow i ile jest w nich pracownikow */
