import os
import json
import glob
from pathlib import Path

# Configuration des chemins basés sur ton arborescence
BASE_DIR = Path(__file__).parent.parent
INPUT_DIR = BASE_DIR / "data" / "1_raw_data" / "raw_schemas"
OUTPUT_DIR = BASE_DIR / "data" / "3_metadata" / "schemas"

def extract_fields_recursive(data, fields_found=None):
    """
    Parcourt récursivement le JSON pour trouver tous les objets qui ressemblent 
    à des définitions de champs (ceux qui ont une 'description' ou un 'type').
    """
    if fields_found is None:
        fields_found = []

    if isinstance(data, dict):
        # Cas 1 : On tombe sur un bloc 'properties' (c'est souvent là que sont les champs)
        if 'properties' in data:
            for field_name, field_info in data['properties'].items():
                # Si c'est un champ "feuille" (qui a un type ou une description directe)
                if isinstance(field_info, dict) and ('type' in field_info or 'description' in field_info):
                    # On évite d'ajouter les conteneurs (comme "fields" ou "records" dans ton exemple)
                    # Sauf s'ils ont une description explicite, mais on préfère les types simples (string, int)
                    if field_info.get('type') != 'object' and field_info.get('type') != 'array':
                        fields_found.append({
                            "nom": field_name,
                            "type": field_info.get('type', 'Non spécifié'),
                            "description": field_info.get('description', 'Pas de description disponible')
                        })
                
                # Récursion : on plonge dans ce champ (cas des objets imbriqués)
                extract_fields_recursive(field_info, fields_found)
        
        # Cas 2 : On parcourt les 'definitions' ou autres clés du dictionnaire
        for key, value in data.items():
            if key != 'properties': # Déjà traité au-dessus
                extract_fields_recursive(value, fields_found)
                
    elif isinstance(data, list):
        for item in data:
            extract_fields_recursive(item, fields_found)

    return fields_found

def json_schema_to_markdown(json_path):
    """Lit un fichier JSON Schema et le convertit en tableau Markdown."""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Extraction intelligente des champs
        fields = extract_fields_recursive(data)
        
        if not fields:
            return None

        # Création du contenu Markdown
        filename = os.path.basename(json_path)
        md_content = f"# Schéma des données : {filename}\n\n"
        md_content += f"Ce document décrit la structure du fichier de données associé.\n\n"
        md_content += "| Nom du champ | Type | Description |\n"
        md_content += "| :--- | :--- | :--- |\n"
        
        for field in fields:
            # Nettoyage des sauts de ligne dans les descriptions pour ne pas casser le tableau
            desc = field['description'].replace('\n', ' ').replace('|', '-')
            md_content += f"| **{field['nom']}** | `{field['type']}` | {desc} |\n"
            
        return md_content

    except Exception as e:
        print(f"Erreur lors du traitement de {json_path}: {e}")
        return None

def main():
    # Création du dossier de sortie s'il n'existe pas
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    json_files = glob.glob(str(INPUT_DIR / "*.json"))
    print(f"🔍 {len(json_files)} schémas trouvés dans {INPUT_DIR}...")

    for json_file in json_files:
        md_output = json_schema_to_markdown(json_file)
        
        if md_output:
            # On garde le même nom de fichier mais en extension .md
            output_filename = Path(json_file).stem + ".md"
            output_path = OUTPUT_DIR / output_filename
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(md_output)
            print(f"✅ Converti : {output_filename}")
        else:
            print(f"⚠️ Ignoré (pas de champs trouvés) : {Path(json_file).name}")

if __name__ == "__main__":
    main()