from fastapi import FastAPI, HTTPException

app = FastAPI()

taches = [{"id": 1, "titre": "Acheter du lait"}, {"id": 2, "titre": "Réviser FastAPI"}]

# Exercice 3
@app.get("/taches")
async def read_item(id_item: int=1):
    global taches
    for elements in taches:
        if str(elements["id"]) == str(id_item):
            return elements
    raise HTTPException(status_code=404, detail="YA ZEEEBI")

# Exercice 2

# Définir l'endpoint POST pour ajouter une nouvelle tâche
@app.post("/taches/{id}/{titre}")
async def ajouter_tache(id: int, titre: str):
    global taches
    nouvelle_tache = {"id": id, "titre":    titre}
    taches.append(nouvelle_tache)
    return {"message": "Nouvelle tâche ajoutée avec succès", "tâche": {"id": id, "titre": titre}}

# Exercice 1

@app.get("/taches/liste")
async def listtache():
    global taches
    return taches