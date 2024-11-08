from sqlalchemy import Column, Integer, Sequence, String
from app.database import Base

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, Sequence('item_id_seq'), primary_key=True)
    name = Column(String)
