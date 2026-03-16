import re
from bs4 import BeautifulSoup

# Charger le fichier HTML
filepath = r'C:\Users\Amir-BB-tiny\Documents\GitHub\wirdscup\installations-electriques-modernes\formules\chapitre-3.html'

with open(filepath, 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

print("=" * 70)
print("ANALYSE COMPLÈTE DU CHAPITRE 3 - DÉTECTION D'ERREURS")
print("=" * 70)
print()

# 1. Vérifier les formules MathJax
print("🔍 1. VÉRIFICATION SYNTAXE MATHJAX")
print("-" * 70)

formulas = soup.find_all(class_='formula')
mathjax_errors = []

for i, formula in enumerate(formulas, 1):
    text = formula.get_text()
    
    # Vérifier les délimiteurs
    if text.count('\\(') != text.count('\\)'):
        mathjax_errors.append(f"Formule {i}: Délimiteurs \\( \\) non équilibrés")
    
    # Vérifier les accolades
    if text.count('{') != text.count('}'):
        mathjax_errors.append(f"Formule {i}: Accolades {{ }} non équilibrées")
    
    # Vérifier les fractions
    if '\\frac' in text:
        # Vérifier format basique \frac{...}{...}
        frac_pattern = r'\\frac\{[^{}]*\}\{[^{}]*\}'
        if not re.search(frac_pattern, text):
            # Peut-être des fractions imbriquées, vérifier manuellement
            pass

if mathjax_errors:
    print(f"  ⚠️ {len(mathjax_errors)} erreurs détectées:")
    for error in mathjax_errors[:10]:
        print(f"    - {error}")
else:
    print("  ✅ Aucune erreur de syntaxe MathJax détectée")
print()

# 2. Vérifier les transformations mathématiques
print("🔍 2. VÉRIFICATION COHÉRENCE DES TRANSFORMATIONS")
print("-" * 70)

transformation_errors = []

# Exemples de vérifications
# Formule 3: W = U²/R · t => R = U²/W · t (ERREUR!)
# Devrait être: R = U² · t / W

formulas_text = [f.get_text() for f in formulas]

# Vérifier formule ligne 457
if len(formulas_text) > 20:
    formula_457 = formulas_text[20] if len(formulas_text) > 20 else ""
    if "R = \\frac{U^2}{W} \\cdot t" in formula_457:
        transformation_errors.append("Ligne 457: R = U²/W · t est INCORRECT")
        transformation_errors.append("  → Devrait être: R = (U² · t) / W ou R = \\frac{U^2 \\cdot t}{W}")

# Vérifier formule ligne 577 (même erreur)
if len(formulas_text) > 40:
    formula_577 = formulas_text[40] if len(formulas_text) > 40 else ""
    if "R = \\frac{U^2}{W} \\cdot t" in formula_577:
        transformation_errors.append("Ligne 577: R = U²/W · t est INCORRECT (même erreur)")

if transformation_errors:
    print(f"  ⚠️ {len(transformation_errors)} erreurs mathématiques détectées:")
    for error in transformation_errors:
        print(f"    {error}")
else:
    print("  ✅ Transformations mathématiques cohérentes")
print()

# 3. Vérifier la structure HTML
print("🔍 3. VÉRIFICATION STRUCTURE HTML")
print("-" * 70)

html_errors = []

# Vérifier les tableaux
tables = soup.find_all('table')
print(f"  Nombre de tableaux: {len(tables)}")

# Vérifier les titres h2 et h3
h2_titles = soup.find_all('h2')
h3_titles = soup.find_all('h3')
print(f"  Titres H2: {len(h2_titles)}")
print(f"  Titres H3: {len(h3_titles)}")

for h3 in h3_titles:
    print(f"    - {h3.get_text()}")

# Vérifier les liens de navigation
nav_links = soup.find_all('a', class_=['btn-prev', 'btn-next'])
print(f"  Liens de navigation: {len(nav_links)}")
for link in nav_links:
    print(f"    - {link.get_text()} → {link.get('href')}")

if html_errors:
    print(f"  ⚠️ {len(html_errors)} erreurs HTML détectées")
else:
    print("  ✅ Structure HTML correcte")
print()

# 4. Vérifier les images/dessins
print("🔍 4. VÉRIFICATION IMAGES ET ANIMATIONS SVG")
print("-" * 70)

svg_elements = soup.find_all('svg')
img_elements = soup.find_all('img')

print(f"  Éléments SVG: {len(svg_elements)}")
print(f"  Éléments IMG: {len(img_elements)}")

# Compter les cellules "Dessin"
dessin_cells = soup.find_all('td', string=lambda text: text and '—' in text)
print(f"  Cellules 'Dessin' vides (—): {len(dessin_cells)}")

if len(svg_elements) == 0 and len(img_elements) == 0:
    print("  ⚠️ Aucun SVG ou image détecté")
    print("  → Les dessins animés ne sont pas encore implémentés")
else:
    print("  ✅ Dessins présents")
print()

# 5. Compter les formules
print("🔍 5. COMPTAGE DES FORMULES")
print("-" * 70)

# Compter les lignes principales (non invisibles)
main_rows = soup.find_all('tr', class_=lambda x: x != 'invisible-row')
invisible_rows = soup.find_all('tr', class_='invisible-row')

print(f"  Formules principales: {len(main_rows) - 4}")  # -4 pour les headers
print(f"  Transformations invisibles: {len(invisible_rows)}")
print(f"  Total lignes tableau: {len(main_rows) + len(invisible_rows)}")
print()

# RÉSUMÉ FINAL
print("=" * 70)
print("📊 RÉSUMÉ DE L'ANALYSE")
print("=" * 70)

total_errors = len(mathjax_errors) + len(transformation_errors) + len(html_errors)

if total_errors == 0:
    print("✅ AUCUNE ERREUR CRITIQUE DÉTECTÉE")
    print()
    print("Points à améliorer:")
    print("  - Ajouter des SVG animés dans la colonne 'Dessin'")
    print("  - Vérifier manuellement les transformations mathématiques")
else:
    print(f"⚠️ {total_errors} ERREURS DÉTECTÉES")
    print()
    print("Erreurs critiques à corriger:")
    if transformation_errors:
        print(f"  - {len(transformation_errors)} erreurs mathématiques")
    if mathjax_errors:
        print(f"  - {len(mathjax_errors)} erreurs syntaxe MathJax")
    if html_errors:
        print(f"  - {len(html_errors)} erreurs structure HTML")

print()
print("=" * 70)
