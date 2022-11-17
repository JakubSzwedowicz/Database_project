psql -h 89.58.24.233 -U postgres -d Akademiki

/* wyswietlanie zlozonych wnioskow */
SELECT a.ID, a.ReceiveDate, ApplicationStatus.Status, ApplicationType.Type
FROM Application a
INNER JOIN ApplicationStatus ON ApplicationStatus.ID = a.ID_ApplicationStatus
INNER JOIN ApplicationType ON ApplicationType.ID = a.ID_ApplicationType
ORDER BY a.ReceiveDate DESC;


/* studenci, ktorzy maja co najmniej jeden nowo zlozony wniosek  */
SELECT Student.ID, Student.LastName, Student.Name
FROM Student
INNER JOIN Application ON Student.ID=Application.ID_Student
INNER JOIN ApplicationStatus ON ApplicationStatus.ID=Application.ID_ApplicationStatus
WHERE ApplicationStatus.Status='RECEIVED'
ORDER BY Student.LastName, Student.Name;


/* studenci, ktorym wygasla karta mieszkanca (nie posiadają aktualnie aktywnej karty)*/
SELECT Student.ID, LastName, Name
FROM STUDENT
INNER JOIN ResidentCard ON ID_Student=Student.ID
WHERE ExpireDate < NOW() 
AND Student.ID NOT IN (
  SELECT Student.ID
  FROM STUDENT
  INNER JOIN ResidentCard ON ID_Student=Student.ID
  WHERE EXPIREDATE > NOW()
)
GROUP BY Student.ID
ORDER BY LastName, Name;


/* Obciazenia studentow */
SELECT s.ID, s.Name, s.LastName, Amount, ChargeDate
FROM Student s
INNER JOIN Charge ON Charge.ID_Student=s.ID
ORDER BY s.ID;

/* Budynki */
SELECT b.ID, Name, Street, BuildingNumber,
(SELECT COUNT(FLOOR.ID) 
FROM FLOOR 
WHERE FLOOR.ID_Building = b.ID) AS Floors,
(SELECT COUNT(KITCHEN.ID) 
FROM KITCHEN
LEFT JOIN FLOOR ON FLOOR.ID_Building=b.ID
WHERE KITCHEN.ID_FLOOR=FLOOR.ID) AS Kitchens,
(SELECT COUNT(LAUNDRY.ID) 
FROM LAUNDRY
LEFT JOIN FLOOR ON FLOOR.ID_Building=b.ID
WHERE LAUNDRY.ID_FLOOR=FLOOR.ID) AS Laundries,
(SELECT COUNT(MODULE.ID) 
FROM MODULE
LEFT JOIN FLOOR ON FLOOR.ID_Building=b.ID
WHERE MODULE.ID_FLOOR=FLOOR.ID) AS Modules,
(SELECT COUNT(ROOM.ID) 
FROM ROOM
LEFT JOIN FLOOR ON FLOOR.ID_Building=b.ID
LEFT JOIN MODULE ON MODULE.ID_FLOOR=FLOOR.ID
WHERE ROOM.ID_MODULE=MODULE.ID) AS Rooms
FROM Building b
GROUP BY b.ID
ORDER BY b.ID, Name;


/* Liczba aktywnych i i niekatywnych studentow */
SELECT StudentStatus.Status, COUNT(StudentStatus.ID)
FROM StudentStatus
INNER JOIN Student ON Student.ID_StudentStatus=StudentStatus.ID
GROUP BY StudentStatus.Status;


/* Wyswietlan wszystkich wynajmow*/
SELECT Student.ID, Name, LastName, StudentNumber, Room.Number as RoomNumber, ExpireDate
FROM RENT r
INNER JOIN ROOM ON r.ID_Room=Room.ID
INNER JOIN STUDENT ON r.ID_Student=Student.ID
ORDER BY r.ExpireDate ASC;


/* Wszystkie sumy platnosci i obciazenia studentow - strasznie dlugo */
SELECT Student.ID, Student.Name, Student.LastName,
(SELECT SUM(Payment.Amount)
FROM Payment
WHERE Payment.ID_Student=Student.ID) AS Payments,
(SELECT SUM(Charge.Amount)
FROM Charge
WHERE Charge.ID_Student=Student.ID) AS Charges
FROM Student
ORDER BY Student.ID;


/* Pracownicy i liczba wnioskow do nich przypisana */
SELECT e.ID, Name, LastName, COUNT(*) AS ApplicationsCount
FROM Employee e
LEFT JOIN Application ON Application.ID_Employee=e.ID
GROUP BY e.ID
ORDER BY e.ID;


/* Dane budynkow i ile jest w nich pracownikow */
SELECT b.ID, name, street, BuildingNumber, City, PostalCode, COUNT(*) AS Employees
FROM Building b
LEFT JOIN Building_Employee ON Building_Employee.ID_Building=b.ID
GROUP BY b.ID
ORDER BY b.ID;