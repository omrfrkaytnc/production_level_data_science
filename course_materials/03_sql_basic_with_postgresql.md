## Ders1:PostgreSQL Giriş

`sudo systemctl status postresql-10`

`psql -l` #Veri tabanlarını listeler

`psql -d traindb` #traindb veri tabanına bağlanır

`\q` #database'den çıkar

`psql -h localhost -p 5432 -d traindb -U train`

`\l` #\l: veri tabanlarını listeler.

`\c mlflow`

`\c traindb`

`create database test1;`

`psql -d traindb -U postgres`

`sudo -u postgres psql` #database'e bağlanırken yetkisi olan postgres user'ı ile bağlan

`create database test1;` #test1 veritabanı oluşturulur

`\l`

## Ders2:CSV Dosyasından Tablo Yapma

```
nano users.csv

id, name, age
1,Mehmet,39
2,Ayşe,33
3,Muhsin,21
4,Mehtap,29
```

`cat users.csv`

`psql -d traindb`

`create table users(id int, name varchar(20),age int);`
`\dt`

`psql -d traindb -c "\copy users FROM 'users.csv' DELIMITERS" ',' CSV HEADER;"`

`psql -d traindb -c "select * from users;"`

## Ders3:DBeaver SQL Editoru

##### Host: localhost
##### Databese: traindb
##### Username: train
##### Password: Ankara06

`select * from books;`

## Ders4:Ornek Tablolar Olusturma

```
create table public.orders(
order_id int primary key,
customer_id int,
employee_id int,
order_date date,
shipper_id int
);
```

```
insert into public.orders (order_id, customer_id, employee_id, order_date, shipper_id)
VALUES(10308, 2, 7, '1996-09-18', 3),
(10309, 37, 3, '1996-09-19', 1),
(10310, 77, 8, '1996-09-20', 2);
```

`select * from orders;`

```
create table public.customers(
customer_id serial primary key,
customer_name varchar,
contact_name varchar,
address varchar,
city varchar,
PostalCode varchar,
country varchar,
income float
);
```

```
insert into customers (customer_name, contact_name, address, city, postalcode, country, income)
values
('Alfreds Futterkiste', 'Maria Anders', 'Obere Str. 57', 'Berlin', '12209', 'Germany', 67470 ),  
('Ana Trujillo Emparedados y helados', 'Ana Trujillo', 'Avda. de la Constitución 2222', 'México D.F.', '05021', 'Mexico', 79210 ),  
('Antonio Moreno Taquería', 'Antonio Moreno', 'Mataderos 2312', 'México D.F.', '05023', 'Mexico', 45090 ),  
('Around the Horn', 'Thomas Hardy', '120 Hanover Sq.', 'London', 'WA1 1DP', 'UK', 64720 ),  
('Berglunds snabbköp', 'Christina Berglund', 'Berguvsvägen 8', 'Luleå', 'S-958 22', 'Sweden', 30150 ),  
('Blauer See Delikatessen', 'Hanna Moos', 'Forsterstr. 57', 'Mannheim', '68306', 'Germany', 16860 ),  
('Blondel père et fils', 'Frédérique Citeaux', '24, place Kléber', 'Strasbourg', '67000', 'France', 12090 ),  
('Bólido Comidas preparadas', 'Martín Sommer', 'C/ Araquil, 67', 'Madrid', '28023', 'Spain', 32150 ),  
('Bon app''', 'Laurence Lebihans', '12, rue des Bouchers', 'Marseille', '13008', 'France', 59430 ),  
('Bottom-Dollar Marketse', 'Elizabeth Lincoln', '23 Tsawassen Blvd.', 'Tsawassen', 'T2F 8M4', 'Canada', 67550 ),  
('B''s Beverages', 'Victoria Ashworth', 'Fauntleroy Circus', 'London', 'EC2 5NT', 'UK', 48080 ),  
('Cactus Comidas para llevar', 'Patricio Simpson', 'Cerrito 333', 'Buenos Aires', '1010', 'Argentina', 56070 ),  
('Centro comercial Moctezuma', 'Francisco Chang', 'Sierras de Granada 9993', 'México D.F.', '05022', 'Mexico', 90880 ),  
('Chop-suey Chinese', 'Yang Wang', 'Hauptstr. 29', 'Bern', '3012', 'Switzerland', 64840 ),  
('Comércio Mineiro', 'Pedro Afonso', 'Av. dos Lusíadas, 23', 'São Paulo', '05432-043', 'Brazil', 85250 ),  
('Consolidated Holdings', 'Elizabeth Brown', 'Berkeley Gardens 12 Brewery', 'London', 'WX1 6LT', 'UK', 38010 ),  
('Drachenblut Delikatessend', 'Sven Ottlieb', 'Walserweg 21', 'Aachen', '52066', 'Germany', 70310 ),  
('Du monde entier', 'Janine Labrune', '67, rue des Cinquante Otages', 'Nantes', '44000', 'France', 22640 ),  
('Eastern Connection', 'Ann Devon', '35 King George', 'London', 'WX3 6FW', 'UK', 31230 ),  
('Ernst Handel', 'Roland Mendel', 'Kirchgasse 6', 'Graz', '8010', 'Austria', 26520 ),  
('Familia Arquibaldo', 'Aria Cruz', 'Rua Orós, 92', 'São Paulo', '05442-030', 'Brazil', 49850 ),  
('FISSA Fabrica Inter. Salchichas S.A.', 'Diego Roel', 'C/ Moralzarzal, 86', 'Madrid', '28034', 'Spain', 12500 ),  
('Folies gourmandes', 'Martine Rancé', '184, chaussée de Tournai', 'Lille', '59000', 'France', 72700 ),  
('Folk och fä HB', 'Maria Larsson', 'Åkergatan 24', 'Bräcke', 'S-844 67', 'Sweden', 11450 ),  
('Frankenversand', 'Peter Franken', 'Berliner Platz 43', 'München', '80805', 'Germany', 12620 ),  
('France restauration', 'Carine Schmitt', '54, rue Royale', 'Nantes', '44000', 'France', 33650 ),  
('Franchi S.p.A.', 'Paolo Accorti', 'Via Monte Bianco 34', 'Torino', '10100', 'Italy', 31320 ),  
('Furia Bacalhau e Frutos do Mar', 'Lino Rodriguez', 'Jardim das rosas n. 32', 'Lisboa', '1675', 'Portugal', 81610 ),  
('Galería del gastrónomo', 'Eduardo Saavedra', 'Rambla de Cataluña, 23', 'Barcelona', '08022', 'Spain', 31090 ),  
('Godos Cocina Típica', 'José Pedro Freyre', 'C/ Romero, 33', 'Sevilla', '41101', 'Spain', 72330 ),  
('Gourmet Lanchonetes', 'André Fonseca', 'Av. Brasil, 442', 'Campinas', '04876-786', 'Brazil', 98690 ),  
('Great Lakes Food Market', 'Howard Snyder', '2732 Baker Blvd.', 'Eugene', '97403', 'USA', 62870 ),  
('GROSELLA-Restaurante', 'Manuel Pereira', '5ª Ave. Los Palos Grandes', 'Caracas', '1081', 'Venezuela', 87280 ),  
('Hanari Carnes', 'Mario Pontes', 'Rua do Paço, 67', 'Rio de Janeiro', '05454-876', 'Brazil', 98320 ),  
('HILARIÓN-Abastos', 'Carlos Hernández', 'Carrera 22 con Ave. Carlos Soublette #8-35', 'San Cristóbal', '5022', 'Venezuela', 90310 ),  
('Hungry Coyote Import Store', 'Yoshi Latimer', 'City Center Plaza 516 Main St.', 'Elgin', '97827', 'USA', 55320 ),  
('Hungry Owl All-Night Grocers', 'Patricia McKenna', '8 Johnstown Road', 'Cork', 'nan', 'Ireland', 75500 ),  
('Island Trading', 'Helen Bennett', 'Garden House Crowther Way', 'Cowes', 'PO31 7PJ', 'UK', 54220 ),  
('Königlich Essen', 'Philip Cramer', 'Maubelstr. 90', 'Brandenburg', '14776', 'Germany', 87980 ),  
('La corne d''abondance', 'Daniel Tonini', '67, avenue de l''Europe', 'Versailles', '78000', 'France', 28460 ),  
('La maison d''Asie', 'Annette Roulet', '1 rue Alsace-Lorraine', 'Toulouse', '31000', 'France', 65060 ),  
('Laughing Bacchus Wine Cellars', 'Yoshi Tannamuri', '1900 Oak St.', 'Vancouver', 'V3F 2K1', 'Canada', 72290 ),  
('Lazy K Kountry Store', 'John Steel', '12 Orchestra Terrace', 'Walla Walla', '99362', 'USA', 31860 ),  
('Lehmanns Marktstand', 'Renate Messner', 'Magazinweg 7', 'Frankfurt a.M.', '60528', 'Germany', 32480 ),  
('Let''s Stop N Shop', 'Jaime Yorres', '87 Polk St. Suite 5', 'San Francisco', '94117', 'USA', 35430 ),  
('LILA-Supermercado', 'Carlos González', 'Carrera 52 con Ave. Bolívar #65-98 Llano Largo', 'Barquisimeto', '3508', 'Venezuela', 63600 ),  
('LINO-Delicateses', 'Felipe Izquierdo', 'Ave. 5 de Mayo Porlamar', 'I. de Margarita', '4980', 'Venezuela', 69340 ),  
('Lonesome Pine Restaurant', 'Fran Wilson', '89 Chiaroscuro Rd.', 'Portland', '97219', 'USA', 38830 ),  
('Magazzini Alimentari Riuniti', 'Giovanni Rovelli', 'Via Ludovico il Moro 22', 'Bergamo', '24100', 'Italy', 17500 ),  
('Maison Dewey', 'Catherine Dewey', 'Rue Joseph-Bens 532', 'Bruxelles', 'B-1180', 'Belgium', 28960 ),  
('Mère Paillarde', 'Jean Fresnière', '43 rue St. Laurent', 'Montréal', 'H1J 1C3', 'Canada', 85550 ),  
('Morgenstern Gesundkost', 'Alexander Feuer', 'Heerstr. 22', 'Leipzig', '04179', 'Germany', 74480 ),  
('North/South', 'Simon Crowther', 'South House 300 Queensbridge', 'London', 'SW7 1RZ', 'UK', 85760 ),  
('Océano Atlántico Ltda.', 'Yvonne Moncada', 'Ing. Gustavo Moncada 8585 Piso 20-A', 'Buenos Aires', '1010', 'Argentina', 49510 ),  
('Old World Delicatessen', 'Rene Phillips', '2743 Bering St.', 'Anchorage', '99508', 'USA', 19360 ),  
('Ottilies Käseladen', 'Henriette Pfalzheim', 'Mehrheimerstr. 369', 'Köln', '50739', 'Germany', 38540 ),  
('Paris spécialités', 'Marie Bertrand', '265, boulevard Charonne', 'Paris', '75012', 'France', 16780 ),  
('Pericles Comidas clásicas', 'Guillermo Fernández', 'Calle Dr. Jorge Cash 321', 'México D.F.', '05033', 'Mexico', 97740 ),  
('Piccolo und mehr', 'Georg Pipps', 'Geislweg 14', 'Salzburg', '5020', 'Austria', 29240 ),  
('Princesa Isabel Vinhoss', 'Isabel de Castro', 'Estrada da saúde n. 58', 'Lisboa', '1756', 'Portugal', 48900 ),  
('Que Delícia', 'Bernardo Batista', 'Rua da Panificadora, 12', 'Rio de Janeiro', '02389-673', 'Brazil', 69160 ),  
('Queen Cozinha', 'Lúcia Carvalho', 'Alameda dos Canàrios, 891', 'São Paulo', '05487-020', 'Brazil', 92060 ),  
('QUICK-Stop', 'Horst Kloss', 'Taucherstraße 10', 'Cunewalde', '01307', 'Germany', 47990 ),  
('Rancho grande', 'Sergio Gutiérrez', 'Av. del Libertador 900', 'Buenos Aires', '1010', 'Argentina', 66600 ),  
('Rattlesnake Canyon Grocery', 'Paula Wilson', '2817 Milton Dr.', 'Albuquerque', '87110', 'USA', 93560 ),  
('Reggiani Caseifici', 'Maurizio Moroni', 'Strada Provinciale 124', 'Reggio Emilia', '42100', 'Italy', 18980 ),  
('Ricardo Adocicados', 'Janete Limeira', 'Av. Copacabana, 267', 'Rio de Janeiro', '02389-890', 'Brazil', 61150 ),  
('Richter Supermarkt', 'Michael Holz', 'Grenzacherweg 237', 'Genève', '1203', 'Switzerland', 44520 ),  
('Romero y tomillo', 'Alejandra Camino', 'Gran Vía, 1', 'Madrid', '28001', 'Spain', 87420 ),  
('Santé Gourmet', 'Jonas Bergulfsen', 'Erling Skakkes gate 78', 'Stavern', '4110', 'Norway', 19350 ),  
('Save-a-lot Markets', 'Jose Pavarotti', '187 Suffolk Ln.', 'Boise', '83720', 'USA', 10690 ),  
('Seven Seas Imports', 'Hari Kumar', '90 Wadhurst Rd.', 'London', 'OX15 4NB', 'UK', 23770 ),  
('Simons bistro', 'Jytte Petersen', 'Vinbæltet 34', 'København', '1734', 'Denmark', 18800 ),  
('Spécialités du monde', 'Dominique Perrier', '25, rue Lauriston', 'Paris', '75016', 'France', 68760 ),  
('Split Rail Beer & Ale', 'Art Braunschweiger', 'P.O. Box 555', 'Lander', '82520', 'USA', 55490 ),  
('Suprêmes délices', 'Pascale Cartrain', 'Boulevard Tirou, 255', 'Charleroi', 'B-6000', 'Belgium', 70770 ),  
('The Big Cheese', 'Liz Nixon', '89 Jefferson Way Suite 2', 'Portland', '97201', 'USA', 21910 ),  
('The Cracker Box', 'Liu Wong', '55 Grizzly Peak Rd.', 'Butte', '59801', 'USA', 68940 ),  
('Toms Spezialitäten', 'Karin Josephs', 'Luisenstr. 48', 'Münster', '44087', 'Germany', 62210 ),  
('Tortuga Restaurante', 'Miguel Angel Paolino', 'Avda. Azteca 123', 'México D.F.', '05033', 'Mexico', 78320 ),  
('Tradição Hipermercados', 'Anabela Domingues', 'Av. Inês de Castro, 414', 'São Paulo', '05634-030', 'Brazil', 91420 ),  
('Trail''s Head Gourmet Provisioners', 'Helvetius Nagy', '722 DaVinci Blvd.', 'Kirkland', '98034', 'USA', 75150 ),  
('Vaffeljernet', 'Palle Ibsen', 'Smagsløget 45', 'Århus', '8200', 'Denmark', 79360 ),  
('Victuailles en stock', 'Mary Saveley', '2, rue du Commerce', 'Lyon', '69004', 'France', 26450 ),  
('Vins et alcools Chevalier', 'Paul Henriot', '59 rue de l''Abbaye', 'Reims', '51100', 'France', 49360 ),  
('Die Wandernde Kuh', 'Rita Müller', 'Adenauerallee 900', 'Stuttgart', '70563', 'Germany', 26480 ),  
('Wartian Herkku', 'Pirkko Koskitalo', 'Torikatu 38', 'Oulu', '90110', 'Finland', 22060 ),  
('Wellington Importadora', 'Paula Parente', 'Rua do Mercado, 12', 'Resende', '08737-363', 'Brazil', 83880 ),  
('White Clover Markets', 'Karl Jablonski', '305 - 14th Ave. S. Suite 3B', 'Seattle', '98128', 'USA', 58610 ),  
('Wilman Kala', 'Matti Karttunen', 'Keskuskatu 45', 'Helsinki', '21240', 'Finland', 26100 ),  
('Wolski', 'Zbyszek', 'ul. Filtrowa 68', 'Walla', '01-012', 'Poland', 31670 );
```

`select * from customers limit 5;`

## Ders5:Select, Alias ve Distinct

`select customer_id, customer_name, income from customers limit 5;`

`select customer_id as id, customer_name as name, income from customers limit 5;`

`select distinct country from customers ;`

## Ders6:Where, And, Or, Not, Like, In ve Between

```
select * from customers
where Country='Germany'
limit 5;
```

```
select * from customers
where country = 'Germany' and city = 'Berlin'
limit 5;
```

```
select * from customers
where country = 'Germany' or city = 'Berlin'
limit 5;
```

```
select * from customers
where not country='Germany'
limit 5;
```

```
select * from customers 
where (country = 'France' or country = 'Spain') and not city = 'Madrid' ;
```

```
select * from customers 
where contact_name like 'A%';
```

```
select * from customers 
where contact_name like '%Dom%';
```

```
select  customer_name, country from customers 
where country in ('France', 'Spain', 'UK');
```

```
select * from customers 
where income between 10000 and 20000;
```

## Ders7:Order by

```
select * from customers 
order by country;
```

```
select * from customers 
order by country desc;
```

```
select * from customers 
order by country, city;
```

## Ders8:Insert Into ve Null

```
INSERT INTO customers (customer_name, contact_name, address, city, postalcode, country, income)
VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway', 38500);
```

```
INSERT INTO customers (customer_name, city, country)
VALUES ('Cardinal X', 'Stavanger', 'Norway');
```

`select * from customers where country = 'Norway';`

`select * from customers where income is null and country = 'Norway';`

`select * from customers where income is not null and country = 'Norway';`

## Ders9:Update

`select * from customers where customer_name = 'Santé Gourmet';`

`select * from customers where customer_id = 70;`

```
update customers set income = 54000 
where customer_id = 70;
```

`select * from customers where country = 'Italy';`

`select customer_name, country, income from customers where country = 'Italy';`

`update customers set income = income + 5000 where country = 'Italy';`

## Ders10:Delete

`select * from customers where customer_id = 70;`

`delete from customers where customer_id = 70;`

`select * from customers where country = 'Italy';`

`delete from customers where country = 'Italy';`

## Ders11:Min, Max, Avg, Count ve Sum

`select * from customers limit 5;`

```
select min(income) as min_income, max(income) as max_income 
from customers limit 5;
```

`select count(1), sum(income), avg(income) from customers ;`

## Ders12:Join

`select * from orders;`

`select * from customers limit 3;`

```
select * from
orders o 
join customers c
on o.customer_id = c. customer_id;
```

```
select o.customer_id, o.order_date, c.customer_id,  c.customer_name from
orders o
join customers c 
on o.customer_id = c.customer_id;
```

`delete from customers where customer_id = 77;`

```
select o.customer_id, o.order_date, c.customer_id,  c.customer_name from
orders o
left join customers c 
on o.customer_id = c.customer_id;
```

```
select o.customer_id, o.order_date, c.customer_id,  c.customer_name from
orders o
right join customers c 
on o.customer_id = c.customer_id;
```

```
select o.customer_id, o.order_date, c.customer_id,  c.customer_name from
orders o
full join customers c 
on o.customer_id = c.customer_id;
```

## Ders13:Union
##### Union verileri birleştirir ve tekrarlanan satırlara izin vermez

```
select * from orders 
union
select * from orders;
```

```
select * from orders 
union all
select * from orders;
```

## Ders14:Group by ve Having

`select * from customers limit 5;`

```
select country, count(customer_id)
from customers 
group by country;
```

```
select country, avg(income)
from customers 
group by country;
```

```
select country, count(customer_id), avg(income)
from customers 
group by country;
```

```
select country, count(customer_id), avg(income)
from customers 
group by country
having country in ('USA', 'Sweden', 'UK')
order by avg;
```

## Ders15:Sub Query

```
select * from customers 
where income = (select max(income) from customers where country = 'USA');
```

## Ders16:Select Into ve Insert Into Select

`select count(1) from customers c;`

```
select * into customers_gt_50k
from customers c 
where income > 50000;
```

`select * from customers_gt_50k limit 5;`

```
insert into customers_gt_50k
select * from customers c
where income between 40000 and 50000;
```

`select count(1) from customers_gt_50k;`

## Ders17:Case

`select * from customers c ;`

```
Select customer_name, income,
case
    when income < 30000 then 'Low income'
    when income between 30000 and 60000 then 'Middle income'
    else 'High income'
end as income_class
from customers c;
```
