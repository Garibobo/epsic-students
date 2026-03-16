from html.parser import HTMLParser

class HTMLValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.errors = []
        self.tags_stack = []
        
    def handle_starttag(self, tag, attrs):
        self.tags_stack.append(tag)
        
    def handle_endtag(self, tag):
        if self.tags_stack and self.tags_stack[-1] == tag:
            self.tags_stack.pop()
        else:
            self.errors.append(f"Balise fermante non correspondante: </{tag}>")

filepath = r'C:\Users\Amir-BB-tiny\Documents\GitHub\wirdscup\installations-electriques-modernes\formules\chapitre-3.html'

print("=" * 70)
print("VÉRIFICATION DES ERREURS HTML - CHAPITRE 3")
print("=" * 70)
print()

try:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    validator = HTMLValidator()
    validator.feed(content)
    
    print(f"✅ Fichier HTML analysé: {len(content)} caractères")
    print()
    
    if validator.errors:
        print(f"⚠️ {len(validator.errors)} erreurs détectées:")
        for i, error in enumerate(validator.errors[:20], 1):
            print(f"  {i}. {error}")
    else:
        print("✅ Aucune erreur HTML détectée par le parser")
    
    print()
    
    # Vérifier les balises non fermées
    if validator.tags_stack:
        print(f"⚠️ Balises potentiellement non fermées:")
        for tag in validator.tags_stack[-10:]:
            print(f"  - <{tag}>")
    else:
        print("✅ Toutes les balises sont correctement fermées")
    
    print()
    print("=" * 70)
    
except Exception as e:
    print(f"❌ Erreur lors de la lecture du fichier: {e}")
