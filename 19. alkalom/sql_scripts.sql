/*
 * 
 * 1. a cégnél következő pozíciókban dolgoznak emberek:
    - vezető fejlesztő
    - fejlesztő
    - gyakornok
    - CEO
    - hr business partner

2. a dolgozókról a következő információkat tároljuk le:
    - mikor kezdett a cégnél
    - mennyi a fizetése
    - milyen munkakörben dolgozik

3. a pozíciókkal kapcsolatos információk:
    - minimum és maximum fizetési sáv megadása
 * 
 * */
--------------------------------------------------------------------------------------
/*
 * OLTP: Online Transactional Processing 
 * netbank, webshop, akármilyen fizetési rendszer, főkönyvi rendszer, 
 * minden olyan fejlesztés
 * ahol a cél 1 ügyfélhez tartozó adat létrehozás, módositás, törlés: (általában a web applikációk)
 * -> kevés adat használatára
 * -> általában az adat aktuális állapotát tartalmazza
 * 
 * 
 * OLAP: Online Analitical Processing
 * Adattárház, Data Lake, Lakehouse
 * Elemzésre, riportlására és előrejelzésre -> 
 * -> nagy adat elemzésre, aggregációk futtatására
 * Business Intelligence osztályokon lévő üzleti folyamatok
 * -> idősorosan (általában) tartalmazza az elvégzett módositásokat
 * */

/*adatbázis adat hisztorizálás*/

create table positions (
position_id serial primary key,
min_salary integer,
max_salary integer,
position_name text
);

create table position_hist (
position_hist_id serial primary key,
modification_date date default now(),
position_id integer,
min_salary integer, 
max_salary integer,
CONSTRAINT fk_position_id
      FOREIGN KEY(position_id) 
	  REFERENCES positions(position_id)
);

create table employees (
employee_id serial primary key,
start_date date,
salary integer,
position_id integer,
CONSTRAINT fk_position_id_emp
      FOREIGN KEY(position_id) 
	  REFERENCES positions(position_id)
);

/*
 *  - vezető fejlesztő
    - fejlesztő
    - gyakornok
    - CEO
    - hr business partner
 * 
 * */

insert into positions (position_name, min_salary, max_salary) values 
('Vezető Fejlesztő', 1500000, 2500000);
insert into positions (position_name, min_salary, max_salary) values 
('Fejlesztő', 750000, 1200000);
insert into positions (position_name, min_salary, max_salary) values 
('Gyakornok', 130000, 200000);
insert into positions (position_name, min_salary, max_salary) values 
('CEO', 3500000, 5500000);
insert into positions (position_name, min_salary, max_salary) values 
('Hr Business Partner', 550000, 850000);

