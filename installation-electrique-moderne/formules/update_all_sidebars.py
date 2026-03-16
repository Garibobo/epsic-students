#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour mettre à jour le sidebar dans tous les fichiers de chapitres
avec le sidebar complet d'index.html
"""

import re
import os

# Lire le nouveau sidebar complet avec toutes les icônes SVG (chapitres 1-5 avec tous les sous-chapitres)
sidebar_path = r"C:\Users\Amir-BB-tiny\Documents\GitHub\wirdscup\installations-electriques-modernes\formules\_sidebar_complet_final.html"
with open(sidebar_path, 'r', encoding='utf-8') as f:
    new_sidebar = f.read()

# Liste des fichiers à mettre à jour
chapitres = [
    r"C:\Users\Amir-BB-tiny\Documents\GitHub\wirdscup\installations-electriques-modernes\formules\chapitre-1.html",
    r"C:\Users\Amir-BB-tiny\Documents\GitHub\wirdscup\installations-electriques-modernes\formules\chapitre-2.html",
    r"C:\Users\Amir-BB-tiny\Documents\GitHub\wirdscup\installations-electriques-modernes\formules\chapitre-3.html",
    r"C:\Users\Amir-BB-tiny\Documents\GitHub\wirdscup\installations-electriques-modernes\formules\chapitre-4.html",
    r"C:\Users\Amir-BB-tiny\Documents\GitHub\wirdscup\installations-electriques-modernes\formules\chapitre-5.html",
]

# Pattern pour trouver le sidebar (de <aside class="sidebar"> à </aside>)
pattern = r'<aside class="sidebar">.*?</aside>'

for chapitre_path in chapitres:
    if os.path.exists(chapitre_path):
        print(f"Traitement de {os.path.basename(chapitre_path)}...")
        
        # Lire le fichier
        with open(chapitre_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remplacer l'ancien sidebar par le nouveau
        new_content = re.sub(pattern, new_sidebar.strip(), content, flags=re.DOTALL)
        
        # Vérifier si le remplacement a été effectué
        if new_content != content:
            # Sauvegarder le fichier
            with open(chapitre_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  ✓ {os.path.basename(chapitre_path)} mis à jour avec succès")
        else:
            print(f"  ✗ Sidebar non trouvé dans {os.path.basename(chapitre_path)}")
    else:
        print(f"  ✗ Fichier {os.path.basename(chapitre_path)} non trouvé")

print("\n✅ Mise à jour terminée!")
print("Tous les chapitres ont maintenant le même volet de navigation qu'index.html")
