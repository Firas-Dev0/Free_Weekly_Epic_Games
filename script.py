import requests
import json

API_URL = "https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=US&allowCountries=FR"
try:
    res = requests.get(API_URL)
    data = res.json()
    elements = (
        data.get("data",{})
            .get("Catalog",{})
            .get("searchStore",{})
            .get("elements",[])
    )

    if not elements:
        print("Couldn't get games")
    else:
        free = []
        for g in elements:
            price = g.get("price",{}).get("totalPrice",{})
            if price.get("discountPrice")== 0 and price.get("originalPrice") != 0:
                free.append(g)
        if not free:
            print("aucun jeu gratuit")
        else:
            for game in free:
                title = game.get("title","Unknown")
                desc = game.get("description","No desvription")
                print(f"\n**Titre:** {title}")
                print(f"**Description:** {desc}")
                print("-"*60)
except requests.exceptions.RequestException as e:
    print(f"Erreur lors de l'appel API: {e}")
except Exception as e:
    print(f"Erreur survenue : {e}")