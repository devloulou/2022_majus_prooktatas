import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

from config import POSTGRES_URI

engine = sqlalchemy.create_engine(POSTGRES_URI, pool_pre_ping=True)
Session = sessionmaker(bind=engine)

# these two lines perform the "database reflection" to analyze tables and relationships
Base = automap_base()
Base.prepare(engine, reflect=True)

# there are many tables in the database but I want `products` and `categories`
# only so I can leave others out
Positions = Base.classes.positions
Employees = Base.classes.employees


session = Session()

for item in session.query(Positions.position_id, Positions.min_salary, Positions.max_salary, Positions.position_name):
    print(item)
