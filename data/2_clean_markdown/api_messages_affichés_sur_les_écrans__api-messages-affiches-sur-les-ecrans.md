---
source_url: https://prim.iledefrance-mobilites.fr/fr/aide-et-contact/documentation/prise-en-main-des-api/api-information-trafic-travaux/api-messages-affiches-sur-les-ecrans
categorie: api_messages_affichés_sur_les_écrans
date_scrap: 2024-05-23
---

Les API Informations Trafic & Travaux

# API Messages affichés sur les écrans

Mis à jour le 28 novembre 2024

**Médias :** Pour la SNCF et le réseau de Bus OPTILE, les APIs temps réel ne disposent pas des informations qui sont fournies sur les médias (site internet, Twitter, …).

**Écrans des gares**

* **RATP** : Ensemble des infos trafics disponibles en gares RER et stations de  métro et sur les médias RATP.
* **SNCF** : Informations disponibles sur les écrans disposés dans les gares.
* **Bus** : Informations disponibles sur les écrans disposés aux arrêts de bus.

### **Structure des requêtes - Paramètres d’appel**​

**Stop :** Ce service permet d’obtenir les informations trafic affichées sur les écrans en temps réel d’un arrêt donné. *Exemple Gare de Saint-Rémy-Lès-Chevreuse : STIF:StopPoint:Q:412844:*

**Ligne :** Ce service permet d’obtenir les informations trafic affichées sur les écrans en temps réel d’une ligne donnée. *Exemple Ligne RER C : STIF:Line::C01727:*

Le paramètre d'appel ALL permet d’obtenir les informations trafic affichées sur les écrans en temps réel de l'ensemble des lignes du réseau. *Exemple : LineRef=ALL*

**Canal :** Ce service permet d'identifier le canal pour lequel on souhaite obtenir les informations trafic affichées sur les écrans en temps réel.  Si ce champ n'est pas présent, la requête concerne tous les canaux. *Exemple : InfoChannelRef=Information OU Perturbation OU Commercial*

***Attention :** Pour requêter l’API vous pouvez soit indiquer le champ « StopPointRef » soit « LineRef » mais pas les deux en même temps.*

Un de ces deux champs est requis car le champ « InfoChannelRef » n'est pas requêtable seul.