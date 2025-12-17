# Schéma des données : arrets-lignes.json

Ce document décrit la structure du fichier de données associé.

| Nom du champ | Type | Description |
| :--- | :--- | :--- |
| **route_id** | `string` | Identifiant de la ligne (aligné avec le GTFS) |
| **route_long_name** | `string` | Nom de la ligne (aligné avec le GTFS) |
| **stop_id** | `string` | Identifiant de l'arrêt (aligné avec le GTFS) |
| **stop_name** | `string` | Nom de l'arrêt (aligné avec le GTFS) |
| **stop_lon** | `string` | Coordonnées longitude de l'arrêt (aligné avec le GTFS) |
| **stop_lat** | `string` | Coordonnées latitude de l'arrêt (aligné avec le GTFS) |
| **OperatorName** | `string` | Nom du transporteur |
| **type** | `string` | Pas de description disponible |
| **name** | `string` | Pas de description disponible |
| **href** | `string` | Pas de description disponible |
| **type** | `string` | Suggested values: proj4, ogjwkt, esriwkt |
| **properties** | `['object', 'null']` | Pas de description disponible |
| **Nom_commune** | `string` | Nom de la commune |
| **Code_insee** | `string` | Code INSEE de la commune |
