# Script PowerShell pour mettre à jour le sidebar dans tous les fichiers de chapitres
# Lit le template du nouveau sidebar et le remplace dans chaque fichier

$templatePath = "C:\Users\Amir-BB-tiny\Documents\GitHub\wirdscup\installations-electriques-modernes\formules\_sidebar_template.html"
$chapitres = @(
    "chapitre-1.html",
    "chapitre-2.html",
    "chapitre-3.html",
    "chapitre-4.html",
    "chapitre-5.html"
)

# Lire le template du nouveau sidebar
$newSidebar = Get-Content $templatePath -Raw

Write-Host "Lecture du template sidebar..." -ForegroundColor Green

foreach ($chapitre in $chapitres) {
    $filePath = "C:\Users\Amir-BB-tiny\Documents\GitHub\wirdscup\installations-electriques-modernes\formules\$chapitre"
    
    if (Test-Path $filePath) {
        Write-Host "Traitement de $chapitre..." -ForegroundColor Yellow
        
        # Lire le contenu du fichier
        $content = Get-Content $filePath -Raw
        
        # Trouver et remplacer le sidebar
        # Pattern pour capturer tout le bloc <aside class="sidebar">...</aside>
        $pattern = '(?s)<aside class="sidebar">.*?</aside>'
        
        if ($content -match $pattern) {
            # Remplacer l'ancien sidebar par le nouveau
            $newContent = $content -replace $pattern, $newSidebar
            
            # Sauvegarder le fichier
            $newContent | Set-Content $filePath -NoNewline
            
            Write-Host "  ✓ $chapitre mis à jour avec succès" -ForegroundColor Green
        } else {
            Write-Host "  ✗ Sidebar non trouvé dans $chapitre" -ForegroundColor Red
        }
    } else {
        Write-Host "  ✗ Fichier $chapitre non trouvé" -ForegroundColor Red
    }
}

Write-Host "`nMise à jour terminée!" -ForegroundColor Cyan
Write-Host "Tous les chapitres ont maintenant le même volet de navigation." -ForegroundColor Cyan
