# 🚇 Paris Subway Chatbot – RATP Assistant

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![PRIM API](https://img.shields.io/badge/Data-RealTime-green)

## 📋 Contexte du Projet

Ce projet est un **Proof of Concept (POC)** d'un assistant conversationnel intelligent dédié aux usagers des transports en commun parisiens.

L'objectif est de démontrer comment une architecture **RAG Agentique** peut transformer une demande en langage naturel en requêtes API techniques précises, pour fournir des informations d'itinéraires et d'horaires en temps réel, tout en limitant les hallucinations.

## 🏗️ Architecture de la Solution

L'application repose sur un pipeline séquentiel clair :

1.  **Interface Utilisateur (Streamlit)** : L'utilisateur pose une question (ex: *"Je veux aller de Châtelet à La Défense"*).
2.  **Router & Data Selection** : Le LLM analyse la demande pour décider s'il a besoin d'un dataset statique (CSV) ou d'une API temps réel.
3.  **RAG (Retrieval)** : Le système consulte un **Index de Connaissances** pour récupérer la documentation technique et le schéma approprié.
4.  **API Execution** : Construction et exécution de la requête vers l'API PRIM/RATP.
5.  **Response Generation** : Synthèse des données techniques en réponse naturelle.

## 🛠️ Stack Technique

* **Frontend** : Streamlit
* **Moteur IA** : LLM via API (ex: Google Gemini, Mistral AI)
* **Data Source** : API PRIM (Ile-de-France Mobilités) & Datasets Open Data

## 🚀 Installation et Démarrage

### 1. Cloner le projet
```bash
git clone https://github.com/Adelllllllll/Paris-Subway-Chatbot.git
cd Paris-Subway-Chatbot
```

### 2. Récupérer les données (Critique) ⚠️
Les fichiers de données volumineux (CSV) ne sont pas stockés sur GitHub.
1.  Téléchargez l'archive **`1_raw_data.zip`** via ce lien : [**Google Drive Link**](https://drive.google.com/drive/u/5/folders/12xumsjusEErf3lzNyObJuMtXUU20cGi-)
2.  Décompressez-la dans le dossier `data/` pour obtenir : `data/1_raw_data/datasets/...`

> *Pour plus de détails sur la construction des données, voir [data/DataPrep_README.md](data/DataPrep_README.md).*

### 3. Environnement Virtuel
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 4. Dépendances & Config
```bash
pip install -r requirements.txt
```
Créez un fichier `.env` à la racine et ajoutez vos clés :
```properties
LLM_API_KEY=votre_cle_api_ici
RATP_API_KEY=votre_cle_prim_ici
```

### 5. Lancer l'interface
```bash
streamlit run app.py
```

## 📂 Structure du Projet

```text
├── app.py                  # Point d'entrée Streamlit
├── backend/                # Cerveau de l'IA (Agent, Tools)
├── src/                    # Scripts utilitaires (Data Prep)
├── data/
│   ├── 1_raw_data/         # CSV Lourds (Non versionnés, voir Drive)
│   ├── 2_clean_markdown/   # Documentation nettoyée
│   └── 3_metadata/         # Index, Schémas et Swaggers (Le "Cerveau" Data)
├── requirements.txt
└── README.md
```

## 👤 Auteurs
Adel ZAIRI & Jiwoo CHOI