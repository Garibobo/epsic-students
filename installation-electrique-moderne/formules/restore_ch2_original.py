#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Lire le fichier actuel
with open(r'C:\Users\Amir-BB-tiny\Documents\GitHub\wirdscup\installations-electriques-modernes\formules\content\chapitre-2-content.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Créer la version originale (tout dans une seule section)
new_content = []

# En-tête avec une seule section
new_content.append('<div class="container">\n')
new_content.append('                \n')
new_content.append('                <!-- Section 2: Couplages de résistances -->\n')
new_content.append('                <section id="couplages" class="content-section" style="position: relative;">\n')
new_content.append('                <!-- Bouton d\'impression Page 7 -->\n')
new_content.append('                <button onclick="printSection(\'couplages\')" style="position: absolute; top: 20px; right: 20px; z-index: 100; display: flex; align-items: center; gap: 8px; padding: 10px 18px; background: linear-gradient(135deg, #dc2626 0%, #991b1b 100%); color: white; border: none; border-radius: 10px; font-size: 0.95rem; font-weight: 600; cursor: pointer; box-shadow: 0 4px 12px rgba(220, 38, 38, 0.4); transition: all 0.3s;">\n')
new_content.append('                    <svg style="width: 20px; height: 20px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n')
new_content.append('                        <polyline points="6 9 6 2 18 2 18 9"></polyline>\n')
new_content.append('                        <path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path>\n')
new_content.append('                        <rect x="6" y="14" width="12" height="8"></rect>\n')
new_content.append('                    </svg>\n')
new_content.append('                    <span>Page 7</span>\n')
new_content.append('                </button>\n')
new_content.append('                \n')
new_content.append('                <h2 style="color: #000000;">\n')
new_content.append('                    <svg style="width: 64px; height: 64px; vertical-align: middle; margin-right: 15px;" viewBox="0 0 34 34" fill="none">\n')
new_content.append('                        <rect x="2" y="2" width="30" height="30" rx="5" fill="#e8f5ee" stroke="#1a5c35" stroke-width="1.8"/>\n')
new_content.append('                        <line x1="2" y1="17" x2="7" y2="17" stroke="#1a5c35" stroke-width="1.6"/>\n')
new_content.append('                        <rect x="7" y="13" width="6" height="8" rx="1" fill="white" stroke="#1a5c35" stroke-width="1.5"/>\n')
new_content.append('                        <line x1="13" y1="17" x2="18" y2="17" stroke="#1a5c35" stroke-width="1.6"/>\n')
new_content.append('                        <rect x="18" y="13" width="6" height="8" rx="1" fill="white" stroke="#1a5c35" stroke-width="1.5"/>\n')
new_content.append('                        <line x1="24" y1="17" x2="32" y2="17" stroke="#1a5c35" stroke-width="1.6"/>\n')
new_content.append('                    </svg>\n')
new_content.append('                    2. Couplages de résistances\n')
new_content.append('                </h2>\n')
new_content.append('                    \n')

# Récupérer tout le contenu des 3 sections (à partir de la ligne 49 du fichier actuel)
# On prend depuis le h2 "2.1 Circuit série" jusqu'à la fin de la dernière section
content_start = 49
# Trouver où se termine le contenu (avant le footer)
for i in range(len(lines)-1, 0, -1):
    if '</section>' in lines[i]:
        content_end = i
        break

# Ajouter tout le contenu
new_content.extend(lines[content_start:content_end])

# Fermer la section unique
new_content.append('                </section>\n')
new_content.append('                \n')
new_content.append('                <!-- Navigation footer -->\n')
new_content.append('                <div class="navigation-footer">\n')
new_content.append('                    <a href="index.html" class="nav-button">\n')
new_content.append('                        <svg style="width: 20px; height: 20px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n')
new_content.append('                            <path d="M19 12H5M12 19l-7-7 7-7"/>\n')
new_content.append('                        </svg>\n')
new_content.append('                        Retour à l\'accueil\n')
new_content.append('                    </a>\n')
new_content.append('                </div>\n')
new_content.append('            </div>\n')

# Écrire le nouveau fichier
with open(r'C:\Users\Amir-BB-tiny\Documents\GitHub\wirdscup\installations-electriques-modernes\formules\content\chapitre-2-content.html', 'w', encoding='utf-8') as f:
    f.writelines(new_content)

print('✅ Fichier restauré à la version AVANT séparation des sous-sections')
print(f'Total lignes originales: {len(lines)}')
print(f'Total lignes restaurées: {len(new_content)}')
