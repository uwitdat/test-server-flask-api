from sqlalchemy.ext.declarative import declared_attr


class Base(object):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
