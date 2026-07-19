from apify_client import ApifyClient
from dotenv import load_dotenv
import os
load_dotenv()
token = os.getenv("APIFY_TOKEN")
client = ApifyClient(token)
if token:
    print("✅ Token cargado correctamente.")
else:
    print("❌ No se encontró el token.")