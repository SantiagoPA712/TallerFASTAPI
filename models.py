from sqlalchemy import Column, Integer, String
from database import Base

class PlayerDB(Base):
    __tablename__ = "players"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    height = Column(Integer)
