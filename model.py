from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()

class M010User(Base):
    __tablename__ = 'm010_user'
    id = Column(String, primary_key=True)
    name = Column(String)
    birthday = Column(String)
    address = Column(String)
    deptcode = Column(String)