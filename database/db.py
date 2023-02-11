from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from models import Urls

Base = declarative_base()

engine = create_engine("sqlite:///database.sqlite3", echo=True)

Session = sessionmaker(bind=engine)
db_session = Session()
