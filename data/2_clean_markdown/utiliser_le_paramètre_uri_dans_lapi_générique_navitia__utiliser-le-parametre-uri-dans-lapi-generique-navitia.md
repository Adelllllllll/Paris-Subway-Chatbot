---
source_url: https://prim.iledefrance-mobilites.fr/fr/aide-et-contact/documentation/prise-en-main-des-api/prise-en-main-des-api-calculateur-ile-de-france-mobilites/utiliser-le-parametre-uri-dans-lapi-generique-navitia
categorie: utiliser_le_paramètre_uri_dans_lapi_générique_navitia
date_scrap: 2024-05-23
---

Les API Calculateur Île-de-France Mobilités

# Utiliser le paramètre {URI} dans l’API générique Navitia

Mis à jour le 28 novembre 2024

Le paramètre {URI} signifie que les paramètres d’appel sont intégrés dans l’URL de la requête et ne se trouve pas, comme la plupart du temps, à la fin de l’URL de requête.

***Exemple :*** *Pour récupérer tous les « stop\_points » de la ligne du métro 1 (line:IDFM:C01373 )*

***On utilise la méthode :*** */v2/navitia/{uri}/*stop*\_points/{id}*

***Avec le paramètre d’appel à la place de {id}:*** lines**%2F**line:IDFM:C01373