# coding: utf-8
"""
Create models whit sqlcodegen
pip3 install sqlacodegen
Example:
sqlacodegen mysql://root:@127.0.0.1:3306/bit_db --outfile models.py

"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Float, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

Base = declarative_base()
metadata = Base.metadata
# Create database engine mysql in the connection string
ENGINE = create_engine('mysql+pymysql://{USER}:{PASSWORD}@{DATABASE-HOST}/{DATABASE-NAME}', echo=True)
# Create session on database engine
Session = sessionmaker(bind=ENGINE)


class BtcHistory(Base):
    __tablename__ = 'btc_history'

    date = Column(String(20), primary_key=True)
    price = Column(Float, nullable=False)
    var = Column(Float, nullable=False)

    # Property serialize data in dictionary
    @property
    def serialized(self):

        return {
            'date': self.date,
            'price': self.price,
            'variation': self.var
        }


class TokenTable(Base):
    __tablename__ = 'token_table'

    id = Column(INTEGER(11), primary_key=True)
    email = Column(String(100), nullable=False)
    token = Column(String(250), nullable=False)

    # Property serialize data in dictionary
    @property
    def serialized(self):

        return {
            'id': self.id,
            'email': self.email,
            'token': self.token
        }