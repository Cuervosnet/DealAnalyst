from scraper.marketplace_scraper import buscar_4runner

print("Buscando Toyota 4Runner...")

anuncios = buscar_4runner()

print(f"Se encontraron {len(anuncios)} anuncios.")

for anuncio in anuncios:
    print(anuncio)