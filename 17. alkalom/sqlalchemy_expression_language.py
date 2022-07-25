from sqlalchemy import create_engine, inspect
from sqlalchemy import Table, Column, String, MetaData

db = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/postgres")

meta = MetaData(db)

films_table = Table('films', meta,
                    Column('title', String),
                    Column('director', String),
                    Column('release_date', String))


insp = inspect(db)

"""
C - insert
R - select
U - update
D - delete

"""

with db.connect() as conn:

    if not insp.has_table(films_table):
        films_table.create()

    # insert data to table

    insert_statement = films_table.insert().values(title='Alien', director="Ridley scott", release_date='1979')
    insert_statement2 = films_table.insert().values(title='Alien2', director="Ridley scott", release_date='1979')
    insert_statement3 = films_table.insert().values(title='Alien3', director="Ridley scott", release_date='1979')

    conn.execute(insert_statement)
    conn.execute(insert_statement2)
    conn.execute(insert_statement3)


    # update data in table

    """
    update films set director = 'James Cameron'
        where title = 'Alien2'
    """

    update_statement = films_table.update().where(films_table.c.title=="Alien2").values(director = "James Cameron")

    conn.execute(update_statement)


    # delete

    delete_statement = films_table.delete().where(films_table.c.title=='Alien3')
    conn.execute(delete_statement)


    # select

    select_statement = films_table.select().where(films_table.c.title=="Alien")

    result_set = conn.execute(select_statement)

    for r in result_set:
        print(r)
