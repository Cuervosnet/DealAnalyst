from apify_client import ApifyClient
from config import APIFY_TOKEN

client = ApifyClient(APIFY_TOKEN)


def buscar_4runner():
    run_input = {
        "startUrls": [
            {
                "url": "https://www.facebook.com/marketplace/103752879662908/search?minPrice=10000&maxPrice=14000&query=4runner%20sr5&exact=false"
            }
        ],
        "resultsLimit": 20,
        "includeListingDetails": True,
    }

    run = client.actor("U5DUNxhH3qKt5PnCf").call(run_input=run_input)

    resultados = list(
        client.dataset(run.default_dataset_id).iterate_items()
    )

    return resultados