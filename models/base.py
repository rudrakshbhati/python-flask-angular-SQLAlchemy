from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# create engine for sqlalchemy
engine = create_engine('postgresql://user:pass@localhost:5432/test')
Session = sessionmaker(bind=engine)

Base = declarative_base()