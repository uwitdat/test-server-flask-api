from sqlalchemy import Column, String, Integer, DateTime
from testserver.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    name = Column(String(25), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True)
    date_created = Column(DateTime(), default=datetime.utcnow)
    services = relationship(
        'UserService', cascade='all, delete-orphan', backref='used_by')
