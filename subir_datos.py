import pandas as pd
from conexion import get_db

def subir_datos():
    db = get_db()
    
    # Leer archivos Excel
    df_2022 = pd.read_excel('data/2022.xlsx')
    df_2023 = pd.read_excel('data/2023.xlsx')
    
    # Convertir a diccionarios
    data_2022 = df_2022.to_dict(orient='records')
    data_2023 = df_2023.to_dict(orient='records')
    
    # Insertar en MongoDB
    db.coleccion_2022.insert_many(data_2022)
    db.coleccion_2023.insert_many(data_2023)
    
    print("Datos insertados correctamente!")

if __name__ == "__main__":
    subir_datos()
