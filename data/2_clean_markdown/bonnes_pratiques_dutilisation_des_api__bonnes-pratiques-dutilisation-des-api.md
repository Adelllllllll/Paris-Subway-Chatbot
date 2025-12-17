---
source_url: https://prim.iledefrance-mobilites.fr/fr/aide-et-contact/documentation/donnees-disponibles/api/bonnes-pratiques-dutilisation-des-api
categorie: bonnes_pratiques_dutilisation_des_api
date_scrap: 2024-05-23
---

Les API

# Bonnes pratiques d'utilisation des API

Mis à jour le 28 novembre 2024

* Les quotas d’appels sont à la journée et à la seconde: il est fortement recommandé de **lisser le nombre de requêtes** dans le temps afin de ne pas perturber le fonctionnement pour les autres utilisateurs.
* Compte tenu de la taille très importante de la réponse à la requête globale « Prochains Passages » , elle sera transmise en **mode compressé.**
* Il est recommandé d’activer dans les headers de vos requêtes l’élément « **Accept-encoding : gzip, deflate**» afin d’optimiser le temps de réponse de l’API.