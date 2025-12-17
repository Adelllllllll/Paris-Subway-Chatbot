---
source_url: https://prim.iledefrance-mobilites.fr/fr/aide-et-contact/documentation/prise-en-main-des-api/api-information-trafic-travaux/api-messages-info-trafic-requete-globale
categorie: api_messages_info_trafic_-_requête_globale
date_scrap: 2024-05-23
---

Les API Informations Trafic & Travaux

# API Messages Info Trafic - Requête globale

Mis à jour le 28 novembre 2024

## Mapping entre l'API Calculateur Ile-de-France Mobilités - Messages Info Trafic (v2) et l'API Messages Info Trafic - Requête globale

### Lignes impactées

|  | Description | API Line\_Reports | Exemple de valeur | API Bulk Disruptions | Exemple de valeur |
| --- | --- | --- | --- | --- | --- |
| 1 | Identifiant de la ligne | line.id | line:IDFM:C01110 | lines.id | line:IDFM:C01110 |
| 2 | Nom de la ligne | line.name | 75 | lines.name | 75 |
| 3 | Nom court de la ligne | line.code | 75 | lines.shortName | 75 |
| 4 | Mode | line.physical\_modes.id | Bus | lines.mode | Bus |
| 5 | Identifiant du réseau | line.network.id | network:IDFM:Operator\_100 | lines.networkId | network:IDFM:Operator\_100 |

### Objets impactés

|  | Description | API Line\_Reports | Exemple de valeur | API Bulk Disruptions | Exemple de valeur |
| --- | --- | --- | --- | --- | --- |
| 1 | Type | pt\_objects.embedded\_type | [line ; network ; stop\_point ; stop\_area] | impactedObjects.type | [line ; network ; stop\_point ; stop\_area] |
| 2 | Identifiant de l'objet impacté | pt\_objects.[line ; network ; stop\_point ; stop\_area].id | line:IDFM:C01110 | impactedObjects.id | line:IDFM:C01110 |
| 3 | Nom de l'objet impacté | pt\_objects.[line ; network ; stop\_point ; stop\_area].name | 75 | impactedObjects.name | 75 |
| 4 | Lien vers les infos trafic | pt\_objects.[line ; network ; stop\_point ; stop\_area].links.id | 35088aa0-abdd-11ee-97fc-0a58a9feac02 | impactedObjects.disruptionIds | 35088aa0-abdd-11ee-97fc-0a58a9feac02 |

### Informations trafic

|  | Description | API Line\_Reports | Exemple de Valeur | API Bulk Disruptions | Exemple de Valeur |
| --- | --- | --- | --- | --- | --- |
| 1 | Identifiant de l'info trafic | id | 35088aa0-abdd-11ee-97fc-0a58a9feac02 | disruptions.id | 35088aa0-abdd-11ee-97fc-0a58a9feac02 |
| 2 | Début de période d'application | application\_periods.begin | 20240102T051500 | disruptions.applicationPeriods.begin | 20240102T051500 |
| 3 | Fin de période d'application | application\_periods.end | 20240512T024500 | disruptions.applicationPeriods.end | 20240512T024500 |
| 4 | Date de mise à jour | updated\_at | 20240105T161506 | disruptions.lastUpdate | 20240105T161506 |
| 5 | Cause | cause | [travaux ; perturbation ; information] | disruptions.cause | [TRAVAUX ; PERTURBATION ; INFORMATION] |
| 6 | Sévérité | severity.name | [bloquante ; perturbée ; information] | disruptions.severity | [BLOQUANTE ; PERTURBEE ; INFORMATION] |
| 7 | Étiquette | tags | Actualité | disruptions.tags | Actualité |
| 8 | Titre | messages.text | Bus 75 : Travaux - Arrêt(s) non desservi(s) | disruptions.title | Bus 75 : Travaux - Arrêt(s) non desservi(s) |
| 9 | Message | messages.text | La ligne 75 est déviée : les arrêts situés entre Alibert et République ne sont plus desservis en direction de Panthéon. Reprise estimée : dimanche 12 mai 2024, à partir de 02h00. Raison : travaux. Plus d'informations sur le site ratp.fr | disruptions.message | La ligne 75 est déviée : les arrêts situés entre Alibert et République ne sont plus desservis en direction de Panthéon. Reprise estimée : dimanche 12 mai 2024, à partir de 02h00. Raison : travaux. Plus d'informations sur le site ratp.fr |