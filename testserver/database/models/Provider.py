from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from testserver.database import Base
from datetime import datetime
from testserver.database import db_session


class Provider(Base):
    __tablename__ = 'providers'

    id = Column(Integer(), primary_key=True)
    name = Column(String(25), nullable=False, unique=True)
    description = Column(String(80), nullable=False)
    date_created = Column(DateTime(), default=datetime.utcnow)
    services = relationship(
        'Service', cascade='all, delete-orphan', backref='provided_by')
