import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

from config import POSTGRES_URI

"""
self -> az objektum belsejében lévő attributumokat tudjuk használni
ahol a self szó szerepel: függvények, változók stb. azok instance változók / attribútumok
"""
"""
class változók / attributumok

static attrtibutumok
"""

class SQLBaseClass:
    def __init__(self):
        self.engine = sqlalchemy.create_engine(POSTGRES_URI, pool_pre_ping=True)
        self.session = self.create_session()
        self.Base = self.create_base_object()        

    def create_session(self):
        fnc = sessionmaker(bind=self.engine)
        return fnc()
    
    def create_base_object(self):
        automap = automap_base()
        automap.prepare(self.engine, reflect=True)

        return automap

    def exl_func(self):
        print(self.add_numbers(1,2))


    @staticmethod
    def add_numbers(a, b):
        return a + b

    @classmethod
    def my_firts_cls_method(cls):
        pass

class PositionsModel(SQLBaseClass):
    "class variable"
    test_var = "Hello there"
    def __init__(self):
        super().__init__()
        self.Positions = self.Base.classes.positions

    def get_data(self):        
        for item in self.session.query(self.Positions.position_id, self.Positions.min_salary, self.Positions.max_salary, self.Positions.position_name):
            print(item)

    def delete_data(self, id):
        try:
            temp = self.session.query(self.Positions).filter(self.Positions.position_id==id).all()
            self.session.query(self.Positions).filter(self.Positions.position_id==id).delete(synchronize_session='evaluate')
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            return

        return {
            'position_id': temp[0].position_id,
            'min_salary': temp[0].min_salary,
            'max_salary': temp[0].max_salary,
            'position_name': temp[0].position_name
        }

    @classmethod
    def test_method(cls):
        print(cls.test_var)


if __name__ == '__main__':
    """ létrehozunk egy PositionsModel instance-t"""
    positions = PositionsModel()

    positions.exl_func()
    #temp = positions.delete_data(9)

    

    #print(temp)
    print("---------------------")
    positions.get_data()


    #test = SQLBaseClass()
    # Positions = test.Base.classes.positions

    # for item in test.session.query(Positions.position_id, Positions.min_salary, Positions.max_salary, Positions.position_name):
    #     print(item)