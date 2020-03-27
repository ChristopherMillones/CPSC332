create table artist(
FLname varchar(20) not null,
phone int,
address varchar(20),
birthPlace varchar(20),
age int,
styleOfArt varchar(20),
primary key(FLname)
);

create table artShows(
contactNumber int not null,
contact varchar(20),
location varchar(20),
dateShow date,
timeShow varchar(20),
primary key(contactNumber)
);

create table customer(
artPreference varchar(20),
phone int,
customerNumber int not null,
primary key(customerNumber)
);

create table artWork(
typeOfArt varchar(20),
dateCreated date,
dateAcquired date,
price float,
location varchar(20),
title varchar(20),
primary key(title)
);
show tables;







