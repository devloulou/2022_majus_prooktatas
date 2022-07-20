"""
1. kérdés: írj egy pár gondolatot a primary key-ről. Mi az a primary key, mire szolgál?

A primary key egy táblának a sorát egyértelmeűen azonosító adat. A primary key értéke egyedi. (Nem lehet null az értéke.)
A primary key szükséges ahhoz, hogy szülő - gyermek kapcsolatot alakítsunk ki táblák között.

2. kérdés: írj egy pár gondolatot a foreign key-ről. Mi az a foreing key, mire szolgál?

Idegen kulcs. A szülő - gyermek kapcsolatnál a gyermek táblában helyezkedik el.
Az idegen nem lehet olyan adat, ami nem szerepel a szülő táblában. A foreing key kapcsolat
biztosítja a rekordok közötti konzistens állapotot. 

3. kérdés: mit csinál a group by utasítás az SQL nyelvben?

A group by utasítással csoportosítani tudjuk az adatokat, olyan csoportokra, amely mezőket felsorolunk
a group by kifejezés után.
Erre akkor van szükség, amikor olyan lekérdezéseket csinálunk, ahol aggregációt használunk (min, max, avg, count, sum)
és szeretnénk egyéb információt megjeleníteni, és ez az egyéb információ fogja meghatározni a csoportokat.

4. kérdés: mi a különbség az inner és left join között?
Inner join: a táblák közös rekodjait adja vissza
Left join:  a bal tábla összes adatát, jobb táblából pedig a közös rekordokat

5. kérdés: írj egy pár gondolatot a tranzaikcióról. Mi a tranzakció? 
Mi történik, ha nem zárom le a tranzakciót?

Tranzakciót = commit / rollback
Adatbázis függő: minden olyan utasítás, ahol létrehozok objektumot (create table, create sequence stb.), 
törlök objektumot (drop table, drop sequence stb.)
Adatot hozok létre (insert into table, create table tabla_nev as (select * from valamilyen_tabla))
Adatot módosítok (delete from, update table)
utasítások tranzakciónak minősülnek.

grant, revoke, truncate, select bizonyos adatbázokban commit / rollback köteles, bizonyos adatbázisokban meg nem.

adatbázisban történő egy vagy több módosítás amit commit-tal "elmentek" vagy "rollbackkel" visszagörgetek azaz
" meg nem történtté teszek.
Ha nem zárom le a tranzakciót akkor nem lépnek életbe a változtatások globálisan.


"""

# Az alábbi program működése hibás.
# Az eredeti feladat, amit szeretnénk elvégezni, hogy töröljük a listából
# azokat az elemeket, amelyek 1-nél többször szerepelnek:

# output a helyes futás után: [1, 2, 4, 6]

my_list = [1, 2, 3, 3, 4, 5, 5, 6]

def extend_list():
    new_list = []
    for item in my_list:
        if my_list.count(item) == 1:
            new_list.append(item)

    return new_list

new_list = extend_list()

print(new_list)
