from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from testserver.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship


class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer(), primary_key=True)
    name = Column(String(25), nullable=False)
    description = Column(String(80), nullable=False)
    date_created = Column(DateTime(), default=datetime.utcnow)
    provider_id = Column(Integer(), ForeignKey('providers.id'))
    services = relationship(
        'UserService', cascade='all, delete-orphan', backref='service')


