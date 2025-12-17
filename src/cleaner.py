from bs4 import BeautifulSoup
from markdownify import markdownify as md
import re

def html_to_markdown(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # 1. CIBLAGE PRÉCIS
    # On cherche d'abord la div spécifique identifiée lors du test
    # On utilise une regex pour trouver une classe qui contient "page-content"
    # car le suffixe "__pCHSm" pourrait changer selon les pages.
    main_content = soup.find('div', class_=re.compile(r'page-content', re.I))

    # Fallback : Si on ne trouve pas la classe spécifique, on se rabat sur <main>
    if not main_content:
        main_content = soup.find('main')

    if not main_content:
        return None

    # 2. NETTOYAGE
    # Suppression des éléments inutiles
    for tag in main_content(['script', 'style', 'nav', 'footer', 'iframe', 'svg', 'button', 'form']):
        tag.decompose()

    # Suppression des liens de navigation internes souvent présents (Retour, Imprimer)
    for a in main_content.find_all('a'):
        text = a.get_text(strip=True).lower()
        if text in ['retour', 'imprimer', 'haut de page']:
            a.decompose()

    # 3. CONVERSION EN MARKDOWN
    # strip=['img'] : On retire les images pour ne garder que le texte pur pour le LLM
    markdown_text = md(str(main_content), heading_style="ATX", strip=['img'])

    # 4. FINITIONS
    # Nettoyage des lignes vides multiples générées par la conversion
    clean_text = re.sub(r'\n{3,}', '\n\n', markdown_text).strip()
    
    return clean_text