from sqlalchemy.orm import sessionmaker
from model_state import State, Base 
from sqlalchemy import create_engine
from sys import argv

mysql_username = argv[1]
mysql_password = argv[2]
mysql_database = argv[3]

path = "mysql+mysqldb://{}:{}@localhost/{}".format(mysql_username, mysql_password, mysql_database)

database = create_engine(path)
Session = sessionmaker(bind=database)
session = Session()


states = session.query(State).all()


for state in states:
    print("{}: {}".format(state.id,state.name))