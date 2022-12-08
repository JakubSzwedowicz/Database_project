/* wyswietlanie zlozonych wnioskow */
EXPLAIN ANALYZE
SELECT a.ID, a.ReceiveDate, ApplicationStatus.Status, ApplicationType.Type
FROM Application a
INNER JOIN ApplicationHistory ON ApplicationHistory.ID = a.ID_LastApplicationHistory
INNER JOIN ApplicationStatus ON ApplicationStatus.ID = ApplicationHistory.ID_ApplicationStatus
INNER JOIN ApplicationType ON ApplicationType.ID = a.ID_ApplicationType
ORDER BY a.ReceiveDate DESC;


/* studenci, ktorzy maja co najmniej jeden nowo zlozony wniosek  */
EXPLAIN ANALYZE
SELECT Student.ID, MyUser.LastName, MyUser.Name
FROM Student
INNER JOIN MyUser ON MyUser.ID=Student.ID_MyUser
INNER JOIN Application ON Student.ID=Application.ID_Student
INNER JOIN ApplicationHistory ON ApplicationHistory.ID = Application.ID_LastApplicationHistory
INNER JOIN ApplicationStatus ON ApplicationStatus.ID=ApplicationHistory.ID_ApplicationStatus
WHERE ApplicationStatus.Status='RECEIVED'
ORDER BY MyUser.LastName, MyUser.Name;


/* studenci, ktorym wygasla karta mieszkanca (nie posiadają aktualnie aktywnej karty)*/
EXPLAIN ANALYZE
SELECT Student.ID, MyUser.LastName, MyUser.Name
FROM STUDENT
INNER JOIN MyUser ON MyUser.ID=Student.ID_MyUser
INNER JOIN ResidentCard ON ID_Student=Student.ID
WHERE ExpireDate < NOW()
AND Student.ID NOT IN (
  SELECT Student.ID
  FROM STUDENT
  INNER JOIN ResidentCard ON ID_Student=Student.ID
  WHERE EXPIREDATE > NOW()
)
GROUP BY Student.ID, MyUser.LastName, MyUser.Name;


/* Obciazenia studentow */
EXPLAIN ANALYZE
SELECT s.ID, MyUser.Name, MyUser.LastName, Charge.Amount, Charge.ChargeDate
FROM Student s
INNER JOIN MyUser ON MyUser.ID=s.ID_MyUser
INNER JOIN Charge ON Charge.ID_Student=s.ID
ORDER BY s.ID;

/* Budynki */
EXPLAIN ANALYZE
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


/* Liczba aktywnych i niekatywnych studentow */
EXPLAIN ANALYZE
SELECT StudentStatus.Status, COUNT(StudentStatus.ID)
FROM StudentStatus
INNER JOIN Student ON Student.ID_StudentStatus=StudentStatus.ID
GROUP BY StudentStatus.Status;


/* Wyswietlan wszystkich wynajmow */
EXPLAIN ANALYZE
SELECT Student.ID, Name, LastName, StudentNumber, Room.Number as RoomNumber, ExpireDate
FROM RENT r
INNER JOIN ROOM ON r.ID_Room=Room.ID
INNER JOIN STUDENT ON r.ID_Student=Student.ID
INNER JOIN MyUser ON MyUser.ID=Student.ID_MyUser
ORDER BY r.ExpireDate ASC;


/* Wszystkie sumy platnosci i obciazenia studentow - strasznie dlugo */
EXPLAIN ANALYZE
SELECT Student.ID, MyUser.Name, MyUser.LastName,
(SELECT SUM(Payment.Amount)
FROM Payment
WHERE Payment.ID_Student=Student.ID) AS Payments,
(SELECT SUM(Charge.Amount)
FROM Charge
WHERE Charge.ID_Student=Student.ID) AS Charge
FROM Student
INNER JOIN MyUser ON MyUser.ID=Student.ID_MyUser
ORDER BY Student.ID;


/* Pracownicy i liczba wnioskow do nich przypisana */
EXPLAIN ANALYZE
SELECT e.ID, MyUser.Name, MyUser.LastName, COUNT(*) AS ApplicationsCount
FROM Employee e
INNER JOIN MyUser ON MyUser.ID=e.ID_MyUser
LEFT JOIN Application ON Application.ID_Employee=e.ID
GROUP BY e.ID, MyUser.Name, MyUser.LastName
ORDER BY e.ID;


/* Dane budynkow i ile jest w nich pracownikow */
EXPLAIN ANALYZE
SELECT b.ID, name, street, BuildingNumber, City, PostalCode, COUNT(*) AS Employees
FROM Building b
LEFT JOIN Building_Employee ON Building_Employee.ID_Building=b.ID
GROUP BY b.ID
ORDER BY b.ID;