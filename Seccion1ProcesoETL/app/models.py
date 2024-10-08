from sqlalchemy import Column, String, DECIMAL, ForeignKey, TIMESTAMP
from app.db import Base

class Company(Base):
    __tablename__ = "companies"
    
    company_id = Column(String(24), primary_key=True, index=True)
    name = Column(String(130))

class Charge(Base):
    __tablename__ = "charges"
    
    id = Column(String(24), primary_key=True, index=True)
    company_id = Column(String(24), ForeignKey('companies.company_id'), nullable=False)
    amount = Column(DECIMAL(16, 2), nullable=False)
    status = Column(String(30), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    paid_at = Column(TIMESTAMP, nullable=True)