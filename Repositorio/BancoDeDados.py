from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///banco.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    Base.metadata.create_all(engine)
    session = Session()

    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise Exception(e)
    finally:
        session.close()
