# Schéma des données : referentiel-des-arrets-zones-d-arrets.json

Ce document décrit la structure du fichier de données associé.

| Nom du champ | Type | Description |
| :--- | :--- | :--- |
| **ZdAId** | `string` | Identifiant Référentiel de l’objet  |
| **ZdAVersion** | `string` | Numéro de version  |
| **ZdACreated** | `string` | Date de création de l’objet |
| **ZdAChanged** | `string` | Date de dernière modification de l’objet  |
| **ZdAName** | `string` | Nom de la Zone d’arrêts |
| **ZdAXEpsg2154** | `integer` | Coordonnées X en Lambert 93 du centroïde |
| **ZdAYEpsg2154** | `integer` | Coordonnées Y en Lambert 93 du centroïde |
| **ZdCId** | `string` | Zone de correspondance parente |
| **ZdAPostalRegion** | `string` | Code INSEE de la commune (centroïde) |
| **ZdATown** | `string` | Libellé de la commune  |
| **ZdAType** | `string` | Type de véhicule desservant cette zone d'arrêt |
