"""
psycopg2 - driver: létrehoz egy kapcsolatot az adatbázishoz és raw (natív sql pl: select * from) sql utasítákat tudunk futtatni

sqlalchemy:
    1. driver
    2. abstract réteget, ahol a táblálat le tudjuk képezni, expression language
    3. ORM - Object Relation Mapping

"""

from sqlalchemy import create_engine

# kapcsolatot kell létrehozni

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/postgres")

engine.execute("create table if not exists movies (title text, director text, release_date text) ")
engine.execute("insert into movies (title, director, release_date) values ('Alien', 'Ridley Scott', '1979')")

class Test:
    def __init__(self, title, director, release_date):
        self.title = title
        self.director = director
        self.release_date = release_date

test = Test(title='Prey', director='Fogalmam sincs', release_date='2022')

engine.execute("truncate table movies")

engine.execute(f"insert into movies (title, director, release_date) values ('{test.title}', '{test.director}', '{test.release_date}')")

engine.execute("insert into movies (title, director, release_date) values (%s, %s, %s)", [(test.title, test.director, test.release_date), (test.title, test.director, test.release_date)])

result_set = engine.execute("select * from movies")

for r in result_set:
    print(r)