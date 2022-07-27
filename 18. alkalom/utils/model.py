from sqlalchemy import Column, String, Integer, Sequence, Date
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

"""
car_name: Volvo S60
engine_type: benzin
color: white
year_of_manufacture: 01-01-2013
price: 5300000

"""

class YamlData(base):
    __tablename__ = 'yaml_data'

    id = Column(Integer, Sequence('seq_yaml_data'), primary_key=True )
    car_name = Column(String)
    engine_type = Column(String)
    color = Column(String)
    year_of_manufacture = Column(Date)
    price = Column(Integer)

    def __str__(self):
        return f"Car({self.car_name},\
             {self.engine_type}, \
             {self.color}, \
             {self.year_of_manufacture}, \
             {self.price})"