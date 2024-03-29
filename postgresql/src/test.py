from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
db_url = "{dialect}://{username}:{password}@{host}:{port}/{database}".format(
    dialect="postgresql+psycopg2",
    username="root",
    password="root",
    host="db",
    port=5432,
    database="root"
)
from sqlalchemy import or_
engine = create_engine(db_url)
#
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
import traceback
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
#
from sqlalchemy import MetaData, event, util
NAMING_CONVENTION = util.immutabledict({
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s',
})
metadata = MetaData(naming_convention=NAMING_CONVENTION)
session = sessionmaker(bind=engine)()
class User(Base):
    __tablename__ = "user_table"
    user_id = Column(Integer,primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    
    def full_name(self):
        return "{} {}".format(self.first_name,self.last_name)
    @classmethod
    def create1(cls, first_name, last_name):
        with session.begin_nested():
            obj = cls(first_name=first_name,last_name=last_name)
            session.add(obj)
        return obj

    @classmethod
    def create2(cls, first_name, last_name):
        obj = User(first_name=first_name,last_name=last_name)
        session.add(obj)
        return obj
Base.metadata.create_all(engine)

#if len(session.query(User).all()) < 1:
#    session.add(User(first_name="xxx1",last_name="yyy1"))
#    session.add(User(first_name="xxx1",last_name="yyy2"))
#    session.add(User(first_name="xxx2",last_name="yyy3"))
#    session.commit()


#try:
#    user = User(first_name="tttt1",last_name="yyy")
#    session.add(user)
#    session.commit()
#    print("name1:{}".format(user.first_name))
#    #raise Exception("test_error")
#except:
#    session.rollback()
#    print("name2:{}".format(user.first_name))
#
#user_q = session.query(User).filter_by(first_name="tttt1").one()
#print("name2_1:{}".format(user_q.first_name))
#session.delete(user_q)
#print("name2:{}".format(user_q.first_name))
#session.commit()
#print("name3:{}".format(user_q.first_name))

session.add(User(first_name="ssss",last_name="sxxxx"))
session.commit()
session.rollback()


#query = session.query(User) 
#print("q1:{}".format(query))
#query = query.filter(or_(User.first_name=="xxx1"))
#print("q2:{}".format(query))
#query = query.filter(or_(User.last_name=="yyy1"))
#print("q3:{}".format(query))
#conditions = [
#    User.first_name=="xxx1"]
#conditions.append(User.first_name=="xxx2")
#query = session.query(User).filter(or_(*conditions))
#print([q.last_name for q in query.all()])
#conditions2=[User.last_name=="yyy1",User.last_name=="yyy2"]
#query = query.filter(or_(*conditions2))
#print(query)
##print(session.query(User).first().__dict__)
##session.close()
##try:
##    user1=User.create(first_name="test111",last_name="tar111")
##    raise Exception("test_error")
##    session.commit()#
##except Exception as e:
##    session.rollback()
##print(user1)
##print(user1.full_name())
##
##print([f.full_name() for f in session.query(User).all()])
#
#
##try:
##    new_user = User.create2("tests","ssss")
##    raise Exception("t")
##    session.commit()
##except Exception as e:
##    session.rollback()
##    print("raise error")
##print(new_user.first_name)
##
##def test():
##    try:
##        new_user = User(first_name="ssss",last_name="ssss")
##        session.add(new_user)
##        session.commit()
##    except Exception as e:
##        session.rollback()
##    return new_user
#
##uuu = test()
##print(uuu.last_name)
##print(session.query(User).first().last_name)
#
#try:
#    new_user = User(first_name="test1",last_name="testtest")
#    session.add(new_user)
#    raise Exception("test")
#    session.commit()
#    
#except Exception as e:
#    session.rollback()
#    print("raise error")


