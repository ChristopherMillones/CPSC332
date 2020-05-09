# Authors: Chris Millones & Abby Aguilar
create table artist(
FLname varchar(30) not null,
phone bigint,
address varchar(30),
birthPlace varchar(20),
age int,
styleOfArt varchar(20),
primary key(FLname)
);

create table artShows(
contactNumber bigint not null,
contact varchar(20),
location varchar(20),
dateShow date,
timeShow varchar(20),
primary key(contactNumber)
);

create table customer(
artPreference varchar(30),
phone bigint,
customerNumber int not null,
primary key(customerNumber)
);

create table artWork(
typeOfArt varchar(30),
dateCreated date,
dateAcquired date,
price decimal(6,2),
location varchar(30),
title varchar(20),
primary key(title)
);

insert into artist 
values("Chris Millones",1234567899, "1 jeff irvine,CA", "the bronx", 25, "Pottery"),("Abby Aguilar",9987654321,"9 the streets Ny,NY", "Miami",23,"Sculpture"),
	  ("Jack Daniels", 4441234321, "4 the bar San Diego, CA", "the beach", 60, "Pop Art"),("barb ra", 1010101010, "4 humble Anahiem, CA", "unknown", 14, "Minimalism");
      
insert into artshows
values(5554449900, "Jeff joe", "Toronto Canada", "2020-09-15", "5:00 PM"),(0909099099, "arthur artty", "Mission Viejo, CA", "2020-10-10","7:00 PM"),(7539518526,"Stewart Little", "Italy", "2020-10-31", "10:00PM"),
	  (4444444444, "Buzz Lightyear", "Andy's Room", "2020-1-1","1:00PM");
      
insert into customer
values("Surrealism", 0991334855, 41),("Pop Art", 1234567892, 11), ("Still Life", 1234567890, 1),("Works of 19th century", 5987654321, 5);

insert into artwork
values ("Photorealism", "2020-3-12", "2020-3-27", 1421.11, "San Diego, CA", "Murder Mystery"), ("Hyperrealism", "2020-1-2", "2020-2-1", 1234.22, "Tijuana, MX", "El Paso"), 
	   ("Still Life", "2020-4-1", "2020-4-20", 1420.99,"Bern, Switzerland", "The Cloud"),  ("Photorealism", "2020-7-2", "2020-12-25",2314.99, "Nairobi, Kenya", "The Gift");

Show Tables;
Select * from artist;
Select * from artshows;
Select * from customer;
Select * from artwork;
