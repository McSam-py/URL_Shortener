from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import Config

# from models import Urls

Base = declarative_base()
app_config = Config()

engine = create_engine(app_config.get_db_url(), echo=True)

Session = sessionmaker(bind=engine)
db_session = Session()
