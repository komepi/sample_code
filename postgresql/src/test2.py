from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import postgresql
db_url = "{dialect}://{username}:{password}@{host}:{port}/{database}".format(
    dialect="postgresql+psycopg2",
    username="root",
    password="root",
    host="db",
    port=5432,
    database="root"
)

engine = create_engine(db_url)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String,VARCHAR
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy_utils.types import JSONType, UUIDType

from sqlalchemy import MetaData, event, util, select,literal_column
NAMING_CONVENTION = util.immutabledict({
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s',
})
metadata = MetaData(naming_convention=NAMING_CONVENTION)
session = sessionmaker(bind=engine)()
import uuid
class RecordMetadata(Base):
    __tablename__ = "records_metadata"
    id = Column(
        UUIDType,
        primary_key=True,
        default=uuid.uuid4,
    )
    """Record identifier."""

    json = Column(
        postgresql.JSONB,
        default=lambda: dict(),
        nullable=True
    )
    
class Activity(Base):
    __tablename__ = "workflow_activity"
    id=Column(Integer,primary_key=True)
    activity_id=Column(String(255),nullable=False,unique=True,index=True)
    item_id=Column(UUIDType,nullable=True,unique=False,index=True)
    
Base.metadata.create_all(engine)

## item_id is null
#act1 = Activity(activity_id="item_id_is_not_null")
#session.add(act1)
#session.commit()
#
## path is not exist
#rm2 = RecordMetadata(json={"id":1})
#session.add(rm2)
#session.commit()
#
#act2 = Activity(activity_id="path_is_not_exist",item_id=rm2.id)
#session.add(act2)
#session.commit()
#
#
## path is exist
#rm3 = RecordMetadata(json={"id":1,"path":["123"]})
#session.add(rm3)
#session.commit()
#
#act3 = Activity(activity_id="path_is_exist",item_id=rm3.id)
#session.add(act3)
#session.commit()
#
#rm4 = RecordMetadata(json={"id":2,"path":["123", "456"]})
#session.add(rm4)
#session.commit()
#act4 = Activity(activity_id="some_path_is_exist", item_id=rm4.id)
#session.add(act4)
#session.commit()

from sqlalchemy import and_, asc, desc, func, or_
from sqlalchemy.sql import exists
query = session.query(Activity,RecordMetadata.json)

query = query.outerjoin(RecordMetadata,
                        and_(Activity.item_id==RecordMetadata.id))
#query = query.filter(exists().where(
#    func.jsonb_array_elements(RecordMetadata.json.op('->')('path')).cast(String).in_(['123'])))
#e_q = session.query(RecordMetadata).filter(RecordMetadata.json.op('->>')('path').cast(String).in_(['456']))
#print(func.jsonb_array_elements_text(RecordMetadata.json.op('->')('path')))
#print(type(func.jsonb_array_elements_text(RecordMetadata.json.op('->')('path'))))
#elem = func.jsonb_array_elements_text(RecordMetadata.json.op('->')('path')).table_valued("value")#.alias('elem')
#e_q = session.query(elem).filter(elem.c.value.cast(String).in_(["789","000"]))
#query = query.filter(e_q.exists())
#print(query)
#res = query.all()
#print(res)
#print([r[0].id for r in res])



#elem = func.jsonb_array_elements_text(RecordMetadata.json.op('->')('path')).alias('elem')
#print(elem)
#e_q = session.query(elem).filter(func.cast(elem.c.values,String).in_(["789","000"]))
#query = query.filter(e_q.exists())
#print(query)
#compiled_query = query.statement.compile(compile_kwargs={"literal_binds": True})
#print(compiled_query)
#print(compiled_query.params)
#res = query.all()
#print(res)
#print([r[0].id for r in res])
#SELECT *
#FROM example_table
#WHERE EXISTS (
#    SELECT 1
#    FROM jsonb_array_elements(test) AS elem
#    WHERE elem::TEXT IN ('"a"', '"b"') 
#);
#f = func.jsonb_array_elements_text(RecordMetadata.json.op('->')('path')).label('elem')
#
##session.query(f).filter(func.cast(f.c.))
#print(f)
#print(type(f))
#print(dir(f))
#elem = func.jsonb_array_elements_text(RecordMetadata.json.op('->')('path')).alias('elem')

#subq = (
#    session.query(1)
#    .select_from(
#        Activity.__table__.outerjoin(
#            RecordMetadata.__table__,
#            Activity.item_id == RecordMetadata.__table__.c.id,
#        )
#    )
#    .filter(
#        func.cast(
#            func.jsonb_array_elements_text(
#                RecordMetadata.__table__.c.json.op("->")("path"),
#            ).op("->>")("value"),
#            String,
#        ).in_(["789", "456"])
#    )
#    .correlate(Activity.__table__)
#    .exists()
#)
#
## メインのクエリ
#result = (
#    session.query(Activity, RecordMetadata.json)
#    .outerjoin(RecordMetadata, Activity.item_id == RecordMetadata.id)
#    .filter(subq)
#    .all()
#)
# メインクエリを作成
from sqlalchemy.orm import aliased
records_metadata_alias = aliased(RecordMetadata)

query = query.filter(exists().select_from(
    func.jsonb_array_elements_text(RecordMetadata.json.op('->')('path')).alias('elem')
).where(func.cast(literal_column('elem'),String).in_(['123'])))
#print(query)
is_
print(compiled_query.params)
result = query.all()
print(result)
#d = elem
#print(d)
#print(type(d))
#print(dir(d))
#e_q = session.query(elem).filter(elem.c.values()[0].cast(String).in_(["789","000"]))
#print(e_q)
#subquery = select([1]).where(func.cast(elem.c.values, String).in_(['789', '456'])).exists()
#print(e_q)
#query = query.filter(e_q.exists())
#print(query)
#print(query.all())

#query = (
#    session.query(
#        Activity.id,
#        Activity.activity_id,
#        Activity.item_id,
#        RecordMetadata.json
#    )
#    .outerjoin(RecordMetadata, WorkflowActivity.item_id == RecordsMetadata.id)
#    .filter(subquery.exists())
#)
