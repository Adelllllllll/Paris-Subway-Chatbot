import requests
import os
import re
import time
from src.cleaner import html_to_markdown

# --- CONFIGURATION ---
INPUT_FILE = "data/Titres&Liens.md"
OUTPUT_DIR = "data/2_clean_markdown"
RAW_DIR = "data/1_raw_data/html"

# On se fait passer pour un navigateur classique pour éviter les blocages (403 Forbidden)
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
}

def setup_directories():
    """Crée l'arborescence des dossiers si elle n'existe pas."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(RAW_DIR, exist_ok=True)

def sanitize_filename(text):
    """Nettoie une chaîne pour en faire un nom de fichier valide."""
    # Remplace les accents et caractères spéciaux basiques
    text = text.replace(' ', '_').replace("'", "").lower()
    # Ne garde que les caractères alphanumériques et underscores
    return re.sub(r'[^\w\-]', '', text)

def extract_slug_from_url(url):
    """Extrait la dernière partie de l'URL pour nommer le fichier."""
    clean_url = url.rstrip('/')
    return clean_url.split('/')[-1]

def parse_input_file(filepath):
    """
    Lit le fichier Markdown d'entrée.
    Associe chaque URL au dernier Titre (H1, H2 ou H3) rencontré pour donner du contexte.
    """
    tasks = []
    current_context = "General"
    
    if not os.path.exists(filepath):
        print(f"❌ Erreur : Le fichier {filepath} est introuvable.")
        return []

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        
        # Si c'est un titre (H1, H2, H3...), on met à jour le contexte
        if line.startswith("#"):
            # On retire les # et on nettoie le texte
            clean_title = line.lstrip("#").strip()
            current_context = sanitize_filename(clean_title)
            
        # Si c'est une URL, on l'ajoute à la liste des tâches
        elif line.startswith("http"):
            tasks.append({
                "context": current_context,
                "url": line
            })
            
    return tasks

def run_scraper():
    setup_directories()
    tasks = parse_input_file(INPUT_FILE)
    
    if not tasks:
        return

    print(f"🚀 Démarrage du scraping de {len(tasks)} pages...\n")

    for i, task in enumerate(tasks, 1):
        url = task['url']
        context = task['context']
        slug = extract_slug_from_url(url)
        
        # Nom du fichier final : Categorie_NomDeLaPage.md
        filename_base = f"{context}__{slug}"
        print(f"[{i}/{len(tasks)}] Traitement : {slug} (Cat: {context})")
        
        try:
            # 1. Téléchargement
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            
            # Sauvegarde HTML Brut (Sécurité)
            raw_path = os.path.join(RAW_DIR, f"{filename_base}.html")
            with open(raw_path, 'w', encoding='utf-8') as f:
                f.write(response.text)

            # 2. Nettoyage & Conversion
            markdown_content = html_to_markdown(response.text)
            
            if markdown_content:
                # 3. Ajout Header Métatadonnées (Pour le LLM)
                # Cela aide le LLM a savoir d'où vient l'info
                file_header = (
                    f"---\n"
                    f"source_url: {url}\n"
                    f"categorie: {context}\n"
                    f"date_scrap: 2024-05-23\n"
                    f"---\n\n"
                )
                
                final_content = file_header + markdown_content
                
                # 4. Sauvegarde Markdown
                out_path = os.path.join(OUTPUT_DIR, f"{filename_base}.md")
                with open(out_path, 'w', encoding='utf-8') as f:
                    f.write(final_content)
            else:
                print(f"   ⚠️  Attention : Contenu vide après nettoyage pour {url}")

            # Petite pause pour être gentil avec le serveur
            time.sleep(0.5)

        except Exception as e:
            print(f"   ❌ Erreur : {e}")

    print("\n✅ Scraping terminé ! Les fichiers sont dans 'data/2_clean_markdown'")

if __name__ == "__main__":
    run_scraper()