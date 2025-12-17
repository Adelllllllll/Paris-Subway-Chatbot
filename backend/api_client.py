import requests
from typing import Dict, Any, Optional, List
from datetime import datetime
from config import APIConfig
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RatpAPIClient:
    """
    Client pour les 4 APIs temps réel d'Île-de-France Mobilités.
    Retourne du JSON compact pour économiser les tokens.
    """
    
    def __init__(self):
        self.config = APIConfig()
        self.headers = {
            "apikey": self.config.RATP_API_KEY,
            "Accept": "application/json"
        }
    
    def _make_request(self, url: str, params: Dict = None) -> Dict[str, Any]:
        """Méthode générique pour tous les appels API"""
        try:
            logger.info(f"🔍 API Call: {url}")
            logger.debug(f"Params: {params}")
            
            response = requests.get(
                url,
                params=params,
                headers=self.headers,
                timeout=15
            )
            response.raise_for_status()
            
            return {
                "status": "success",
                "data": response.json()
            }
            
        except requests.Timeout:
            logger.error("⏱️ API Timeout")
            return {
                "status": "error",
                "error_type": "timeout",
                "message": "L'API met trop de temps à répondre (>15s)"
            }
            
        except requests.HTTPError as e:
            logger.error(f"❌ HTTP Error: {e}")
            return {
                "status": "error",
                "error_type": "http_error",
                "code": e.response.status_code,
                "message": f"Erreur API: {e.response.status_code}"
            }
            
        except Exception as e:
            logger.error(f"💥 Unexpected error: {e}")
            return {
                "status": "error",
                "error_type": "unknown",
                "message": str(e)
            }
    
    
    # ==================== API 1 : ITINÉRAIRES ====================
    def get_itineraire(
        self,
        depart: str,
        arrivee: str,
        datetime_depart: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Calcule un itinéraire entre deux points.
        
        Endpoint: GET /v2/navitia/journeys
        
        Args:
            depart: Nom ou ID de la station de départ
            arrivee: Nom ou ID de la station d'arrivée
            datetime_depart: Format ISO (ex: "20241216T143000")
        
        Returns:
            JSON compact avec 3 meilleurs itinéraires
        """
        # Format datetime pour l'API Navitia (YYYYMMDDTHHmmss)
        if not datetime_depart:
            datetime_depart = datetime.now().strftime("%Y%m%dT%H%M%S")
        
        params = {
            "from": depart,
            "to": arrivee,
            "datetime": datetime_depart,
            "count": 3,  # 3 itinéraires max
            "min_nb_journeys": 1,
            "max_nb_transfers": 5
        }
        
        response = self._make_request(self.config.JOURNEYS_ENDPOINT, params)
        
        if response["status"] == "error":
            return response
        
        # 🔥 PARSING COMPACT pour économiser tokens
        try:
            journeys = response["data"].get("journeys", [])
            
            if not journeys:
                return {
                    "status": "success",
                    "data": {
                        "found": False,
                        "message": "Aucun itinéraire trouvé entre ces deux points"
                    }
                }
            
            # Extraire uniquement l'essentiel (format ultra-compact)
            itineraires = []
            for journey in journeys[:3]:
                duration_min = journey.get("duration", 0) // 60
                
                # Parser les sections (étapes du trajet)
                sections_compactes = []
                for section in journey.get("sections", []):
                    section_type = section.get("type")
                    
                    if section_type == "public_transport":
                        display = section.get("display_informations", {})
                        sections_compactes.append({
                            "type": "transport",
                            "ligne": display.get("code", "?"),
                            "nom_ligne": display.get("name", ""),
                            "direction": display.get("direction", ""),
                            "depart": section.get("from", {}).get("name", ""),
                            "arrivee": section.get("to", {}).get("name", ""),
                            "duree_min": section.get("duration", 0) // 60
                        })
                    
                    elif section_type == "walking":
                        sections_compactes.append({
                            "type": "marche",
                            "duree_min": section.get("duration", 0) // 60,
                            "distance_m": section.get("duration", 0)
                        })
                
                itineraires.append({
                    "duree_totale_min": duration_min,
                    "heure_depart": journey.get("departure_date_time", ""),
                    "heure_arrivee": journey.get("arrival_date_time", ""),
                    "nb_correspondances": journey.get("nb_transfers", 0),
                    "sections": sections_compactes
                })
            
            return {
                "status": "success",
                "data": {
                    "found": True,
                    "depart": depart,
                    "arrivee": arrivee,
                    "itineraires": itineraires
                }
            }
            
        except Exception as e:
            logger.error(f"Parsing error: {e}")
            return {
                "status": "error",
                "error_type": "parsing",
                "message": "Impossible de parser les données d'itinéraire"
            }
    
    
    # ==================== API 2 : PROCHAINS PASSAGES ====================
    def get_prochains_passages(
        self,
        monitoring_ref: str,  # ID de l'arrêt (ex: "STIF:StopPoint:Q:473921:")
        line_ref: Optional[str] = None  # ID de la ligne (ex: "STIF:Line::C01742:")
    ) -> Dict[str, Any]:
        """
        Récupère les prochains passages à un arrêt.
        
        Endpoint: GET /stop-monitoring
        
        Args:
            monitoring_ref: ID STIF de l'arrêt ou zone d'arrêt
            line_ref: ID STIF de la ligne (optionnel)
        
        Returns:
            JSON compact avec les 5 prochains passages
        """
        params = {
            "MonitoringRef": monitoring_ref
        }
        
        if line_ref:
            params["LineRef"] = line_ref
        
        response = self._make_request(self.config.STOP_MONITORING_ENDPOINT, params)
        
        if response["status"] == "error":
            return response
        
        # Parsing SIRI Lite format
        try:
            siri_data = response["data"].get("Siri", {})
            delivery = siri_data.get("ServiceDelivery", {})
            stop_monitoring = delivery.get("StopMonitoringDelivery", [])
            
            if not stop_monitoring:
                return {
                    "status": "success",
                    "data": {
                        "found": False,
                        "message": "Aucun passage prévu pour cet arrêt"
                    }
                }
            
            # Extraire les passages
            monitored_stops = stop_monitoring[0].get("MonitoredStopVisit", [])
            passages = []
            
            for stop in monitored_stops[:5]:  # Max 5 passages
                journey = stop.get("MonitoredVehicleJourney", {})
                
                passages.append({
                    "ligne": journey.get("LineRef", {}).get("value", "?"),
                    "destination": journey.get("DestinationName", [{}])[0].get("value", ""),
                    "heure_prevue": journey.get("MonitoredCall", {}).get("ExpectedDepartureTime", ""),
                    "temps_attente_min": journey.get("MonitoredCall", {}).get("ExpectedDepartureTime", "")  # À calculer
                })
            
            return {
                "status": "success",
                "data": {
                    "found": True,
                    "arret": monitoring_ref,
                    "passages": passages
                }
            }
            
        except Exception as e:
            logger.error(f"Parsing error: {e}")
            return {
                "status": "error",
                "error_type": "parsing",
                "message": "Impossible de parser les horaires"
            }
    
    
    # ==================== API 3 : INFO TRAFIC ====================
    def get_info_trafic(
        self,
        ligne: Optional[str] = None  # Ex: "line:IDFM:C01742" pour RER A
    ) -> Dict[str, Any]:
        """
        Récupère les perturbations sur le réseau.
        
        Endpoint: GET /v2/navitia/line_reports
        
        Args:
            ligne: ID de la ligne (optionnel, sinon toutes les lignes)
        
        Returns:
            JSON compact avec les perturbations en cours
        """
        url = self.config.LINE_REPORTS_ENDPOINT
        
        # Si une ligne spécifique est demandée
        if ligne:
            url = f"{self.config.BASE_URL}/v2/navitia/{ligne}/line_reports"
        
        response = self._make_request(url, params={})
        
        if response["status"] == "error":
            return response
        
        try:
            reports = response["data"].get("disruptions", [])
            
            if not reports:
                return {
                    "status": "success",
                    "data": {
                        "found": False,
                        "message": "Trafic normal sur l'ensemble du réseau"
                    }
                }
            
            # Extraire les perturbations importantes
            perturbations = []
            for report in reports:
                severity = report.get("severity", {}).get("name", "")
                
                # Ignorer les infos mineures
                if severity in ["information", "none"]:
                    continue
                
                perturbations.append({
                    "ligne": report.get("impacted_objects", [{}])[0].get("pt_object", {}).get("name", ""),
                    "gravite": severity,
                    "titre": report.get("messages", [{}])[0].get("text", ""),
                    "periode": {
                        "debut": report.get("application_periods", [{}])[0].get("begin", ""),
                        "fin": report.get("application_periods", [{}])[0].get("end", "")
                    }
                })
            
            return {
                "status": "success",
                "data": {
                    "found": True,
                    "nb_perturbations": len(perturbations),
                    "perturbations": perturbations
                }
            }
            
        except Exception as e:
            logger.error(f"Parsing error: {e}")
            return {
                "status": "error",
                "error_type": "parsing",
                "message": "Impossible de récupérer les infos trafic"
            }
    
    
    # ==================== API 4 : RECHERCHE DE LIEUX ====================
    def search_place(self, query: str) -> Dict[str, Any]:
        """
        Recherche un lieu (station, adresse...) pour obtenir son ID.
        Utile pour convertir "Châtelet" → "stop_point:IDFM:..."
        
        Endpoint: GET /v2/navitia/places
        """
        params = {
            "q": query,
            "type[]": ["stop_area", "stop_point"]  # Uniquement les arrêts
        }
        
        response = self._make_request(self.config.PLACES_ENDPOINT, params)
        
        if response["status"] == "error":
            return response
        
        try:
            places = response["data"].get("places", [])
            
            if not places:
                return {
                    "status": "success",
                    "data": {
                        "found": False,
                        "message": f"Aucun lieu trouvé pour '{query}'"
                    }
                }
            
            # Retourner les 3 meilleurs résultats
            resultats = []
            for place in places[:3]:
                stop_point = place.get("stop_point", {}) or place.get("stop_area", {})
                
                resultats.append({
                    "nom": stop_point.get("name", ""),
                    "id": stop_point.get("id", ""),
                    "type": place.get("embedded_type", ""),
                    "coord": stop_point.get("coord", {})
                })
            
            return {
                "status": "success",
                "data": {
                    "found": True,
                    "resultats": resultats
                }
            }
            
        except Exception as e:
            logger.error(f"Parsing error: {e}")
            return {
                "status": "error",
                "error_type": "parsing",
                "message": "Impossible de rechercher ce lieu"
            }