from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.dialects.postgresql import JSONB


from sessions import session

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer,primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    json = Column(JSONB)
    
    @property
    def full_name(self):
        return "{} {}".format(self.first_name,self.last_name)
    
    @classmethod
    def create1(cls, first_name, last_name,json):
        with session.begin_nested():
            obj = cls(first_name=first_name,last_name=last_name,json=json)
            session.add(obj)
        session.commit()
        return obj

    @classmethod
    def create2(cls, first_name, last_name,json):
        obj = User(first_name=first_name,last_name=last_name,json=json)
        session.add(obj)
        session.commit()
        return obj
    

