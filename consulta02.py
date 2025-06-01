from conexion import get_db
from datetime import datetime

def consulta_torneo_y_ranking():
    db = get_db()
    coleccion = db['coleccion_2022']
    
    query = {
        "Tournament": "Adelaide International 1",
        "WRank": {"$lt": 30}
    }
    
    documentos = coleccion.find(query)
    
    for doc in documentos:
        fecha = doc.get("Date")
        if isinstance(fecha, dict) and "$date" in fecha:
            fecha = datetime.fromisoformat(fecha["$date"].replace("Z", "+00:00")).date()
        torneo = doc.get("Tournament", "Desconocido")
        ronda = doc.get("Round", "Desconocida")
        ganador = doc.get("Winner", "N/A")
        perdedor = doc.get("Loser", "N/A")
        sets_ganador = doc.get("Wsets", 0)
        sets_perdedor = doc.get("Lsets", 0)

        print(f"{fecha} - {torneo}")
        print(f"Ronda: {ronda}")
        print(f"Ganador: {ganador} (sets: {sets_ganador})")
        print(f"Perdedor: {perdedor} (sets: {sets_perdedor})")
        print("-" * 40)

if __name__ == "__main__":
    consulta_torneo_y_ranking()
