#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour remplacer le contenu principal de index.html par un conteneur vide
qui sera rempli dynamiquement au chargement
"""

import re

# Chemin du fichier index.html
index_path = r"C:\Users\Amir-BB-tiny\Documents\GitHub\wirdscup\installations-electriques-modernes\formules\index.html"

# Lire le fichier
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Trouver et remplacer le contenu entre <main class="main-content"> et </main>
# On garde juste un indicateur de chargement
pattern = r'(<main class="main-content">)(.*?)(</main>)'
replacement = r'\1\n            <!-- Le contenu sera chargé dynamiquement ici -->\n            <div style="text-align: center; padding: 100px 20px;">\n                <div style="font-size: 3rem; margin-bottom: 20px;">⏳</div>\n                <p style="font-size: 1.5rem; color: #667eea;">Chargement...</p>\n            </div>\n        \3'

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Sauvegarder le fichier
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Contenu principal de index.html remplacé par un conteneur vide!")
print("Le contenu sera chargé dynamiquement depuis content/home-content.html")
