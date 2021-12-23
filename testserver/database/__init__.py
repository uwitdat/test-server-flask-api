from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from testserver.database.models.Base import Base
from sqlalchemy.ext.declarative import declarative_base

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def set_db_connection():
    connection_string = 'sqlite:///' + os.path.join(BASE_DIR, 'testserver.db')
    return connection_string


engine = create_engine(set_db_connection(), echo=True)
Session = sessionmaker(bind=engine)

# Set the custom base class
Base = declarative_base(cls=Base)


def init_app(app):
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    Session.configure(bind=engine)
    app.session = scoped_session(Session)


# Export session for use in other classes
db_session = Session()
