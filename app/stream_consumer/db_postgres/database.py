from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from .models import *


connection_url = 'postgresql://postgres:1234@localhost:5432/Suspicious_emails'
engine = create_engine(connection_url)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

def init_db():
    Base.metadata.create_all(bind=engine)