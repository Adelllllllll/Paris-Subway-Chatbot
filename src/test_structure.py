import requests
from bs4 import BeautifulSoup

# URL cible (une page représentative de la documentation)
url = "https://prim.iledefrance-mobilites.fr/fr/aide-et-contact/documentation/donnees-disponibles/api/bonnes-pratiques-dutilisation-des-api"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    print(f"🔍 Téléchargement de {url}...")
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # 1. Sauvegarde du HTML complet pour analyse manuelle si besoin
    with open("debug_page.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("✅ Fichier 'debug_page.html' créé.")

    # 2. Analyse rapide de la structure
    soup = BeautifulSoup(response.text, 'html.parser')
    
    print("\n--- ANALYSE DE LA STRUCTURE ---")
    
    # Vérifier si <main> ou <article> existe
    print(f"Balise <main> présente ? : {'OUI' if soup.find('main') else 'NON'}")
    print(f"Balise <article> présente ? : {'OUI' if soup.find('article') else 'NON'}")
    
    # Chercher où se trouve le texte du titre pour remonter au conteneur parent
    # Le titre de la page est "Bonnes pratiques d'utilisation des API"
    target_text = soup.find(string=lambda t: "Bonnes pratiques" in t if t else False)
    if target_text:
        parent = target_text.find_parent('div')
        if parent:
            print(f"\nLe texte cible se trouve dans une div avec les classes : {parent.get('class')}")
            grand_parent = parent.find_parent('div')
            if grand_parent:
                print(f"Le parent du parent a les classes : {grand_parent.get('class')}")

except Exception as e:
    print(f"❌ Erreur : {e}")