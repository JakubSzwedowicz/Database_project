CREATE TABLE MyUser (
  ID BIGSERIAL NOT NULL, 
  Name varchar(255), 
  LastName varchar(255), 
  Street varchar(255), 
  City varchar(255), 
  PostalCode varchar(255), 
  Email varchar(255), 
  Phone varchar(255), 
  isAdmin boolean,
  ID_EmployeeTemp int8,
  ID_StudentTemp int8,
  PRIMARY KEY (ID)
);


/* Przeniesienie danych z employee i studenta do usera */
INSERT INTO MyUser(Name, LastName, Street, Email, Phone, City, PostalCode, ID_StudentTemp)
(SELECT Name, LastName, Street, Email, Phone, City, PostalCode, ID FROM Student);

INSERT INTO MyUser (Name, LastName, Street, Email, Phone, City, PostalCode, ID_EmployeeTemp)
(SELECT Name, LastName, Street, Email, Phone, City, PostalCode, ID FROM Employee);

/* dodanie klucza obcego w tabeli student i employee */
ALTER TABLE Student
ADD ID_MyUser int8;

ALTER TABLE Student
ADD FOREIGN KEY(ID_MyUser) REFERENCES MyUser(ID);

ALTER TABLE Employee
ADD ID_MyUser int8;

ALTER TABLE Employee
ADD FOREIGN KEY(ID_MyUser) REFERENCES MyUser(ID);


/* umieszczenie w student i employee odpowiadajacych kluczy obcych z tabeli myuser */
UPDATE STUDENT
SET ID_MyUser = MyUser.ID
FROM MyUser
WHERE Student.ID = MyUser.ID_StudentTemp;

UPDATE Employee
SET ID_MyUser = MyUser.ID
FROM MyUser
WHERE Employee.ID = MyUser.ID_EmployeeTemp;

/* stworzenie tabeli application history */
CREATE TABLE ApplicationHistory (
  ID BIGSERIAL NOT NULL, 
  ID_Application int8 NOT NULL, 
  ID_MyUser int8, 
  ID_Utensils int8 NOT NULL, 
  ApplicationTimestamp timestamp, 
  ID_ApplicationStatus int8 NOT NULL,
  Notes varchar(255), 
  PRIMARY KEY (ID),
  FOREIGN KEY(ID_Application) REFERENCES Application(ID),
  FOREIGN KEY(ID_MYUSER) REFERENCES MyUser(ID),
  FOREIGN KEY(ID_Utensils) REFERENCES Utensils(ID),
  FOREIGN KEY(ID_ApplicationStatus) REFERENCES ApplicationStatus(ID)
);

/* przeniesienie danych do applicationhistory z application */
INSERT INTO ApplicationHistory(ID_Application, ID_Utensils, ID_ApplicationStatus)
(SELECT ID, ID_Utensils, ID_ApplicationStatus FROM APPLICATION);

/* dodanie klucza obcego na applicationhistory w tabeli application */
ALTER TABLE APPLICATION
ADD ID_LastApplicationHistory int8;

ALTER TABLE APPLICATION
ADD FOREIGN KEY(ID_LastApplicationHistory) REFERENCES ApplicationHistory(ID);


/* usuniecie zbednych atrybutów */
ALTER TABLE APPLICATION
DROP ID_ApplicationStatus,
DROP ID_UTENSILS;

ALTER TABLE STUDENT
DROP Name,
DROP LastName,
DROP Street,
DROP Email,
DROP Phone,
DROP City,
DROP PostalCode,
DROP BuildingNumber,
DROP ApartmentNumber;

ALTER TABLE EMPLOYEE
DROP Name,
DROP LastName,
DROP Street,
DROP Email,
DROP Phone,
DROP City,
DROP PostalCode,
DROP BuildingNumber,
DROP ApartmentNumber;

ALTER TABLE MyUser
DROP ID_EmployeeTemp,
DROP ID_StudentTemp;
