#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour mettre à jour les liens du sidebar dans index.html
pour utiliser des ancres (#chapitre-1, #chapitre-2, etc.) au lieu de fichiers séparés
"""

import re

# Chemin du fichier index.html
index_path = r"C:\Users\Amir-BB-tiny\Documents\GitHub\wirdscup\installations-electriques-modernes\formules\index.html"

# Lire le fichier
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remplacements à effectuer dans le sidebar
replacements = {
    'href="chapitre-1.html"': 'href="#chapitre-1"',
    'href="chapitre-2.html"': 'href="#chapitre-2"',
    'href="chapitre-3.html"': 'href="#chapitre-3"',
    'href="chapitre-4.html"': 'href="#chapitre-4"',
    'href="chapitre-5.html"': 'href="#chapitre-5"',
    
    # Sous-chapitres - remplacer chapitre-X.html#id par #chapitre-X (le sous-chapitre sera géré dans le contenu chargé)
    'href="chapitre-1.html#resistance-conducteurs"': 'href="#chapitre-1"',
    'href="chapitre-2.html#circuit-serie"': 'href="#chapitre-2"',
    'href="chapitre-2.html#circuit-parallele"': 'href="#chapitre-2"',
    'href="chapitre-2.html#resistance-ligne"': 'href="#chapitre-2"',
    'href="chapitre-2.html#diviseur-tension"': 'href="#chapitre-2"',
    'href="chapitre-3.html#compteur-energie"': 'href="#chapitre-3"',
    'href="chapitre-3.html#puissance-electrique"': 'href="#chapitre-3"',
    'href="chapitre-3.html#rendement"': 'href="#chapitre-3"',
}

# Appliquer les remplacements
for old, new in replacements.items():
    content = content.replace(old, new)

# Sauvegarder le fichier
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Liens du sidebar mis à jour avec succès!")
print("Les liens utilisent maintenant des ancres (#chapitre-1, #chapitre-2, etc.)")
