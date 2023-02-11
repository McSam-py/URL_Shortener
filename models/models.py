from sqlalchemy import Column, Integer, String, DateTime
from database import Base, engine
from datetime import datetime


class Urls(Base):
    __tablename__ = "urls"
    _id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(String, nullable=False)
    # user_session = Column(String, nullable=False)
    target_url = Column(String, nullable=True)
    link_created = Column(String, nullable=False)
    time_created = Column(DateTime, nullable=True, default=datetime.utcnow)

    def __init__(self, user_id, target_url, link_created):
        self.user_id = user_id
        self.target_url = target_url
        # self.shortened_url = shortened_url
        # self.user_session = user_session
        self.link_created = link_created


Base.metadata.create_all(bind=engine)
