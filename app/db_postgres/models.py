from sqlalchemy import Column, Integer, String, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class ExplosiveModel(Base):
    __tablename__ = 'explosive_emails'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)


class HostagesModel(Base):
    __tablename__ = 'hostages_emails'
    id = Column(Integer, primary_key=True)
    email = Column(String)

