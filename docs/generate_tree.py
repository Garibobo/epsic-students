import os
import json

# Configuration
BASE_URL = "https://github.com/Garibobo/epsic-students/blob/main"
TARGET_DIRS = ["00-Administratif", "01-Cours"]
EXCLUDED_FILES = ["README.md"]
EXCLUDED_DIRS = ["docs"]

# Icon mapping based on file extension
ICON_MAP = {
    "pdf": "📑",
    "xlsx": "📄",
    "html": "📄",
    "css": "📄",
    "js": "📄",
    "jpg": "🖼️",
    "png": "🖼️",
    "md": "📄",
    "default": "📁"
}

def get_icon(filename):
    ext = filename.split('.')[-1].lower()
    return ICON_MAP.get(ext, ICON_MAP["default"])

def build_tree(path):
    tree = []
    for item in sorted(os.listdir(path)):
        full_path = os.path.join(path, item)
        rel_path = os.path.relpath(full_path, start=os.getcwd())
        if item in EXCLUDED_FILES or item in EXCLUDED_DIRS:
            continue
        if os.path.isdir(full_path):
            subtree = build_tree(full_path)
            tree.append({
                "name": item,
                "type": "folder",
                "icon": ICON_MAP["default"],
                "children": subtree
            })
        else:
            tree.append({
                "name": item,
                "type": "file",
                "icon": get_icon(item),
                "url": f"{BASE_URL}/{rel_path.replace(os.sep, '/')}"
            })
    return tree

# Build the full tree from target directories
full_tree = []
for target in TARGET_DIRS:
    if os.path.exists(target):
        full_tree.append({
            "name": target,
            "type": "folder",
            "icon": ICON_MAP["default"],
            "children": build_tree(target)
        })

# Assure que le dossier docs existe
os.makedirs("docs", exist_ok=True)

# Enregistre tree.json dans docs/
with open("docs/tree.json", "w", encoding="utf-8") as f:
    json.dump(full_tree, f, indent=2, ensure_ascii=False)

print("✅ tree.json has been generated successfully in docs/")
