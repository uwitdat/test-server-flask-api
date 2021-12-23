from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from testserver.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class UserService(Base):
    __tablename__ = 'user_service'

    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
