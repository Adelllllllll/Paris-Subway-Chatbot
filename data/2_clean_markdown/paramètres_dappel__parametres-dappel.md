---
source_url: https://prim.iledefrance-mobilites.fr/fr/aide-et-contact/documentation/prise-en-main-des-api/prise-en-main-des-api-calculateur-ile-de-france-mobilites/parametres-dappel
categorie: paramètres_dappel
date_scrap: 2024-05-23
---

Les API Calculateur Île-de-France Mobilités

# Paramètres d'appel

Mis à jour le 28 novembre 2024

### **route**

Une « **route** » est un ensemble d’itinéraires regroupés sous un même nom, cet objet fait référence à l’identifiant de la ligne disponible dans le [référentiel des lignes](https://data.iledefrance-mobilites.fr/explore/dataset/referentiel-des-lignes/information/?ref=prim.iledefrance-mobilites.fr).

*Ex : IDFM:C01371 (Métro 1)*

### **trip**

Une « **trip** » définit un parcours sur une ligne donnée, il s’agit d’un enchaînement structuré d’arrêts.

*Ex : IDFM:RATP:9541-C01371-10\_3736592\_955496 (Métro 1 – Sens la Défense)*

### **service**

Une course « **service**» est la déclinaison d’un itinéraire à un horaire donné. Une course attribue à chaque arrêt de l’itinéraire un horaire de passage.

Sur une journée, une course est unique : deux véhicules d’une même ligne effectuent chacun une course différente.

*Ex : IDFM:100071 (Métro 1 - une course qui circule que les samedis du 21 août 2021 au 28 août 2021)*

### **agency**

Une « **agency** » est un réseau commercial ou un opérateur de transport.

*Ex :  IDFM:1051 (Poissy - Les Mureaux) ou IDFM:Operator\_100 (RATP)*

### **stop**

Un « **stop** » est un objet qui décrit un type d’arrêt, il s’agit de :

1. Un point d’arrêt d’un seul et unique transporteur, pour ce cas il prend les formes suivantes :

* StopPoint Ferré (RER,Transilien): «IDFM:[ID ZdA] »
* StopPoint (reste): « IDFM:[ID ArR] »

*Ex : IDFM:3640 (Jean de La Fontaine)*

2. Un « **stop\_area »** est un regroupement d’arrêts physiques portant le même nom dit aussi un arrêt commercial:

* StopArea : «IDFM:[ID ZdC]»

*Ex : IDFM:70604 (Porte de Choisy)*

***À noter:***

**« stop\_point »** est une donnée non pérenne pour le bus. Elle est susceptible d’être changée chaque jour à la publication du GTFS. Les **« stop\_points »** sont plutôt stables pour le réseau ferré.