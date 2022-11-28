from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class BaseModel:
    __abstract__ = True

    def __repr__(self):
        fmt = u'{}({})'
        class_ = self.__class__.__name__
        attrs = sorted(
            (k, getattr(self, k)) for k in self.__mapper__.columns.keys()
        )
        sattrs = u', '.join('{}={!r}'.format(*x) for x in attrs)
        return fmt.format(class_, sattrs)


Base = declarative_base(cls=BaseModel)
engine = create_engine("sqlite:///reqresin_users.db")
Session = sessionmaker(engine)


