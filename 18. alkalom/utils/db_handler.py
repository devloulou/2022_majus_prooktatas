from datetime import datetime
from contextlib import contextmanager

import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URI, file_path
from model import YamlData, base

engine = create_engine(DATABASE_URI, echo=True)

"""
@contextmanager
def some_generator(<arguments>):
    <setup> 
    try:
        yield <value>
    finally:
        <cleanup>
"""
# session.query(FilmTable).filter(FilmTable.title=='Alien')

# with session_handler() as conn:
#   conn.query()
#   conn.valami

#print

@contextmanager
def session_handler():
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

# sohasem csinálunk ilyet production ready rendszerben
def recreate_database():
    base.metadata.drop_all(engine)
    base.metadata.create_all(engine)


def etl_for_yaml():
    with session_handler() as conn:
        for data in yaml.safe_load_all(open(file_path)):
            data['year_of_manufacture'] = datetime.strptime(data['year_of_manufacture'], '%m-%d-%Y')
            car = YamlData(**data)
            conn.add(car)

if __name__ == '__main__':
    recreate_database()
    etl_for_yaml()
    # from sqlalchemy.sql import text
    # with session_handler() as conn:
    #     for data in conn.query(text("now()")):
    #         print(data)