-- Christopher Millones 

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

create table DEPARTMENT
(
Dname	varchar(15)	NOT NULL,
Dnumber	int	NOT NuLL,
Mgr_ssn	char(9)	NOT NULL,
Mgr_start_date	Date,
primary key(Dnumber),
unique(Dname),
foreign key(Mgr_ssn) references EMPLOYEE(Ssn)
);

create table DEPT_LOCATIONS
(
Dnumber	int	NOT NULL,
Dlocation	varchar(15)	NOT NULL,
primary key(Dnumber,Dlocation),
foreign key(Dnumber) references DEPARTMENT(Dnumber)
);

create table PROJECT
(
Pname	varchar(15)	NOT NULL,
Pnumber	int not null,
Plocation	varchar(15),
Dnum	int	not null,
primary key(Pnumber),
unique(Pname),
foreign key(Dnum) references DEPARTMENT(Dnumber)
);

create table WORKS_ON
(
Essn	char(9)	not null,
Pno	int	not null,
Hours	decimal(3,1)	not null,
primary key(Essn,Pno),
foreign key(Essn) references EMPLOYEE(Ssn),
foreign key(Pno) references PROJECT(Pnumber)
);

create table DEPENDENT
(
Essn	char(9)	not null,
Dependent_name	varchar(15)	not null,
Sex	char,
Bdate	date,
Relationship	varchar(8),
primary key (Essn,Dependent_name),
foreign key (Essn) references EMPLOYEE(Ssn)
);















































