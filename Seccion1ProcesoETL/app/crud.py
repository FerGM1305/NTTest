from sqlalchemy.orm import Session
from app.models import Company, Charge

# Función para crear compañía
def create_company(db: Session, company_data: dict):
    company = Company(**company_data)
    db.add(company)
    db.commit()
    db.refresh(company)
    return company

# Función para crear un cargo
def create_charge(db: Session, charge_data: dict):
    charge = Charge(**charge_data)
    db.add(charge)
    db.commit()
    db.refresh(charge)
    return charge

# Consultar todas las compañías
def get_companies(db: Session):
    return db.query(Company).all()

def get_company_by_id(db: Session, company_id: str):
    return db.query(Company).filter(Company.company_id == company_id).first()
