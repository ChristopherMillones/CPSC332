SHOW TABLES;
create table EMPLOYEE
(
Fname varchar(15) NOT NULL,
Minit CHAR,
Lname VARCHAR(15) NOT NULL,
Ssn   CHAR(9) NOT NULL,
Bdate DATE,
Address VARCHAR(30),
Sex   CHAR,
Salary  DECIMAL(10,2),
Super_ssn CHAR(9),
Dno    INT  NOT NULL,
primary key(Ssn)
);













