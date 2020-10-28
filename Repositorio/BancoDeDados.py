
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(r'sqlite:///C:\tmp\PythonWord\banco.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

Base.metadata.create_all(engine)

