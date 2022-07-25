"""
ORM - Object Relation Mapping

"""

from matplotlib.pyplot import title
from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/postgres")

base = declarative_base()

# tábla class definíciónk - model
class FilmTable(base):
    __tablename__ = "film_table"

    title = Column(String, primary_key=True)
    director = Column(String)
    year = Column(String)


Session = sessionmaker(db)
session = Session()

base.metadata.drop_all(db)
base.metadata.create_all(db)


# Create - Insert
alien = FilmTable(title="Alien", director='Ridley Scott', year='1979')
predator = FilmTable(title="predator", director='fogalmam sincs', year='1987')

session.add_all([alien, predator])
session.commit()

# Read - Select
"""
Serializáció - Deserializáció

"""

films = session.query(FilmTable).filter(FilmTable.title=='Alien')
for film in films:
    print(film.title, film.director, film.year)
    # Update - Update

    film.title = "Aliens"
    film.director = 'James Cameron'
    film.year = "1986"

    session.commit()

from sqlalchemy import func
sql_stat = session.query(func.count(FilmTable.title))

"""
select count(title) from film_table;
"""

for item in sql_stat:
    print(item)


# Delete - Delete
#session.delete(alien)
session.query(FilmTable).filter(FilmTable.title=='predator').delete()

session.commit()