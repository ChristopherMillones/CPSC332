select * from employee;
insert into employee(Fname,Minit,Lname,Ssn,Bdate,Address,Sex,Salary,Super_ssn,Dno)
values('James','E','Borg','888665555','1937-11-10','450 Stone, Houston,TX', 'M', 55000, NULL,1);

select * from department;
insert into department(Dname,Dnumber,Mgr_ssn,Mgr_start_date)
values('Headquesters',1,'888665555','1981-06-19');

select * from dept_locations;
insert into dept_locations(Dnumber,Dlocation)
values(5,'Houston');


select * from works_on;
SET FOREIGN_KEY_CHECKS=0;
insert into works_on(Essn,Pno,Hours)
values('987987987',30,5.0);
SET FOREIGN_KEY_CHECKS=1;


select * from project;
insert into project(Pname,Pnumber,Plocation,Dnum)
values('Newbenefits',30,'Stafford',4);

select * from dependent;
insert into dependent(Essn,Dependent_name,Sex,Bdate,Relationship)
values('123456789','Elizabeth','F','1967-05-05','Spouse');




