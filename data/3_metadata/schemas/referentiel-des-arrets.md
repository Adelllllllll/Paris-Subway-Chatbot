# Schéma des données : referentiel-des-arrets.json

Ce document décrit la structure du fichier de données associé.

| Nom du champ | Type | Description |
| :--- | :--- | :--- |
| **ArRId** | `string` | Identifiant Réferentiel de l'objet |
| **ArRVersion** | `string` | Numéro de version de l’objet  |
| **ArRCreated** | `string` | Date de création de l’objet |
| **ArRChanged** | `string` | Date de la dernière modification de l’objet |
| **ArRName** | `string` | Nom de la zone d'embarquement  |
| **ArRType** | `string` | Type d’arrêt |
| **ArRPublicCode** | `string` | Nom du quai ou de la voie connu du voyageur |
| **ArRXEpsg2154** | `integer` | Coordonnées X en Lambert 93 |
| **ArRYEpsg2154** | `integer` | Coordonnées Y en Lambert 93 |
| **ArRTown** | `string` | Libellé de la commune |
| **ArRPostalRegion** | `string` | Code insee de la commune |
| **ArRAccessibility** | `string` | Accessibilité UFR |
| **ArRAudibleSignals** | `string` | Présence d’informations sonores  |
| **ArRVisualSigns** | `string` | Présence d’informations dynamiques  |
| **ArRFareZone** | `string` | Zones tarifaires |
| **ZdAId** | `string` | Identifiant de la zone d'arrêt parente   |
