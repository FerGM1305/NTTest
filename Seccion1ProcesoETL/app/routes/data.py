from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
import pandas as pd
from app import crud, db
import hashlib
import uuid
from decimal import Decimal

router = APIRouter()

@router.post("/upload_csv/")
async def upload_csv(file: UploadFile = File(...), dbs: Session = Depends(db.get_db)):
    df = pd.read_csv(file.file)
    #df = df.dropna(how='all')
    # Cargar datos en una tabla temporal
    df.to_sql("temp_data", con=db.engine, if_exists='replace', index=False)
    return {"status": "CSV loaded successfully"}




@router.post("/transform/")
async def transform_data(dbs: Session = Depends(db.get_db)):
    # Leer tabla temporal
    df = pd.read_sql("SELECT * FROM temp_data", con=db.engine)

    correct_ids = {
        "MiPasajefy": "cbf1c8b09cd5b549416d49d220a40cbd317f952e",
        "Muebles chidos":"8f642dc67fccf861548dfe1c761ce22f795e91f0"
    }

    for index, row in df.iterrows():
        original_id = str(row["company_id"])
        company_name = str(row['name'])

        if row['id'] is not None:
            # Calcular el hash para el ID del cargo si tiene un valor
            df.loc[index, "id"] = hashlib.sha256(row['id'].encode('utf-8')).hexdigest()[:24]
        else:
            df.loc[index, "id"] = str(uuid.uuid4())[:24]  # Generar un UUID y truncarlo a 24 caracteres


        if "MiP" in company_name:
            company_name = "MiPasajefy"
            df.loc[index, "name"] = company_name
        if company_name == "nan":
            company_names = [k for k, v in correct_ids.items() if v == list(correct_ids.values())[0]]
            company_name = company_names[0]
            if company_name == "":
                company_name = [k for k, v in correct_ids.items() if v == list(correct_ids.values())[1]]
            df.loc[index, "name"] = company_name
        
        
        if original_id == "nan" or not original_id.isalnum():
            corrected_id = correct_ids.get(company_name, original_id)
        else:
            corrected_id = original_id
        hash_corto = hashlib.sha256(corrected_id.encode('utf-8')).hexdigest()[:24]
        df.loc[index, "company_id"] = hash_corto

        amount = row["amount"]
        #df.loc[index, "amount"] = round(float(amount), 2)
        max_value = 99999999999999.99  # Límite máximo para DECIMAL(16, 2)
    
        if amount > max_value:
            print(f"El valor {amount} es demasiado grande para la columna DECIMAL(16, 2). Se agregara amount/amount")
            amount = amount/amount
        df.loc[index, "amount"] = amount
    companies = df[['name', 'company_id']].drop_duplicates()
    charges = df[['id', 'company_id', 'amount', 'status', 'created_at', 'paid_at']]

    for _,company in companies.iterrows():
        existing_company = crud.get_company_by_id(dbs, company['company_id'])
        if not existing_company:
            crud.create_company(dbs, company)
    
    for _, charge in charges.iterrows():
        crud.create_charge(dbs, charge.to_dict())

    return {"status": "Data transformed and loaded successfully"}