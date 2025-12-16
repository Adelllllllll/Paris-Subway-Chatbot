import os
import time
import json
import requests
from urllib.parse import quote
from dotenv import load_dotenv

# 1. Configuration
load_dotenv()
API_KEY = os.getenv("RATP_API_KEY")
BASE_URL = "https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia"
HEADERS = {"apikey": API_KEY}

def wait_for_rate_limit():
    """Pause pour respecter les 5 req/s"""
    time.sleep(0.5)

def test_search_place(query):
    """
    Etape 1 : Convertir le texte utilisateur en ID technique
    """
    print(f"\n🔎 RECHERCHE : '{query}'...")
    endpoint = f"{BASE_URL}/places"
    params = {"q": query, "disable_geojson": True}
    
    try:
        wait_for_rate_limit()
        response = requests.get(endpoint, headers=HEADERS, params=params)
        response.raise_for_status()
        data = response.json()
        
        if not data.get("places"):
            print("❌ Aucun résultat.")
            return None
            
        first = data["places"][0]
        # On affiche le nom et l'ID
        print(f"✅ Trouvé : {first['name']} | ID: {first['id']}")
        return first["id"]
    except Exception as e:
        print(f"❌ Erreur recherche : {e}")
        return None

def test_next_departures(station_id):
    """
    Etape 2 : Avoir les horaires
    CORRECTION MAJEURE : Utilisation de /stop_areas/{id}/departures
    """
    print(f"\n⏱️ PROCHAINS DÉPARTS (ID: {station_id})...")
    
    # Encodage de l'ID pour l'URL (les ':' deviennent '%3A')
    safe_id = quote(station_id)
    
    # ASTUCE : Si c'est une 'stop_area', on utilise l'endpoint dédié pour éviter l'erreur 400
    if "stop_area" in station_id:
        endpoint = f"{BASE_URL}/stop_areas/{safe_id}/departures"
    else:
        # Fallback pour les autres types d'objets
        endpoint = f"{BASE_URL}/{safe_id}/departures"

    params = {"count": 5} # On laisse Navitia gérer le mix temps réel/théorique

    try:
        wait_for_rate_limit()
        response = requests.get(endpoint, headers=HEADERS, params=params)
        
        if response.status_code == 400:
            print(f"❌ Erreur 400 sur l'URL : {endpoint}")
            return

        response.raise_for_status()
        data = response.json()
        
        departures = data.get("departures", [])
        print(f"✅ {len(departures)} passages récupérés.")
        
        for dep in departures[:4]:
            info = dep.get("display_informations", {})
            mode = info.get("physical_mode", "Transport")
            line = info.get("label", "?")
            direction = info.get("direction", "?")
            
            # Récupération propre de l'heure
            raw_time = dep.get("stop_date_time", {}).get("departure_date_time", "")
            # Format brut API : 20231027T145000 -> On veut 14h50
            if 'T' in raw_time:
                time_part = raw_time.split('T')[1]
                formatted_time = f"{time_part[:2]}h{time_part[2:4]}"
            else:
                formatted_time = "??h??"
            
            print(f"   🚇 {mode} {line} vers {direction} à {formatted_time}")

    except Exception as e:
        print(f"❌ Erreur horaires : {e}")

def test_itinerary(start_id, end_id):
    """
    Etape 3 : Calcul d'itinéraire
    """
    print(f"\n🗺️ ITINÉRAIRE ({start_id} -> {end_id})...")
    endpoint = f"{BASE_URL}/journeys"
    params = {
        "from": start_id,
        "to": end_id,
        "count": 1,
        "datetime_represents": "departure"
    }

    try:
        wait_for_rate_limit()
        response = requests.get(endpoint, headers=HEADERS, params=params)
        response.raise_for_status()
        data = response.json()
        
        journeys = data.get("journeys", [])
        if not journeys:
            print("❌ Pas d'itinéraire trouvé.")
            return

        best = journeys[0]
        duration = best.get("duration", 0) // 60
        print(f"✅ Trajet trouvé : {duration} min")
        
        # Affichage simplifié des étapes
        for section in best.get("sections", []):
            if section.get("type") == "public_transport":
                info = section.get("display_informations", {})
                print(f"   🔹 {info.get('physical_mode')} {info.get('label')} -> {info.get('direction')}")

    except Exception as e:
        print(f"❌ Erreur itinéraire : {e}")

def test_traffic_check(line_code):
    """
    Etape 4 : Info Trafic (Bonus Swagger 2)
    """
    print(f"\n🚦 INFO TRAFIC pour : '{line_code}'...")
    
    # A. Trouver la ligne
    try:
        wait_for_rate_limit()
        # On cherche l'objet "line" correspondant au code (ex: "1")
        r = requests.get(f"{BASE_URL}/pt_objects", headers=HEADERS, params={"q": line_code, "type[]": "line"})
        data = r.json()
        
        if not data.get("pt_objects"):
            print("   ❌ Ligne introuvable.")
            return

        line_obj = data["pt_objects"][0]
        line_id = line_obj["id"]
        line_name = line_obj["line"]["name"]
        print(f"   ℹ️ Ligne trouvée : {line_name}")

        # B. Chercher les incidents sur cette ligne
        # On interroge /lines/{id}/line_reports
        safe_id = quote(line_id)
        report_endpoint = f"{BASE_URL}/lines/{safe_id}/line_reports"
        
        wait_for_rate_limit()
        r_rep = requests.get(report_endpoint, headers=HEADERS)
        reports = r_rep.json().get("disruptions", [])
        
        active_issues = [r for r in reports if r.get("status") == "active"]
        
        if not active_issues:
            print("   ✅ Trafic fluide (Aucun incident actif).")
        else:
            print(f"   ⚠️ {len(active_issues)} perturbation(s) en cours :")
            for issue in active_issues:
                msg = issue.get("messages", [{}])[0].get("text", "Pas de détail")
                cause = issue.get("cause", "Inconnue")
                print(f"      🔴 {cause}: {msg[:80]}...")

    except Exception as e:
        print(f"❌ Erreur trafic : {e}")

if __name__ == "__main__":
    if not API_KEY:
        print("❌ ERREUR: Pas de clé API dans .env")
        exit()

    print("--- 🚀 TEST DU PIPELINE COMPLET ---")
    
    # 1. Scénario "Prochains départs"
    id_gare = test_search_place("Gare de Lyon")
    if id_gare:
        test_next_departures(id_gare)

    # 2. Scénario "Itinéraire"
    id_defense = test_search_place("La Défense")
    if id_gare and id_defense:
        test_itinerary(id_gare, id_defense)

    # 3. Scénario "Info Trafic"
    test_traffic_check("Metro 1")
    test_traffic_check("RER A")