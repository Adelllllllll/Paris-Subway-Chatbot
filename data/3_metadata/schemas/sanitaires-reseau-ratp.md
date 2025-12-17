# Schéma des données : sanitaires-reseau-ratp.json

Ce document décrit la structure du fichier de données associé.

| Nom du champ | Type | Description |
| :--- | :--- | :--- |
| **Ligne** | `string` | Nom de la ligne de transport |
| **Station** | `string` | Nom de la station |
| **Accessible au public** | `string` | Valeurs booléennes oui/non |
| **Tarif [Gratuit|Payant]** | `string` | Valeurs gratuit/payant |
| **Acces Passe Navigo ou Ticket T+** | `string` | Valeurs oui ou vide |
| **Acces Bouton poussoir** | `string` | Valeurs oui ou vide |
| **En zone controlee** | `string` | Valeurs oui ou vide |
| **Hors zone controlee station** | `string` | Valeurs oui ou vide |
| **Hors zone controlee voie publique** | `string` | Valeurs oui ou vide |
| **Accessibilite PMR** | `string` | Valeurs oui ou non |
| **Localisation** | `string` | Description de la localisation |
| **type** | `string` | Pas de description disponible |
| **name** | `string` | Pas de description disponible |
| **href** | `string` | Pas de description disponible |
| **type** | `string` | Suggested values: proj4, ogjwkt, esriwkt |
| **properties** | `['object', 'null']` | Pas de description disponible |
| **gestionnaire** | `string` | nom du gestionnaire |
