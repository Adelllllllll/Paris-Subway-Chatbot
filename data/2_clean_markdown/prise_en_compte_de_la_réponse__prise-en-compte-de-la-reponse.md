---
source_url: https://prim.iledefrance-mobilites.fr/fr/aide-et-contact/documentation/prise-en-main-des-api/prise-en-main-des-api-prochains-passages/prise-en-compte-de-la-reponse
categorie: prise_en_compte_de_la_réponse
date_scrap: 2024-05-23
---

Les API Prochains Passages

# Prise en compte de la réponse

Mis à jour le 28 novembre 2024

### **AimedArrival/ DepartureTime:** ​

Horaires théoriques de départ et d’arrivée établis la veille par le transporteur en prenant en compte la disponibilité des conducteurs et des véhicules. Ces horaires ne sont pas toujours disponibles.​

### **ExpectedArrival/ DepartureTime:** ​

Prédictions d’horaires de prochains passages prenant en compte la **position réelle** du véhicule, le temps restant pour atteindre un arrêt et les temps de parcours observés sur les trajets précédents.​

### **Arrival/ DepartureStatus :** ​

Caractérisent les horaires de départ ou d’arrivée attendus (ou mesurés si le véhicule est à quai).​

Ces champs peuvent prendre les valeurs suivantes :​

* **onTime :** A l'heure prévue​
* **early :** En avance​
* **delayed :** Retardé​
* **cancelled :** Passage à un arrêt annulé (ne concerne pas l'entièreté du trajet).​
* **missed :** Le véhicule n'a pas marqué l'arrêt alors qu'il aurait dû, mais la course continue.​
* **arrived :** Arrivé​
* **departed :** Parti​
* **notExpected :** Non planifié (cas de TAD encore non déclenché)​
* **noReport :** Non communiqué Valeur par défaut : « onTime ».​

***Attention :** La réponse de l'API contient les données à partir de 30 minutes avant le moment de la requête et jusqu’à 2 heures après.​*

### **DirectionRef:**

Il n’y a pas de référentiel  partagé à l’échelle d’Île-de-France Mobilités, le  champ est donc facultatif. Cependant le champ **« DestinationRef »** (terminus de la course) est toujours renseigné.

### **DatedvehicleJourney  Ref:**

L’identifiant de la course **identifie de manière unique** une  course pour tous les transporteurs. Dans une réponse à une requête globale, la course est reconstituée car on  obtient les prochains passages à tous les arrêts de cette course.

### **VehicleFeatureRef:**

Indique la **longueur des trains**. Ce champ peut prendre deux valeurs :

* La valeur « **shortTrain** » signale qu’il  s’agit d’un train court.
* La valeur « **longTrain** » signale qu’il  s’agit d’un train long.

Cependant, ce champ est facultatif pour les transporteurs, ainsi s’il ne figure pas dans la réponse cela signifie que le transporteur n’a pas transmis l’information.

***Attention :***

La RATP ne fournit pas d’identifiants de courses mais un compteur technique sans lien métier avec la notion de course.

Nous obtenons alors dans la réponse à la requête globale pour une même ligne et un même sens tous les véhicules s’arrêtant à la même heure quel que soit l’arrêt. Par conséquent, dans les réponses aux requêtes globales, **les courses RATP ne sont pas correctement reconstituées.** Les prochains passages aux arrêts sont cependant tous renseignés dans la réponse.