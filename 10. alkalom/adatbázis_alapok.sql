/*
 * Mi az adatbázis? Mi az a relációs adatbázis?
 * Relációs adatbázis  RDBMS - Relational DataBase Management System
 * 
 * Mi az a reláció?
 * Reláció a kapcsolatot jelenti az adatok között 
 * 
 * Táblák-ban tároljuk - relációk
 * sor alapú - row-based adatbázisokról fogunk beszélni
 *  
 *  * 
 * */

-- hozzá kell kapcsolódnunk: connection
-- ahhoz, hogy SQL műveleteket tudjunk futtatni / session-öket létrehoznunk
-- le kell zárnom a módositást: commit - rollback ---> tranzakció kezelés

-- első eltérés a különböző RDBMS -ek között: nem minden adatbázisban kell minden SQL utasitást lezárni

-- ez bizonyos adatbázisoknál vannak tranzakció köteles utasitások SQL-ben, meg vannak
-- azok, amelyek nem igényelnek tranzakciót: 
-- pl. Oracle - tranzakció köteles lesz: update, delete, insert


/*
 * tables (reláció): az adatokat tároljuk benne
 * view (nézetek): logikai objektumok, a táblákban lévő adatok egyfajta nézete
 * --materialized view - fizikai objektumok, hasonló mint a view
 * indexes - táblákhoz tartozó indexek -> perfomanciát elősegitő objektumok
 * --functions - postgresql oldalon lévő function
 * sequences (szekvencia) - egyedi azonositót generáljunk - auto incement számokat
 * 
 * */

/*
 * SQL - Stuctured Query Languge
 * 
 * DDL - Data Definition Language
 * create, drop, alter, truncate, comment, rename
 * 
 * DML - Data Manipulation Language
 * insert, update, delete, lock, call, explain plan
 * 
 * DCL - Data Control Language
 * grant, revoke
 * 
 * DQL - Data Query Langue
 * select * 
 * */

/*adatmodellezés - 3rd normal form*/
create table first_table (
col_1 integer,
col_2 text,
col_3 date,
col_4 integer
);


select * from first_table ft ;

insert into first_table (col_1, col_2, col_3, col_4) values (1, 'Alma', now(), 10);


--------------------------------------------------------------
drop table motor_type;

create table motor_type (
id integer primary key,
type_name text
);

drop table brand;
create table brand (
id integer primary key,
brand_name text
);

truncate table cars;
drop table cars;
create table cars (
brand_id integer,
color text,
motor_type_id integer,
ccm numeric,
max_speed integer,
manufactured_date date,
CONSTRAINT fk_brand_id
      FOREIGN KEY(brand_id) 
	  REFERENCES brand(id),
CONSTRAINT fk_motor_type_id
      FOREIGN KEY(motor_type_id) 
	  REFERENCES motor_type(id)
);


select * from motor_type;
select * from brand;
select * from cars;

insert into motor_type (id, type_name) values (1, 'benzin');
insert into motor_type (id, type_name) values (2, 'diesel');
insert into motor_type (id, type_name) values (3, 'electric');
insert into motor_type (id, type_name) values (4, 'hybrid');

insert into brand (id, brand_name) values (100,'Volvo');
insert into brand (id, brand_name) values (200,'BMW');
insert into brand (id, brand_name) values (300,'Opel');
insert into brand (id, brand_name) values (400,'Reanult');
insert into brand (id, brand_name) values (500,'Tesla');
insert into brand (id, brand_name) values (600,'Trabant');


delete from motor_type where id = 4;

insert into cars (brand_id, color, motor_type_id, ccm, max_speed, manufactured_date) values
(100,'fehér',1,1.6, 180,to_date('2008', 'YYYY'));
insert into cars (brand_id, color, motor_type_id, ccm, max_speed, manufactured_date) values
(200,'kék',2,2.4,220,to_date('2012', 'YYYY'));
insert into cars (brand_id, color, motor_type_id, ccm, max_speed, manufactured_date) values
(300,'fehér',1,1.4,150,to_date('2005', 'YYYY'));
insert into cars (brand_id, color, motor_type_id, ccm, max_speed, manufactured_date) values
(400,'piros',2,1.8,180,to_date('2006', 'YYYY'));
insert into cars (brand_id, color, motor_type_id, ccm, max_speed, manufactured_date) values
(500,'fekete',3,null,230,to_date('2015', 'YYYY'));
insert into cars (brand_id, color, motor_type_id, ccm, max_speed, manufactured_date) values
(600,'kék',1,1.1,100,to_date('1989', 'YYYY'));


insert into cars (brand_id, motor_type_id) values (700, 5);


select to_date('2008', 'YYYY')




/*
 * reláció kialakitása táblák között:
 * 
 * Szülő - gyermek kapcsolat
 * 
 * a szülő táblában van elsődleges kulcs - primary key: csak 1 db lehet 1 táblán, egyedi értékkel kell rendelkeznie és az érték nem lehet null
 * a gyermek tábla abban pedig idegen kulcs hivatkozás van, a szülő tábla primary kulcsára
 * 
 * 
 * */














