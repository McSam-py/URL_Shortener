from sqlalchemy import Column, Integer, String, DateTime
from database.db import Base


class Urls(Base):
    __tablename__ = 'urls'
    _id = Column(Integer, primary_key=True)
    target_url = Column(String, nullable=True)
    linked_created = Column(String, nullable=False)
    time_created = Column(DateTime, nullable=False)

    def __init__(self, target_url, shortened_url):
        self.target_url = target_url
        self.shortened_url = shortened_url
