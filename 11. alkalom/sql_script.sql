/*SQL*/

/*minden adatot visszaad a táblából*/
-- * asterix karakter - minden mezőt 
select * from brand;

select brand_name from brand;

select brand_name, id from brand;

/*SQL filterezés - szűrés*/
-- where

select * from brand
where id > 200
or 400 > id;

select * from brand
where brand_name = 'Volvo';

select * from brand
where brand_name in ('Volvo', 'BMW');

select * from brand
order by brand_name desc; --asc

select * from brand
order by 2 asc;

select * from brand
order by id desc, brand_name asc;

/*group by - csoportositás*/
/*aggregáló függvények: sum, count, min, max, avg*/
select count(brand_id), brand_id, motor_type_id from cars
group by brand_id, motor_type_id;

select * from cars;


/*kiértékelési sorrend
 * 
 * from cars
 * where brand_id != 100
 * group by brand_id, motor_type_id
 * having count(brand_id) > 1
 * select count(brand_id), brand_id, motor_type_id
 * order by brand_id desc
 * limit 3
 * 
 * először a táblából eléri az adatot
 * majd filterezi - szűri az adatot
 * ha van group by akkor megcsinálja a csoportositást
 * ha van having, akkor a csoportositott adaton elvégzi a havingnél megadott vizsgálatot
 * majd a mezőket a select résznél megadott formában előállitja
 * ha van order by akkor az ott megadott rendezésnek megfelelően rendezi a rekordokat
 * ha van limit , akkor annak megfelelően adja vissza a rekordok számát
 * */
select count(brand_id), brand_id, motor_type_id
from cars
where brand_id != 100
group by brand_id, motor_type_id
having count(brand_id) > 1
order by brand_id desc
limit 3;
-- limit

/*hogyan kapcsolunk össze táblákat*/

--- miért van erre szükség?
--- joinok


select * from cars;
select * from brand;
select * from motor_type mt;

select count(brand_id) as cnt_brand_id, brand_id, motor_type_id from cars
group by brand_id, motor_type_id;


select /*count(c.brand_id) as cnt_brand_id,*/ b.brand_name, mt.type_name from cars c
inner join brand b on c.brand_id = b.id 
right join motor_type mt on c.motor_type_id  = mt.id
where brand_name is null
--group by b.brand_name, mt.type_name 
;

select * from motor_type mt
left join cars c on mt.id  = c.motor_type_id ;

insert into motor_type (id, type_name) values (4, 'hybrid');


select c.brand_id, c.color, c.motor_type_id  from cars c;

/*Descartes szorzat*/
select * from cars c, brand b;

/*subselectek*/

select sum(t.cnt_brand_id)  from
(select count(brand_id) as cnt_brand_id, brand_id, motor_type_id from cars
group by brand_id, motor_type_id) t
where t.cnt_brand_id > 1;

select sum(cnt_brand_id)  from
(select count(brand_id) as cnt_brand_id from cars
group by brand_id, motor_type_id
having count(brand_id) > 1) t


/*
 * string függvényt: instr, replace, substr
 * dátum függvényt: to_date, extract, add_months
 * aggregáló függvényt: min, max, avg, sum, count
 * with clause
 * case when
 * coalesce
 * trim
 * like
 * 
 * window function
 * */

