"Creación de carpetas para almacenar datos"
import os
os.makedirs("data/raw", exist_ok=True)

"Extracción de información desde la API Open Library"
import requests
import json
import os

def descargar_openlibrary(query):
    # Crear carpetas si no existen
    os.makedirs("data/raw", exist_ok=True)
    
    url = f"https://openlibrary.org/search.json?q={query}"
    resp = requests.get(url)
    data = resp.json()
    
    with open("data/raw/openlibrary.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Archivo openlibrary.json guardado correctamente")

descargar_openlibrary("python libros")

"Conversion a csv"
import json
import pandas as pd

os.makedirs("data/processed", exist_ok=True)

with open("data/raw/openlibrary.json", encoding="utf-8") as f:
    data = json.load(f)

libros = []

for libro in data["docs"][:100]:  # primeros 100 libros
    libros.append({
        "titulo": libro.get("title"),
        "autor": ", ".join(libro.get("author_name", [])) if "author_name" in libro else None,
        "anio_publicacion": libro.get("first_publish_year")
    })

df = pd.DataFrame(libros)
df.to_csv("data/processed/openlibrary.csv", index=False, encoding="utf-8")


"Importaciones para consumo de la API OpenAlex"

def descargar_openalex(query):
    os.makedirs("data/raw", exist_ok=True)
    
    url = "https://api.openalex.org/works"
    params = {
        "filter": "type:book",
        "search": query,
        "per-page": 50
    }
    
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()
    
    with open("data/raw/openalex_books.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print("Archivo openalex_books.json guardado correctamente")

descargar_openalex("data science")

"Conversión de datos a CSV (OpenAlex)"

with open("data/raw/openalex_books.json", encoding="utf-8") as f:
    data = json.load(f)

libros = []

for item in data["results"]:
    libros.append({
        "titulo": item.get("title"),
        "anio_publicacion": item.get("publication_year"),
        "editorial": item.get("publisher"),
        "tipo": item.get("type")
    })

df = pd.DataFrame(libros)
os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/openalex_books.csv", index=False, encoding="utf-8")



"Extracción de información desde la API OpenAlex"

def descargar_crossref():
    os.makedirs("data/raw", exist_ok=True)

    url = "https://api.crossref.org/works"
    params = {
        "filter": "type:book",
        "rows": 50
    }

    resp = requests.get(url, params=params)
    data = resp.json()

    with open("data/raw/crossref_books.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Archivo crossref_books.json guardado correctamente")

descargar_crossref()


"Conversión de datos a CSV (Crossref)"
with open("data/raw/crossref_books.json", encoding="utf-8") as f:
    data = json.load(f)

libros = []

for item in data["message"]["items"]:
    libros.append({
        "titulo": item.get("title", [""])[0],
        "anio": item.get("issued", {}).get("date-parts", [[None]])[0][0],
        "editorial": item.get("publisher"),
        "doi": item.get("DOI")
    })

df = pd.DataFrame(libros)

df.to_csv(
    "data/processed/crossref_books.csv",
    index=False,
    encoding="utf-8"
)




