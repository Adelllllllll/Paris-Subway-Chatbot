# 📘 Documentation Data Preparation - Projet Paris-Subway-Chatbot

## 1. Contexte et Objectif
Ce module "Data Preparation" a pour but de transformer les ressources brutes du portail **PRIM (Île-de-France Mobilités)** en une **Base de Connaissances Structurée** exploitable par un Agent IA.

L'objectif est de permettre à l'agent de générer du code Python d'appel API sans hallucinations, en lui fournissant :
1.  **Le contexte métier** (Documentation textuelle).
2.  **La définition technique** (Swagger OpenAPI).
3.  **La structure des données** (Schémas des CSV).

---

## 2. 📥 Installation & Récupération des Données

Ce dépôt ne contient pas les données CSV brutes (fichiers volumineux) pour rester léger et performant.

### 1. Cloner le projet
```bash
git clone https://github.com/Adelllllllll/Paris-Subway-Chatbot.git
cd Paris-Subway-Chatbot
```

### 2. Télécharger les données brutes (Datasets)
Les fichiers CSV lourds sont stockés externement.
👉 [**Télécharger l'archive 1_raw_data.zip**](https://drive.google.com/drive/u/5/folders/12xumsjusEErf3lzNyObJuMtXUU20cGi-)

### 3. Installer les données
Décompressez l'archive dans le dossier `data/` du projet.
Assurez-vous d'avoir l'arborescence suivante :
```text
data/
└── 1_raw_data/       <-- Dossier décompressé
    ├── datasets/
    ├── html/
    └── schemas_bruts/
```

### 4. Installer les dépendances Python
```bash
pip install -r requirements.txt
```

---

## 3. Architecture des Données

Les données sont organisées selon un pipeline de raffinement en 3 étapes :

```text
data/
├── 1_raw_data/              # [ENTRÉE] Données brutes (Non versionnées sur Git)
│   ├── datasets/            # Fichiers CSV réels (ex: arrets.csv)
│   ├── html/                # Pages web de documentation (sauvegarde)
│   └── schemas_bruts/       # JSON complexes copiés du site (avant nettoyage)
│
├── 2_clean_markdown/        # [TRAITEMENT] Documentation textuelle "LLM-Ready"
│   └── [Categorie]__[Titre].md  # HTML converti en Markdown propre
│
└── 3_metadata/              # [SORTIE] Le "Cerveau" de l'Agent (Versionné sur Git)
    ├── swagger/             # Définitions API (fichiers .json) <-- DÉPLACÉ ICI
    ├── knowledge_index.json # Index liant Documentation <-> Swagger
    ├── datasets&api_catalogue.csv # Catalogue nettoyé pour le choix des sources
    └── schemas/             # Description simplifiée des colonnes CSV (.json/.md)
```

---

## 4. Pipeline de Traitement (Détail des étapes)

### Étape 1 : Web Scraping & Nettoyage (HTML -> Markdown)
* **Source :** Pages de documentation "Guide du développeur" du site PRIM (URLs définies dans `Titres&Liens.md`).
* **Problème :** Le HTML contient trop de bruit (menus, footers) et consomme trop de tokens.
* **Solution :**
    * Extraction ciblée de la `div` de contenu via `BeautifulSoup`.
    * Conversion en **Markdown** (format dense et structuré).
    * Nommage des fichiers avec préfixe de catégorie pour le tri.
* **Résultat :** Dossier `2_clean_markdown/`.

### Étape 2 : Catalogage (Le Menu)
* **Source :** Le fichier `datasets&api_catalogue.csv` original.
* **Action :** Nettoyage pour ne conserver que les **datasets** et **API** réellement utilisés dans le projet. Suppression des colonnes inutiles ("attributs", emails vides).
* **Usage :** C'est le premier fichier que l'Agent lit pour répondre à la question "Quelles données sont disponibles ?".

### Étape 3 : Indexation (Le Cerveau RAG)
* **Fichier clé :** `3_metadata/knowledge_index.json`.
* **Rôle :** Créer le lien logique entre une documentation "Métier" et un fichier "Technique".
* **Structure :**
    ```json
    {
      "doc_id": "doc_002",
      "doc_title": "Identification des Objets",
      "filename": "identification_des_objets.md",
      "related_technical_assets": [
          { "type": "api_definition", "filename": "swagger_prochains_passages.json" }
      ]
    }
    ```
* **Méthode :** Indexation manuelle pour garantir une précision absolue et éviter que l'IA ne mélange les API (ex: confondre l'API Temps Réel avec le Calculateur).

### Étape 4 : Simplification des Schémas (Les Ingrédients)
* **Problème :** Les fichiers CSV sont trop volumineux pour être lus en entier par le LLM. Les définitions JSON brutes du site sont trop verbeuses (GeoJSON standard).
* **Solution :** Création de "Cartes d'identité" légères pour chaque dataset.
* **Script :** `src/clean_schemas.py`.
* **Résultat :** Fichiers dans `3_metadata/schemas/` ne contenant que `Nom Colonne : Description`.
    * *Exemple :* `{"route_id": "Identifiant ligne", "stop_name": "Nom arrêt"}`.

---

## 5. Mode d'Emploi pour l'Agent (Workflow Cible)

L'architecture est conçue pour une **Logique Agentique** en 3 temps :

1.  **SÉLECTION (Router) :**
    * L'agent reçoit la question.
    * Il consulte `datasets&api_catalogue.csv`.
    * Il décide s'il a besoin d'un **Dataset** (ex: `arrets-lignes`) ou d'une **API** (ex: `Prochains Passages`).

2.  **RÉCUPÉRATION (Retrieval) :**
    * *Si API :* Il consulte `knowledge_index.json` pour charger le Markdown explicatif et le Swagger associé.
    * *Si Dataset :* Il charge le schéma simplifié depuis `3_metadata/schemas/` pour connaître les noms de colonnes.

3.  **EXÉCUTION (Generation) :**
    * Il génère le code Python en utilisant les bons IDs (trouvés via recherche dans les datasets) et les bons endpoints (trouvés dans le Swagger).

---

## 6. Inventaire des Scripts de Préparation

Ces scripts (situés dans `src/`) ne servent qu'à la **construction** de la base de données. Ils ne sont pas utilisés lors de l'exécution du chatbot.

| Script | Fonction |
| :--- | :--- |
| `main.py` | Orchestrateur principal qui lance le scraping des URLs définies. |
| `cleaner.py` | Module de nettoyage HTML et conversion Markdown. |
| `clean_catalogue.py` | (Utilitaire) Filtre le CSV catalogue pour garder uniquement les lignes utiles. |
| `clean_schemas.py` | Transforme les JSON bruts (PIRM) en schémas simplifiés pour le LLM. |
| `generate_metadata.py` | (Obsolète) Script de tentative d'indexation automatique (remplacé par manuel). |

---

## Auteur

**Adel ZAIRI**

*Dernière mise à jour : Décembre 2025*

