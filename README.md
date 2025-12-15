# 🚇 Paris Subway Chatbot – RATP Assistant

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![RATP API](https://img.shields.io/badge/Data-RealTime-green)

## 📋 Contexte du Projet

Ce projet est un **Proof of Concept (POC)** d'un assistant conversationnel intelligent dédié aux usagers du métro parisien.

L'objectif est de démontrer comment une architecture **LLM modulaire** peut transformer une demande en langage naturel en requêtes API techniques précises, pour fournir des informations d'itinéraires et d'horaires en temps réel, tout en étant rigoureusement évalué.

## 🏗️ Architecture de la Solution

L'application repose sur un pipeline séquentiel clair, allant de l'augmentation du prompt à la génération finale.

### Flux de données (Data Flow)

1.  **Interface Utilisateur (Streamlit)** : L'utilisateur pose une question en langage naturel (ex: *"Je veux aller de Châtelet à La Défense, il est 14h"*).
2.  **Prompt Augmentation** : La requête brute est enrichie via un *System Prompt* qui injecte le contexte, la date actuelle et les consignes de comportement.
3.  **Router & Tool Selection** : Le modèle (LLM) analyse la demande enrichie pour décider quelle API interroger (Itinéraire, Horaires, Info Trafic) et construit la requête technique.
4.  **API Execution** : Le système interroge l'API RATP (ou Open Data) et récupère les données brutes (JSON).
5.  **Response Generation** : Le LLM synthétise les données techniques en une réponse naturelle et utile pour l'utilisateur.

### Pipeline d'Évaluation

Pour garantir la fiabilité, une boucle d'évaluation compare les sorties du chatbot avec des données de référence (Ground Truth) :
* **Input** : Dataset de questions types.
* **Process** : Génération de réponse par le bot.
* **Eval** : Comparaison sémantique et factuelle entre la réponse générée et les "documents véridiques" (réponse attendue) pour calculer un score de précision.

## 🛠️ Stack Technique

* **Frontend** : Streamlit
* **Moteur IA** : OpenAI GPT-4o / Mistral (via API)
* **Data Source** : API RATP / PRIM (Ile-de-France Mobilités)
* **Orchestration** : LangChain / Custom Python Logic
* **Évaluation** : Pytest + Framework d'eval (ex: Ragas ou DeepEval)

## 🚀 Installation et Démarrage

### 1. Cloner le projet

```bash
git clone [https://github.com/Adelllllllll/Paris-Subway-Chatbot.git](https://github.com/Adelllllllll/Paris-Subway-Chatbot.git)
cd Paris-Subway-Chatbot
```

### 2. Créer l'environnement virtuel

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```
### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configuration

```bash
MISTRAL_KEY=votre_cle_mistral
RATP_API_KEY=votre_cle_ratp
```

### 5. Lancer l'interface

```bash
streamlit run app.py
```

## 📂 Structure du Projet

├── app.py              # Point d'entrée Streamlit
├── backend/            
│   ├── core.py         # Logique du Chatbot (Prompt Augmentation)
│   ├── tools.py        # Connecteurs API RATP
│   └── prompts.py      # Templates de prompts
├── data/
│   └── eval_dataset.csv # Dataset de questions/réponses véridiques
├── evaluation/
│   └── evaluate.py     # Script de calcul des métriques
├── requirements.txt
└── README.md

## 👤 Auteur 
Adel ZAIRI & Jiwoo CHOI