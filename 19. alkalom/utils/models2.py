from functools import wraps

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

    @classmethod
    def historization(cls, func):
        @wraps(func)
        def make_history(*args, **kwargs):
            retval = func(*args, **kwargs)

            obj = retval['obj']
            history_record = obj.history_table(**retval['data'])
            obj.session.add(history_record)
            obj.session.commit()
            
            return retval
        return make_history


class PositionsModel(SQLBaseClass):
    "class variable"
    test_var = "Hello there"
    def __init__(self):
        super().__init__()
        self.table = self.Base.classes.positions
        self.history_table = self.Base.classes.position_hist

    def get_data(self):        
        for item in self.session.query(self.table.position_id, self.table.min_salary, self.table.max_salary, self.table.position_name):
            print(item)

    @SQLBaseClass.historization
    def modify_data(self, filter_col, filter_val, change_col, change_val):
        """ update tabla_neve set mezo = éretek where mezo = kapott_ertek  """
        record = {"obj": self, "data": {}}
        try:
            obj = self.session.query(self.table).filter(filter_col==filter_val).all()
            
            record['data']['position_id'] = obj[0].position_id
            record['data']['min_salary'] = obj[0].min_salary
            record['data']['max_salary'] = obj[0].max_salary
            record['data']['position_name'] = obj[0].position_name

            # hist_rec = self.history_table(**record)
            # self.session.add(hist_rec)

            self.session.query(self.table).filter(filter_col==filter_val).update({change_col:change_val}, synchronize_session = False)
            #temp = self.session.query(self.table).filter(eval(f"self.table.{filter_col}")==filter_val)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(e)

        return record


class EmployeesModel(SQLBaseClass):
    "class variable"
    test_var = "Hello there"
    def __init__(self):
        super().__init__()
        self.table = self.Base.classes.employees
        self.history_table = self.Base.classes.employees_hist

    def get_data(self):        
        for item in self.session.query(self.table.employee_id, self.table.start_date, self.table.salary, self.table.position_id, self.table.employee_name):
            print(item)

    @SQLBaseClass.historization
    def modify_data(self, filter_col, filter_val, change_col, change_val):
        """ update tabla_neve set mezo = éretek where mezo = kapott_ertek  """
        record = {"obj": self, "data": {}}
        try:
            obj = self.session.query(self.table).filter(filter_col==filter_val).all()
            
            record['data']['employee_id'] = obj[0].employee_id
            record['data']['start_date'] = obj[0].start_date
            record['data']['salary'] = obj[0].salary
            record['data']['position_id'] = obj[0].position_id
            record['data']['employee_name'] = obj[0].employee_name

            # hist_rec = self.history_table(**record)
            # self.session.add(hist_rec)

            self.session.query(self.table).filter(filter_col==filter_val).update({change_col:change_val}, synchronize_session = False)
            #temp = self.session.query(self.table).filter(eval(f"self.table.{filter_col}")==filter_val)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(e)

        return record

    def add_employee(self, start_date, salary, position_id, employee_name):
        try:
            record = self.table(start_date=start_date, salary=salary, position_id=position_id, employee_name=employee_name)
            self.session.add(record)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(e)


if __name__ == '__main__':
    import datetime
    """ létrehozunk egy PositionsModel instance-t"""
    positions = PositionsModel()

    print("---------------------")
    #positions.get_data()

    #temp = positions.modify_data(positions.table.position_name, "Hr Business Partner", positions.table.min_salary, 750_000)
    #positions.modify_data('min_salary', 550_000, None, None)

    employee = EmployeesModel()

    #employee.add_employee(start_date=datetime.datetime(2022, 7, 30), salary=1150_000, position_id=27, employee_name="John McLane")
    
    employee.modify_data(employee.table.employee_name, 'John Wick', employee.table.salary, 1_200_000)