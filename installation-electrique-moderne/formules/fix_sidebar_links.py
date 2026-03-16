#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour corriger tous les liens du sidebar qui pointent vers chapitre-X.html
et les remplacer par #chapitre-X pour le système SPA
"""

import re

# Chemin du fichier index.html
index_path = r"C:\Users\Amir-BB-tiny\Documents\GitHub\wirdscup\installations-electriques-modernes\formules\index.html"

# Lire le fichier
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remplacements à effectuer
replacements = {
    # Chapitre 2 - sous-chapitres
    'href="chapitre-2.html#resistance-additionnelle"': 'href="#chapitre-2"',
    'href="chapitre-2.html#resistance-shunt"': 'href="#chapitre-2"',
    
    # Chapitre 4 - sous-chapitres
    'href="chapitre-4.html#production-chaleur"': 'href="#chapitre-4"',
    'href="chapitre-4.html#rendement-thermique"': 'href="#chapitre-4"',
    'href="chapitre-4.html#perte-conducteur"': 'href="#chapitre-4"',
    'href="chapitre-4.html#conversion-energies"': 'href="#chapitre-4"',
    'href="chapitre-4.html#densite-courant"': 'href="#chapitre-4"',
    'href="chapitre-4.html#effet-thermique-resistances"': 'href="#chapitre-4"',
    
    # Chapitre 5 - sous-chapitres
    'href="chapitre-5.html#formules-base"': 'href="#chapitre-5"',
    'href="chapitre-5.html#charge-pile"': 'href="#chapitre-5"',
    'href="chapitre-5.html#couplage-piles"': 'href="#chapitre-5"',
}

# Appliquer les remplacements
for old, new in replacements.items():
    content = content.replace(old, new)

# Sauvegarder le fichier
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Liens du sidebar corrigés!")
print(f"   - {len(replacements)} liens mis à jour")
print("   - Tous les liens pointent maintenant vers #chapitre-X")
