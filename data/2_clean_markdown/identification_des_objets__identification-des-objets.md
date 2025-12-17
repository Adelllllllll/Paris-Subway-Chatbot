---
source_url: https://prim.iledefrance-mobilites.fr/fr/aide-et-contact/documentation/prise-en-main-des-api/prise-en-main-des-api-prochains-passages/identification-des-objets
categorie: identification_des_objets
date_scrap: 2024-05-23
---

Les API Prochains Passages

# Identification des objets

Mis à jour le 5 mai 2025

### Identification des lignes

L’identifiant d’une ligne « **LineRef »** doit être passé sous la forme :​

**STIF:Line::CXXXXX:** avec **CXXXXX** l’identifiant de la ligne dans le [**Référentiel**](https://data.iledefrance-mobilites.fr/explore/dataset/referentiel-des-lignes/table?ref=prim.iledefrance-mobilites.fr)[**Île-de-France**](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/referentiel-des-lignes)[**Mobilités**](https://data.iledefrance-mobilites.fr/explore/dataset/referentiel-des-lignes/table?ref=prim.iledefrance-mobilites.fr)​

*Exemples :*​

* Pour la ligne B du RER, l’identifiant de la ligne dans le Référentiel Île-de-France Mobilités est **C01743**, le *pattern* est donc **« STIF:Line::C01743: ».**​
* Pour la ligne de bus Phébus A, l’identifiant de la ligne dans le Référentiel Île-de-France Mobilité est **C00692**, le *pattern* est donc **« STIF:Line::C00692: ».**​

### Identification des arrêts

L’identifiant d’un arrêt « **MonitoringRef\_ZDE »** doit être passé sous la forme :​

**STIF:StopPoint:Q:XXXXX:** avec **XXXXX** l’identifiant du [référentiel](https://data.iledefrance-mobilites.fr/explore/dataset/arrets/table/?ref=prim.iledefrance-mobilites.fr)[des arrêts](https://data.iledefrance-mobilites.fr/explore/dataset/arrets/table/?ref=prim.iledefrance-mobilites.fr)​

***Exemple :***

Pour l’arrêt « Gare de Massy-Palaiseau » sur la ligne B du RER, l’identifiant du référentiel est **412833**, le *pattern* est​ **« STIF:StopPoint:Q:412833: ».**  
  
Notez que depuis le 13/03/2025, les données Prochains Passages SNCF sont disponibles uniquement par zone d'arrêt « **ZdAid »,** que vous pouvez retrouver dans [ce référentiel](https://protection.retarus.com/v1?u=https%3A%2F%2Fprim.iledefrance-mobilites.fr%2Ffr%2Fjeux-de-donnees%2Fzones-d-arrets&c=11R4ui7QrC&r=57AvmVPRfq3wxsKea6dzXV&k=7s1&s=vqdWCPkgj9GU2l3w7608krxLSEH9uaKEUUcmlSErdB3&ref=prim.iledefrance-mobilites.fr), L'identifiant d'une zone d'arrêt doit être passé sous la forme :  
  
**STIF:StopArea:SP:XXXXX:** avec **XXXXX** l’identifiant du [référentiel](https://data.iledefrance-mobilites.fr/explore/dataset/arrets/table/?ref=prim.iledefrance-mobilites.fr)[des Zones d'arrêts](https://data.iledefrance-mobilites.fr/explore/dataset/arrets/table/?ref=prim.iledefrance-mobilites.fr)  
  
***Exemple :***  
  
Pour la station « Clamart » sur la ligne B du RER, l’identifiant du référentiel est **43111**, le *pattern* est​ **« STIF:StopArea:SP:43111: ».**