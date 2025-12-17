---
source_url: https://prim.iledefrance-mobilites.fr/fr/aide-et-contact/documentation/prise-en-main-des-api/prise-en-main-des-api-prochains-passages/structure-des-requetes-parametres-dappel
categorie: structure_des_requêtes_-_paramètres_dappel
date_scrap: 2024-05-23
---

Les API Prochains Passages

# Structure des requêtes - Paramètres d’appel​

Mis à jour le 28 novembre 2024

## *Service prochains passages – Requête unitaire​*

### Stop (requis)​

Ce service permet d’obtenir les prochains horaires de passages en temps réel d’un arrêt donné.​

Les paramètres d'appel tolérés sont tous les niveaux d’arrêts décrits dans le Référentiel des arrêts d’Île-de-France (arrets.xls), à savoir :​

* **ARr, zone d'embarquement (anciennement ZDER) : « STIF:StopPoint:Q:[ArRId]: »**​ *Exemple : Quais M4 - Châtelet : STIF:StopPoint:22092: (aller) et STIF:StopPoint:463158: (retour)*​

***Attention:*​**

Un quai contient 2 identifiants de zone d’embarquement (ArRId) différents : un pour le sens aller et un pour le sens retour. Une requête sur un quai renverra les prochains passages dans une unique direction.​

Pour les gares RER et Transilien, la SNCF renseigne les données à un ArR fictif qui représente toute la gare.​ --> Privilégier des requêtes aux ZdA / ZdC​

* **ZdA , zone d’arrêts monomodale (anciennement ZDL : Zone de lieu) : « STIF:StopArea:SP:[ZdAId]: »​*Exemple Zone d’arrêts Metro – Châtelet : STIF:StopArea:SP:42587:***​
* **ZdC (zone de correspondance multimodale)** « STIF:StopArea:SP:[ZdCId]: »​ *Exemple Zone de correspondance – Châtelet : STIF:StopArea:SP:71264:*​

**A noter:**​

* Le jeu de données [Référentiel](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/arrets?staticDataSlug=arrets)[des](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/arrets?staticDataSlug=arrets)[arrêts](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/arrets?staticDataSlug=arrets)[:](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/arrets?staticDataSlug=arrets)[Arrêts](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/arrets?staticDataSlug=arrets)propose les arrêts de référence du référentiel des arrêts d'Île-de-France.​
* Le jeu de données [Référentiel](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/relations?staticDataSlug=relations)[des](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/relations?staticDataSlug=relations)[arrêts](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/relations?staticDataSlug=relations)[:](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/relations?staticDataSlug=relations)[Relations](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/relations?staticDataSlug=relations)propose l'ensemble des relations entre les objets du référentiel des arrêts d'Île-de-France.​
* Le Jeu de données [Périmètre](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/perimetre-des-donnees-tr-disponibles-plateforme-idfm?staticDataSlug=perimetre-des-donnees-tr-disponibles-plateforme-idfm)[des](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/perimetre-des-donnees-tr-disponibles-plateforme-idfm?staticDataSlug=perimetre-des-donnees-tr-disponibles-plateforme-idfm)[données](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/perimetre-des-donnees-tr-disponibles-plateforme-idfm?staticDataSlug=perimetre-des-donnees-tr-disponibles-plateforme-idfm)[temps](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/perimetre-des-donnees-tr-disponibles-plateforme-idfm?staticDataSlug=perimetre-des-donnees-tr-disponibles-plateforme-idfm)[réel](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/perimetre-des-donnees-tr-disponibles-plateforme-idfm?staticDataSlug=perimetre-des-donnees-tr-disponibles-plateforme-idfm)[disponibles](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/perimetre-des-donnees-tr-disponibles-plateforme-idfm?staticDataSlug=perimetre-des-donnees-tr-disponibles-plateforme-idfm)expose la liste des arrêts par ligne/ transporteur concernés par ce service.​
* Le jeu de données [Arrêts et lignes associées](https://prim.iledefrance-mobilites.fr/jeux-de-donnees/arrets-lignes) liste toutes les lignes du réseau francilien et les arrêts desservis pour chacune de ces lignes comme dans le GTFS.​

### **​​Ligne (optionnel)**​

Ce service permet d’obtenir les prochains horaires de passages en temps réel d’un arrêt donné, pour une ligne donnée.​

Les paramètres d'appel tolérés sont les lignes décrites dans le [Référentiel](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/referentiel-des-lignes?staticDataSlug=referentiel-des-lignes)[des](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/referentiel-des-lignes?staticDataSlug=referentiel-des-lignes)[lignes](https://rec.prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/referentiel-des-lignes?staticDataSlug=referentiel-des-lignes&ref=prim.iledefrance-mobilites.fr)[de](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/referentiel-des-lignes?staticDataSlug=referentiel-des-lignes)[transport](https://rec.prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/referentiel-des-lignes?staticDataSlug=referentiel-des-lignes&ref=prim.iledefrance-mobilites.fr)[en](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/referentiel-des-lignes?staticDataSlug=referentiel-des-lignes)[commun](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/referentiel-des-lignes?staticDataSlug=referentiel-des-lignes)[d'Île](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/referentiel-des-lignes?staticDataSlug=referentiel-des-lignes)[-de-France](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/referentiel-des-lignes?staticDataSlug=referentiel-des-lignes), à savoir :​

* ID\_Line, identifiant de référence de la ligne commerciale : « STIF:Line::[ID\_Line]: »​ *Exemple Ligne RER C : STIF:Line::C01727:*

## *Service prochains passages – Requête globale​*

### **ALL (requis)**​

Ce service permet d’obtenir les prochains horaires de passages en temps réel de l'ensemble des arrêts du réseau.​

Le seul paramètre d’appel toléré est : ALL.​ *Exemple : LineRef=ALL*​

***Attention:*​**

L’assistant de requêtage disponible sur le portail PRIM n’est pas utilisable pour la requête globale, en vue de la taille de sa réponse. Nous vous recommandons de requêter cette API via une interface de requêtage ou un script.​

***A noter:***​

Le jeu de données [Périmètre](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/perimetre-des-donnees-tr-disponibles-plateforme-idfm?staticDataSlug=perimetre-des-donnees-tr-disponibles-plateforme-idfm)[des](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/perimetre-des-donnees-tr-disponibles-plateforme-idfm?staticDataSlug=perimetre-des-donnees-tr-disponibles-plateforme-idfm)[données](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/perimetre-des-donnees-tr-disponibles-plateforme-idfm?staticDataSlug=perimetre-des-donnees-tr-disponibles-plateforme-idfm)[temps](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/perimetre-des-donnees-tr-disponibles-plateforme-idfm?staticDataSlug=perimetre-des-donnees-tr-disponibles-plateforme-idfm)[réel](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/perimetre-des-donnees-tr-disponibles-plateforme-idfm?staticDataSlug=perimetre-des-donnees-tr-disponibles-plateforme-idfm)[disponibles](https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/perimetre-des-donnees-tr-disponibles-plateforme-idfm?staticDataSlug=perimetre-des-donnees-tr-disponibles-plateforme-idfm)expose la liste des arrêts par ligne/ transporteur concernés par ce service.​