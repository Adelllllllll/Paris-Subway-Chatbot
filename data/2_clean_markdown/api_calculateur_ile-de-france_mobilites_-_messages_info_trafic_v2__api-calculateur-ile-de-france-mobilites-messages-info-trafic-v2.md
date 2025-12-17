---
source_url: https://prim.iledefrance-mobilites.fr/fr/aide-et-contact/documentation/prise-en-main-des-api/api-information-trafic-travaux/api-calculateur-ile-de-france-mobilites-messages-info-trafic-v2
categorie: api_calculateur_ile-de-france_mobilites_-_messages_info_trafic_v2
date_scrap: 2024-05-23
---

Les API Informations Trafic & Travaux

# API Calculateur Ile-de-France Mobilités - Messages Info Trafic (v2)

Mis à jour le 28 novembre 2024

## Optimiser vos requêtes d’appel à l’API Calculateur Ile-de-France Mobilités - Messages Info Trafic (v2)

*Pour rappel:​*

*Le nombre d'éléments renvoyés pour une requête **ne peut être supérieur à 100**. Si vous en demandez plus, l’API retournera les 100 premiers résultats, et vous devrez paginer en utilisant **le paramètre start\_page pour obtenir les 100 suivants**.*​

*Nous vous recommandons d'ajouter à vos requêtes certains paramètres disponibles afin d'obtenir des réponses plus précises qui s'adaptent réellement à vos besoins.*

**Quelques exemples de requêtes avec le paramètre {URI} pour affiner vos recherches (méthode : /v2/navitia/{uri}/line\_reports)**

**1- Objectif :**Récupérer les infos trafic pour tous les « stop\_points » d’une ligne

***Exemple de requête pour le RER C (line:IDFM:C01727**):* [*https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/line\_reports/lines/line%3AIDFM%3AC01727/line\_reports?count=100*](https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/line_reports/lines/line%3AIDFM%3AC01727/line_reports?count=100)

**2- Objectif :**Récupérer les Info trafic pour un mode de transport en particulier

***Exemple de requête pour le mode « metro »:*** [*https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/line\_reports/physical\_modes/physical\_mode%3AMetro/line\_reports?count=100*](https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/line_reports/physical_modes/physical_mode%3AMetro/line_reports?count=100)

**3- Objectif :**Récupérer toutes les infos trafic sauf exception:

***Exemple de requête pour récupérer toutes les infos trafic sauf bus** :* [*https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/line\_reports/line\_reports?count=100&forbidden\_uris%5B%5D=physical\_mode%3ABus*](https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/line_reports/line_reports?count=100&forbidden_uris%5B%5D=physical_mode%3ABus)