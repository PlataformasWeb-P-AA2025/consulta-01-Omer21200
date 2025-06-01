# consulta01.py
# Los partidos ganados por Kwon S.W. en 2022
from conexion import get_db
from datetime import datetime

def consulta_ganadores():
    db = get_db()
    coleccion = db['coleccion_2022']
    query = {"Winner": "Kwon S.W."}
    documentos = coleccion.find(query)

    for doc in documentos:
        fecha = doc.get("Date")
        if isinstance(fecha, dict) and "$date" in fecha:
            fecha = datetime.fromisoformat(fecha["$date"].replace("Z", "+00:00")).date()
        torneo = doc.get("Tournament", "Desconocido")
        ronda = doc.get("Round", "Desconocida")
        perdedor = doc.get("Loser", "N/A")
        sets_ganador = doc.get("Wsets", 0)
        sets_perdedor = doc.get("Lsets", 0)

        # Resultado set por set
        sets = []
        for i in range(1, 6):
            w_key = f"W{i}"
            l_key = f"L{i}"
            if w_key in doc and l_key in doc:
                w_val = doc[w_key]
                l_val = doc[l_key]
                if isinstance(w_val, (int, float)) and isinstance(l_val, (int, float)):
                    sets.append(f"{w_val}-{l_val}")
        
        print(f"{fecha} - {torneo}")
        print(f"Ronda: {ronda}")
        print(f"Kwon S.W. (sets: {sets_ganador})")
        print(f"{perdedor} (sets: {sets_perdedor})")
        print(f"Resultado: {' | '.join(sets) if sets else 'No disponible'}")
        print("-" * 50)

if __name__ == "__main__":
    consulta_ganadores()
