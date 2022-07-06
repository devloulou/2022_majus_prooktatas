select * from brand;
select * from cars;
select * from motor_type;

select osszeg - 4 from (
select sum(t.cnt_brand_id) as osszeg from
(select count(brand_id) as cnt_brand_id, brand_id, motor_type_id from cars
group by brand_id, motor_type_id) t
where t.cnt_brand_id > 1) t2;


/* with clause */
with base_data as (
select count(brand_id) as cnt_brand_id, brand_id, motor_type_id from cars
group by brand_id, motor_type_id
), agg_data as (
	select sum(cnt_brand_id) as osszeg from base_data
	where cnt_brand_id > 1
), test_data as (	
	select now()
)
select * from test_data

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

/*string műveletek*/
select
substring(c.color from 2 for 4),
substring(c.color from 2),
substring(c.color, 2, 4),
c.color
from cars c;

/*substring használata és konkatenálás*/
with test_data as (
select 'HU93116000060000000012345676' as iban ),
modif_data as (
select
substring(iban, 5, 8) as first_part,
substring(iban, 13, 8) as second_part,
substring(iban, 21) as third_part,
iban
from test_data)
select first_part || '-' || second_part || '-' || third_part  from modif_data;
-------------------------------------------------------------------------------------------
/*instr - position*/

with base_data as (
select 'valamilyen.elborult.2000@email.hu' as email )
, invest_data as (
select
position('@' in email) as pos,
email
from base_data
)
select
substring(email, 1, pos - 1) as eleje,
substring(email, pos + 1) as vege, 
email
email
from invest_data;


with base_data as (
select 'kkkbbbkkkkbbbfff' as szo),
modif_data as (
select
replace(szo, 'kkk', 't')
from base_data
)
select * from modif_data;
------------------------------------------------------------------
/*dátum függvények*/

with base_data as (select now() dat, '2022.04.06. 10:12:31' as dat2)
, modif_data as (
select
to_date(to_char(dat, 'YYYY'), 'YYYY'),
to_number(to_char(dat, 'YYYY'), '9G999g999'),
to_date(dat2, 'year'),
to_char(to_date(dat2, 'YYYY.MM.DD HH24:MI:SS'), 'WW'),
extract(minute from timestamp '2022.04.06. 10:12:31'),
dat + interval '-10 month',
date_trunc('year', dat)
from base_data
)
select * from modif_data
;


/*like -os keresés*/

select * from cars c
where 1 = 1
-- and c.color like '_iros'
--and c.color like '_iro_'
--and c.color like '_ir%'
--and c.color like '%r'
--and c.color like '%'
and to_char(c.manufactured_date, 'YYYY-MM-DD') like '%19%';


/*elágazás sql-ben: case when (if else)*/

select distinct c.color from cars c

select * from cars c;
select
case 
	when c.color = 'barna' then 1
	when c.color = 'zöld' then 2
	when c.color = 'piros' then 3
	else 4
	end as color_to_number,
	
case when c.color = 'barna' then 1
	 when c.color = 'zöld' then 2
	 else 
	 	case 
	 		when c.brand_id > 100 then 3
	 		when c.brand_id > 200 then 4
	 		else 5
	 	end
	 end as color_to_num,
c.color
from cars c;

select
row_number()over(order by c.max_speed desc) as rn,
rank()over(order by c.max_speed desc) as rank_num,
dense_rank()over(order by c.max_speed desc) as dense_num,
c.*
from cars c;

select
row_number()over(partition by c.brand_id order by c.max_speed desc),
rank()over(partition by c.brand_id order by c.max_speed desc),
dense_rank()over(partition by c.brand_id order by c.max_speed desc),
--sum(brand_id)over(partition by c.brand_id order by c.max_speed),
min(c.max_speed)over(partition by c.brand_id order by c.max_speed asc),
max(c.max_speed)over(partition by c.brand_id order by c.max_speed desc),
c.*
from cars c;





