from sqlalchemy import create_engine, util, MetaData
from sqlalchemy.orm import sessionmaker

db_url = "{dialect}://{username}:{password}@{host}:{port}/{database}".format(
    dialect="postgresql+psycopg2",
    username="root",
    password="root",
    host="postgresql",
    port=5432,
    database="root"
)

engine = create_engine(db_url)
session = sessionmaker(bind=engine)()