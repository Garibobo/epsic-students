#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Lire le fichier original
with open(r'C:\Users\Amir-BB-tiny\Documents\GitHub\wirdscup\installations-electriques-modernes\formules\content\chapitre-2-content.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Créer le nouveau contenu restructuré
new_content = []

# Partie 1: Section principale (lignes 1-26 + fermeture)
new_content.extend(lines[0:26])  # Jusqu'au h2 inclus
new_content.append('\n')
new_content.append('                <p style="font-size: 1.1rem; line-height: 1.8; margin: 30px 0;">\n')
new_content.append('                    Ce chapitre présente les différents types de couplages de résistances électriques et leurs applications pratiques.\n')
new_content.append('                </p>\n')
new_content.append('                \n')
new_content.append('                <!-- Numérotation de page -->\n')
new_content.append('                <div class="page-number" style="text-align: center; margin-top: 40px; padding: 20px 0; font-size: 1.2rem; color: #667eea; font-weight: 600;">\n')
new_content.append('                    Page 7\n')
new_content.append('                </div>\n')
new_content.append('            </section>\n')
new_content.append('\n')

# Partie 2: Section 2.1 Circuit série (ligne 27-450)
new_content.append('            <!-- Section 2.1: Circuit série -->\n')
new_content.append('            <section id="circuit-serie" class="content-section" style="position: relative;">\n')
new_content.append('                <!-- Bouton d\'impression Page 8 -->\n')
new_content.append('                <button onclick="printSection(\'circuit-serie\')" style="position: absolute; top: 20px; right: 20px; z-index: 100; display: flex; align-items: center; gap: 8px; padding: 10px 18px; background: linear-gradient(135deg, #dc2626 0%, #991b1b 100%); color: white; border: none; border-radius: 10px; font-size: 0.95rem; font-weight: 600; cursor: pointer; box-shadow: 0 4px 12px rgba(220, 38, 38, 0.4); transition: all 0.3s;">\n')
new_content.append('                    <svg style="width: 20px; height: 20px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n')
new_content.append('                        <polyline points="6 9 6 2 18 2 18 9"></polyline>\n')
new_content.append('                        <path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path>\n')
new_content.append('                        <rect x="6" y="14" width="12" height="8"></rect>\n')
new_content.append('                    </svg>\n')
new_content.append('                    <span>Page 8</span>\n')
new_content.append('                </button>\n')
new_content.append('                \n')
# Changer h3 en h2 pour circuit-serie
line_27 = lines[26].replace('<h3 ', '<h2 ').replace('</h3>', '</h2>')
new_content.append(line_27)
new_content.extend(lines[27:450])  # Contenu jusqu'à circuit-parallele
new_content.append('                \n')
new_content.append('                <!-- Numérotation de page -->\n')
new_content.append('                <div class="page-number" style="text-align: center; margin-top: 40px; padding: 20px 0; font-size: 1.2rem; color: #667eea; font-weight: 600;">\n')
new_content.append('                    Page 8\n')
new_content.append('                </div>\n')
new_content.append('            </section>\n')
new_content.append('\n')

# Partie 3: Section 2.2 Circuit parallèle (ligne 451-976)
new_content.append('            <!-- Section 2.2: Circuit parallèle -->\n')
new_content.append('            <section id="circuit-parallele" class="content-section" style="position: relative;">\n')
new_content.append('                <!-- Bouton d\'impression Page 9 -->\n')
new_content.append('                <button onclick="printSection(\'circuit-parallele\')" style="position: absolute; top: 20px; right: 20px; z-index: 100; display: flex; align-items: center; gap: 8px; padding: 10px 18px; background: linear-gradient(135deg, #dc2626 0%, #991b1b 100%); color: white; border: none; border-radius: 10px; font-size: 0.95rem; font-weight: 600; cursor: pointer; box-shadow: 0 4px 12px rgba(220, 38, 38, 0.4); transition: all 0.3s;">\n')
new_content.append('                    <svg style="width: 20px; height: 20px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n')
new_content.append('                        <polyline points="6 9 6 2 18 2 18 9"></polyline>\n')
new_content.append('                        <path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path>\n')
new_content.append('                        <rect x="6" y="14" width="12" height="8"></rect>\n')
new_content.append('                    </svg>\n')
new_content.append('                    <span>Page 9</span>\n')
new_content.append('                </button>\n')
new_content.append('                \n')
# Changer h3 en h2 pour circuit-parallele
line_451 = lines[450].replace('<h3 ', '<h2 ').replace('</h3>', '</h2>')
new_content.append(line_451)
new_content.extend(lines[451:976])  # Contenu jusqu'à resistance-ligne
new_content.append('                \n')
new_content.append('                <!-- Numérotation de page -->\n')
new_content.append('                <div class="page-number" style="text-align: center; margin-top: 40px; padding: 20px 0; font-size: 1.2rem; color: #667eea; font-weight: 600;">\n')
new_content.append('                    Page 9\n')
new_content.append('                </div>\n')
new_content.append('            </section>\n')
new_content.append('\n')

# Partie 4: Section 2.3 Résistance et chute de tension (ligne 977-1744)
new_content.append('            <!-- Section 2.3: Résistance et chute de tension -->\n')
new_content.append('            <section id="resistance-ligne" class="content-section" style="position: relative;">\n')
new_content.append('                <!-- Bouton d\'impression Page 10 -->\n')
new_content.append('                <button onclick="printSection(\'resistance-ligne\')" style="position: absolute; top: 20px; right: 20px; z-index: 100; display: flex; align-items: center; gap: 8px; padding: 10px 18px; background: linear-gradient(135deg, #dc2626 0%, #991b1b 100%); color: white; border: none; border-radius: 10px; font-size: 0.95rem; font-weight: 600; cursor: pointer; box-shadow: 0 4px 12px rgba(220, 38, 38, 0.4); transition: all 0.3s;">\n')
new_content.append('                    <svg style="width: 20px; height: 20px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n')
new_content.append('                        <polyline points="6 9 6 2 18 2 18 9"></polyline>\n')
new_content.append('                        <path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path>\n')
new_content.append('                        <rect x="6" y="14" width="12" height="8"></rect>\n')
new_content.append('                    </svg>\n')
new_content.append('                    <span>Page 10</span>\n')
new_content.append('                </button>\n')
new_content.append('                \n')
# Changer h3 en h2 pour resistance-ligne
line_977 = lines[976].replace('<h3 ', '<h2 ').replace('</h3>', '</h2>')
new_content.append(line_977)
new_content.extend(lines[977:1744])  # Contenu jusqu'à </section>
new_content.append('                \n')
new_content.append('                <!-- Numérotation de page -->\n')
new_content.append('                <div class="page-number" style="text-align: center; margin-top: 40px; padding: 20px 0; font-size: 1.2rem; color: #667eea; font-weight: 600;">\n')
new_content.append('                    Page 10\n')
new_content.append('                </div>\n')
new_content.append('            </section>\n')

# Ajouter le reste (navigation footer)
new_content.extend(lines[1745:])

# Écrire le nouveau fichier
with open(r'C:\Users\Amir-BB-tiny\Documents\GitHub\wirdscup\installations-electriques-modernes\formules\content\chapitre-2-content.html', 'w', encoding='utf-8') as f:
    f.writelines(new_content)

print('✅ Fichier restructuré avec succès!')
print(f'Total lignes originales: {len(lines)}')
print(f'Total lignes nouvelles: {len(new_content)}')
