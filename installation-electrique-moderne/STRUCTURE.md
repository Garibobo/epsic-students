# 📐 STRUCTURE DU PROJET - Installations Électriques Modernes

**Date de création** : 10 février 2026  
**Structure choisie** : Option 1 - Thématique Simple  
**Compatibilité** : Orfo2015 (actuel) + Orfo2026 (à partir d'août 2026)

---

## 🎯 OBJECTIF

Site internet moderne pour **expliquer en classe** les concepts d'électricité aux élèves du domaine 3.

---

## 📁 ARBORESCENCE COMPLÈTE

```
installations-electriques-modernes/
│
├── index.html                          ✅ Page d'accueil moderne (FAIT)
│
├── assets/                             ✅ Ressources statiques
│   ├── css/
│   │   ├── style.css                  ✅ Styles modernes (FAIT)
│   │   └── tribute-bubble.css         ✅ Bulle "Merci Denis" (FAIT)
│   ├── js/
│   │   └── main.js                    ✅ Scripts JavaScript (FAIT)
│   ├── images/                        📂 Images et icônes (VIDE)
│   └── fonts/                         📂 Polices personnalisées (VIDE)
│
├── pages/                              📂 Pages thématiques (À CRÉER)
│   ├── electrotechnique/              📄 Loi d'Ohm, résistances, condensateurs
│   ├── telecommunications/            📄 Téléphonie, réseaux, modulation
│   ├── installations/                 📄 Schémas, câblage, raccordements
│   ├── normes/                        📄 NIBT, DIT, sécurité
│   ├── eclairagisme/                  📄 Lampes, luminescence, calculs
│   ├── appareillage/                  📄 Contacteurs, moteurs, DDR, FI
│   └── magnetisme/                    📄 Champ magnétique, induction
│
├── formules/
│   └── index.html                     ✅ Formulaire technique MathJax + SVG (FAIT)
│
├── exercices/                          📂 Exercices et évaluations (À CRÉER)
│   ├── qcm/                           📄 Questions à choix multiples
│   ├── calculs/                       📄 Exercices de calcul
│   └── schemas/                       📄 Exercices de schémas
│
├── ressources/                         📂 Documents pédagogiques (À CRÉER)
│   ├── pdf/                           📄 Fiches PDF téléchargeables
│   ├── videos/                        📄 Capsules vidéo
│   └── documents/                     📄 Autres documents
│
├── README.md                           ✅ Documentation projet (FAIT)
├── STRUCTURE.md                        ✅ Ce fichier (FAIT)
└── .gitignore                          ✅ Fichiers à ignorer (FAIT)
```

---

## 📊 ÉTAT D'AVANCEMENT

### ✅ TERMINÉ (5 éléments)
1. **index.html** - Page d'accueil avec navigation moderne
2. **formules/index.html** - Formulaire technique avec MathJax et SVG animés
3. **assets/css/** - Styles modernes + bulle hommage Denis
4. **assets/js/** - Scripts JavaScript
5. **Structure complète** - Tous les dossiers créés

### 📂 EN ATTENTE (3 catégories)
1. **Pages thématiques** (7 sections à créer)
2. **Exercices** (3 types à développer)
3. **Ressources** (PDF, vidéos, documents)

---

## 🔄 MIGRATION DEPUIS ANCIEN SITE

### Source : `installations-electriques/`
- **Electr/** → `pages/electrotechnique/`
- **Telec/** → `pages/telecommunications/`
- **Instal/** → `pages/installations/`
- **Instal/NIBT/** → `pages/normes/`
- **Apelm/** → `pages/appareillage/`
- **Magnb/** → `pages/magnetisme/`
- **reponsesCFC/** → `exercices/`
- **cours/** → `ressources/documents/`

---

## 🎨 DESIGN ET TECHNOLOGIES

### Frontend
- **HTML5** - Structure sémantique
- **CSS3** - Grid, Flexbox, Animations
- **JavaScript ES6+** - Interactivité
- **MathJax** - Formules mathématiques
- **SVG** - Dessins techniques animés

### Responsive
- **Mobile** - Smartphones élèves
- **Tablette** - Utilisation en classe
- **Desktop** - Préparation cours enseignants

### Accessibilité
- **Langue** - Français uniquement
- **Navigation** - Claire et intuitive
- **Contenu** - Pédagogique et structuré

---

## 🚀 DÉPLOIEMENT

### GitHub Pages
```bash
# Le dossier installations-electriques-modernes sera déployé sur GitHub
# URL finale : https://[username].github.io/installations-electriques-modernes/
```

### Serveur Local (développement)
```bash
cd installations-electriques-modernes
python -m http.server 8000
# Ouvrir : http://localhost:8000/
```

---

## 📝 NOTES IMPORTANTES

1. **Orfo2015 vs Orfo2026**
   - Site compatible avec les deux ordonnances
   - Contenu actuel : Orfo2015 (élèves actuels)
   - Préparation : Orfo2026 (nouvelles volées dès août 2026)

2. **Usage en classe**
   - Site conçu pour **expliquer** les concepts
   - Support visuel pour enseignement
   - Formules et schémas interactifs

3. **Source**
   - Dossier `installations-electriques` = SOURCE (ne pas modifier)
   - Dossier `installations-electriques-modernes` = VERSION MODERNE (à développer)

---

**Créé par Amir Garibovic - Février 2026**
