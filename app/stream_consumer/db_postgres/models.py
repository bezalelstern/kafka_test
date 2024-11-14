from sqlalchemy import Column, Integer, String, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class ExplosiveModel(Base):
    __tablename__ = 'explosive_content'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    email = Column(String, ForeignKey('emails.email'), nullable=True)
    email_details = relationship("EmailModel", back_populates="explosive_contents")

class HostagesModel(Base):
    __tablename__ = 'hostages_content'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    email = Column(String, ForeignKey('emails.email'), nullable=True)
    email_details = relationship("EmailModel", back_populates="hostage_contents")

class EmailModel(Base):
    __tablename__ = 'emails'

    email = Column(String, primary_key=True)
    username = Column(String)
    hostage_contents = relationship('HostagesModel', back_populates='email_details')
    explosive_contents = relationship('ExplosiveModel', back_populates='email_details')

