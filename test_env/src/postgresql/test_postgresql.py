from sqlalchemy import create_engine, util, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.dialects.postgresql import JSONB

from sessions import session
from models import User
import json

#test_data = json.dumps([{'test':"that's right"}])
#input_data = {"first_name":"test","last_name":"testsss","json":test_data}
#user = User(**input_data)
#session.add(user)
#session.commit()
#
#ss = session.query(User).filter_by().one()
#print(ss.json)
user = User.create1("test","testtest",{"test1":1})
ss = session.query(User).filter_by(user_id=user.user_id).one()
print(ss.json)