from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    user_phone = Column(String, index=True)
    type = Column(String)  # income or expense
    amount = Column(Float)
    description = Column(String)
    date = Column(DateTime, default=datetime.utcnow)