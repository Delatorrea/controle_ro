
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory', echo=True)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

