import hashlib
import pandas as pd
import uuid
from decimal import Decimal

def transformarCompanies(df, correct_ids):
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
            print(original_id)
            corrected_id = correct_ids.get(company_name, original_id)
            print(corrected_id)
        else:
            corrected_id = original_id
        hash_corto = hashlib.sha256(corrected_id.encode('utf-8')).hexdigest()[:24]
        df.loc[index, "company_id"] = hash_corto

        amount = row["amount"]
        df.loc[index, "amount"] = round(amount, 2)
    
    return df

    
    

"""strs = "cbf1c8b09cd5b549416d49d220a40cbd317f952e"
ssss = "cbf1c8b09cd5b549416d49d220a40cbd317f952e"
hash_obj = hashlib.sha256(strs.encode('utf-8'))
hash_hex = hash_obj.hexdigest()
hash_corto = hash_hex[:24]
print(hash_corto)"""

df = pd.read_csv("C:/Users/feres/Documents/UAEM/DocEmplo/Prueba tecnica - NT Group/Seccion1ProcesoETL/files/data_prueba_tecnica.csv")

companies_names = ["MiPasajefy","Muebles chidos"]
correct_ids = {
    "MiPasajefy": "cbf1c8b09cd5b549416d49d220a40cbd317f952e",
    "Muebles chidos":"8f642dc67fccf861548dfe1c761ce22f795e91f0"
}

#companies = df[['name', 'company_id']].drop_duplicates()
#charges = df[['id', 'company_id', 'amount', 'status', 'created_at', 'paid_at']]

f = 2131231231231231200
amount = f/100000000
amount = round(float(amount), 2)

print(amount)