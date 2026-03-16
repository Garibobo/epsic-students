#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour extraire le contenu principal de chaque chapitre
et créer des fichiers de contenu pur (sans sidebar ni structure HTML complète)
"""

import re
import os

# Dossier de base
base_dir = r"C:\Users\Amir-BB-tiny\Documents\GitHub\wirdscup\installations-electriques-modernes\formules"

# Liste des fichiers chapitres
chapitres = [
    "chapitre-1.html",
    "chapitre-2.html",
    "chapitre-3.html",
    "chapitre-4.html",
    "chapitre-5.html"
]

# Créer un dossier pour les contenus
content_dir = os.path.join(base_dir, "content")
os.makedirs(content_dir, exist_ok=True)

for chapitre_file in chapitres:
    chapitre_path = os.path.join(base_dir, chapitre_file)
    
    if not os.path.exists(chapitre_path):
        print(f"⚠️  Fichier {chapitre_file} non trouvé")
        continue
    
    print(f"Traitement de {chapitre_file}...")
    
    # Lire le fichier
    with open(chapitre_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extraire le contenu entre <main class="main-content"> et </main>
    match = re.search(r'<main class="main-content">(.*?)</main>', content, re.DOTALL)
    
    if match:
        main_content = match.group(1)
        
        # Nom du fichier de sortie
        output_file = os.path.join(content_dir, chapitre_file.replace('.html', '-content.html'))
        
        # Sauvegarder le contenu
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(main_content)
        
        print(f"  ✓ Contenu extrait vers {os.path.basename(output_file)}")
    else:
        print(f"  ✗ Impossible d'extraire le contenu de {chapitre_file}")

print("\n✅ Extraction terminée!")
print(f"Les fichiers de contenu sont dans le dossier: {content_dir}")
