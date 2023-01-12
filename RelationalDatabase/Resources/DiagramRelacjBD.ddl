CREATE TABLE Application (
  ID BIGSERIAL NOT NULL, 
  ID_Student int8 NOT NULL, 
  ID_Employee int8 NOT NULL, 
  ID_ApplicationStatus BIGSERIAL NOT NULL, 
  ReceiveDate date, 
  ID_Utensils int8 NOT NULL, 
  ID_ApplicationType BIGSERIAL NOT NULL, 
  PRIMARY KEY (ID),
  CHECK (ReceiveDate <= NOW())
);

CREATE TABLE Student (
  ID BIGSERIAL NOT NULL, 
  Name varchar(255), 
  LastName varchar(255), 
  StudentNumber varchar(255), 
  BuildingNumber varchar(255), 
  ApartmentNumber varchar(255), 
  Street varchar(255), 
  City varchar(255), 
  PostalCode varchar(255), 
  Email varchar(255), 
  Phone varchar(255), 
  ID_StudentStatus BIGSERIAL NOT NULL, 
  PRIMARY KEY (ID)
);

CREATE TABLE Employee (
  ID BIGSERIAL NOT NULL, 
  Name varchar(255), 
  LastName varchar(255), 
  Street varchar(255), 
  ApartmentNumber varchar(255), 
  BuildingNumber varchar(255), 
  City varchar(255), 
  PostalCode varchar(255), 
  Email varchar(255), 
  Phone varchar(255), 
  Salary numeric(6, 2), 
  PRIMARY KEY (ID),
  CHECK (Salary > 0)
);

CREATE TABLE Utensils (
  ID BIGSERIAL NOT NULL, 
  Description varchar(255) NOT NULL, 
  Quantity int4, 
  ID_Laundry int8 NOT NULL, 
  ID_Kitchen int8 NOT NULL, 
  ID_Room int8 NOT NULL, 
  PRIMARY KEY (ID),
  CHECK (Quantity > 0)
);

CREATE TABLE Laundry (
  ID BIGSERIAL NOT NULL, 
  ID_Floor int8 NOT NULL, 
  PRIMARY KEY (ID)
);

CREATE TABLE Floor (
  ID BIGSERIAL NOT NULL, 
  Number int4, 
  ID_Building int8 NOT NULL, 
  PRIMARY KEY (ID)
);

CREATE TABLE Building (
  ID BIGSERIAL NOT NULL, 
  Name varchar(255), 
  Street varchar(255), 
  BuildingNumber varchar(255), 
  City varchar(255), 
  PostalCode varchar(255), 
  PRIMARY KEY (ID)
);

CREATE TABLE Kitchen (
  ID BIGSERIAL NOT NULL, 
  ID_Floor int8 NOT NULL, 
  PRIMARY KEY (ID)
);

CREATE TABLE Room (
  ID BIGSERIAL NOT NULL, 
  Number int4, 
  ID_Module int8 NOT NULL, 
  PRIMARY KEY (ID)
);

CREATE TABLE Module (
  ID BIGSERIAL NOT NULL, 
  ID_Floor int8 NOT NULL, 
  PRIMARY KEY (ID)
);

CREATE TABLE Rent (
  ID BIGSERIAL NOT NULL, 
  ID_Room int8 NOT NULL, 
  ID_Student int8 NOT NULL, 
  ID_Application int8 NOT NULL, 
  ExpireDate date, 
  PRIMARY KEY (ID)
);

CREATE TABLE Charge (
  ID BIGSERIAL NOT NULL, 
  ID_Student int8 NOT NULL, 
  ChargeDate date, 
  Amount numeric(6, 2), 
  PRIMARY KEY (ID),
  CHECK (ChargeDate <= NOW()),
  CHECK (Amount > 0)
);

CREATE TABLE Payment (
  ID BIGSERIAL NOT NULL, 
  ID_Student int8 NOT NULL, 
  Amount numeric(6, 2), 
  PaymentDate date, 
  PRIMARY KEY (ID),
  CHECK (PaymentDate <= NOW()),
  CHECK (Amount > 0)
);

CREATE TABLE ParkingSpot (
  ID BIGSERIAL NOT NULL, 
  Number int4, 
  ID_Building int8 NOT NULL, 
  PRIMARY KEY (ID)
);

CREATE TABLE ResidentCard (
  ID BIGSERIAL NOT NULL, 
  ID_ParkingSpot int8 NOT NULL, 
  ID_Student int8 NOT NULL, 
  ExpireDate date, 
  ID_CardStatus BIGSERIAL NOT NULL, 
  PRIMARY KEY (ID)
);

CREATE TABLE Building_Employee (
  ID_Building int8 NOT NULL, 
  ID_Employee int8 NOT NULL, 
  PRIMARY KEY (ID_Building, ID_Employee)
);

CREATE TABLE StudentStatus (
  ID BIGSERIAL NOT NULL, 
  Status varchar(255), 
  PRIMARY KEY (ID)
);

CREATE TABLE ApplicationType (
  ID BIGSERIAL NOT NULL, 
  Type varchar(255), 
  PRIMARY KEY (ID)
);

CREATE TABLE ApplicationStatus (
  ID BIGSERIAL NOT NULL, 
  Status varchar(255), 
  PRIMARY KEY (ID)
);

CREATE TABLE CardStatus (
  ID BIGSERIAL NOT NULL, 
  Status varchar(255), 
  PRIMARY KEY (ID)
);

ALTER TABLE 
  Application 
ADD CONSTRAINT FKApplicatio961263 FOREIGN KEY (ID_Student) REFERENCES Student (ID) ON DELETE CASCADE,
ADD CONSTRAINT FKApplicatio545901 FOREIGN KEY (ID_Employee) REFERENCES Employee (ID) ON DELETE CASCADE,
ADD CONSTRAINT FKApplicatio990856 FOREIGN KEY (ID_Utensils) REFERENCES Utensils (ID) ON DELETE CASCADE,
ADD CONSTRAINT FKApplicatio607625 FOREIGN KEY (ID_ApplicationType) REFERENCES ApplicationType (ID) ON DELETE CASCADE,
ADD CONSTRAINT FKApplicatio607626 FOREIGN KEY (ID_ApplicationStatus) REFERENCES ApplicationStatus (ID) ON DELETE CASCADE;

ALTER TABLE 
  Utensils 
ADD CONSTRAINT FKUtensils730005 FOREIGN KEY (ID_Laundry) REFERENCES Laundry (ID) ON DELETE SET NULL,
ADD CONSTRAINT FKUtensils803735 FOREIGN KEY (ID_Kitchen) REFERENCES Kitchen (ID) ON DELETE SET NULL,
ADD CONSTRAINT FKUtensils187071 FOREIGN KEY (ID_Room) REFERENCES Room (ID) ON DELETE SET NULL;

ALTER TABLE 
  Laundry 
ADD CONSTRAINT FKLaundry358599 FOREIGN KEY (ID_Floor) REFERENCES Floor (ID) ON DELETE CASCADE;

ALTER TABLE 
  Floor 
ADD CONSTRAINT FKFloor990185 FOREIGN KEY (ID_Building) REFERENCES Building (ID) ON DELETE CASCADE;

ALTER TABLE 
  Kitchen 
ADD CONSTRAINT FKKitchen864391 FOREIGN KEY (ID_Floor) REFERENCES Floor (ID) ON DELETE CASCADE;

ALTER TABLE 
  Room 
ADD CONSTRAINT FKRoom980156 FOREIGN KEY (ID_Module) REFERENCES Module (ID) ON DELETE CASCADE;

ALTER TABLE 
  Module 
ADD CONSTRAINT FKModule353721 FOREIGN KEY (ID_Floor) REFERENCES Floor (ID) ON DELETE CASCADE;

ALTER TABLE 
  Rent 
ADD CONSTRAINT FKRent541203 FOREIGN KEY (ID_Room) REFERENCES Room (ID) ON DELETE CASCADE,
ADD CONSTRAINT FKRent351308 FOREIGN KEY (ID_Student) REFERENCES Student (ID) ON DELETE CASCADE,
ADD CONSTRAINT FKRent169707 FOREIGN KEY (ID_Application) REFERENCES Application (ID) ON DELETE CASCADE;

ALTER TABLE 
  Charge 
ADD CONSTRAINT FKCharge959840 FOREIGN KEY (ID_Student) REFERENCES Student (ID) ON DELETE CASCADE;

ALTER TABLE 
  Payment 
ADD CONSTRAINT FKPayment190914 FOREIGN KEY (ID_Student) REFERENCES Student (ID) ON DELETE CASCADE;

ALTER TABLE 
  ParkingSpot 
ADD CONSTRAINT FKParkingSpo840532 FOREIGN KEY (ID_Building) REFERENCES Building (ID) ON DELETE CASCADE;

ALTER TABLE 
  ResidentCard 
ADD CONSTRAINT FKResidentCa30431 FOREIGN KEY (ID_ParkingSpot) REFERENCES ParkingSpot (ID) ON DELETE SET NULL,
ADD CONSTRAINT FKResidentCa181885 FOREIGN KEY (ID_Student) REFERENCES Student (ID) ON DELETE CASCADE,
ADD CONSTRAINT FKResidentCa181886 FOREIGN KEY (ID_CardStatus) REFERENCES CardStatus (ID) ON DELETE CASCADE;

ALTER TABLE 
  Building_Employee 
ADD CONSTRAINT FKBuilding_E691225 FOREIGN KEY (ID_Building) REFERENCES Building (ID) ON DELETE CASCADE,
ADD CONSTRAINT FKBuilding_E426156 FOREIGN KEY (ID_Employee) REFERENCES Employee (ID) ON DELETE CASCADE;

ALTER TABLE 
  Student 
ADD CONSTRAINT FKStudent793410 FOREIGN KEY (ID_StudentStatus) REFERENCES StudentStatus (ID) ON DELETE CASCADE;
INSERT INTO APPLICATIONTYPE(TYPE) VALUES ('RENT ROOM'), ('LEAVE ROOM'), ('REPORT ISSUE'), ('PAYMENT ISSUE');
INSERT INTO APPLICATIONSTATUS(STATUS) VALUES ('RECEIVED'),('CLOSED'), ('PROCESSING'), ('WAITING');
INSERT INTO CARDSTATUS(STATUS) VALUES ('VALID'),('INVALID');
INSERT INTO STUDENTSTATUS(STATUS) VALUES ('ACTIVE'), ('INACTIVE');