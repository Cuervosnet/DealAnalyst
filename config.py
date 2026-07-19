from dotenv import load_dotenv
import os

load_dotenv(override=True)

APIFY_TOKEN = os.getenv("APIFY_TOKEN")

print("Token encontrado:", bool(APIFY_TOKEN))
print("Inicio del token:", APIFY_TOKEN[:10] if APIFY_TOKEN else "VACÍO")
print("Longitud:", len(APIFY_TOKEN) if APIFY_TOKEN else 0)
