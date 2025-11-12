# Script PowerShell pour pousser les fichiers WebP dans la branche main (structure comme DeVerino-DVR/images)

$repoPath = Get-Location
$branchName = "main"

Write-Host "Répertoire de travail: $repoPath" -ForegroundColor Cyan

# Vérifier si c'est un dépôt Git
if (-not (Test-Path ".git")) {
    Write-Host "Initialisation du dépôt Git..." -ForegroundColor Yellow
    git init
    git remote add origin https://github.com/DeVerino-DVR/images.git
}

# Vérifier le remote
Write-Host "`nVérification du remote..." -ForegroundColor Cyan
git remote -v

# Basculer sur la branche main
Write-Host "`nBasculement sur la branche '$branchName'..." -ForegroundColor Cyan
$branchExists = git branch -a | Select-String -Pattern "main"
if ($branchExists) {
    git checkout main
} else {
    Write-Host "Création de la branche main..." -ForegroundColor Yellow
    git checkout -b main
}

# Ajouter les fichiers WebP du dossier webp
Write-Host "`nAjout des fichiers WebP..." -ForegroundColor Cyan
if (Test-Path "webp") {
    git add webp/*.webp
} else {
    Write-Host "Le dossier 'webp' n'existe pas!" -ForegroundColor Red
    exit 1
}

# Vérifier s'il y a des changements
Write-Host "`nVérification des changements..." -ForegroundColor Cyan
$status = git status --porcelain
if ($status) {
    Write-Host "Changements détectés:" -ForegroundColor Green
    git status --short
    
    Write-Host "`nCommit des fichiers WebP..." -ForegroundColor Cyan
    git commit -m "Add WebP converted images"
    
    Write-Host "`nPush vers GitHub..." -ForegroundColor Cyan
    git push -u origin $branchName
    
    Write-Host "`n✓ Terminé! Les fichiers WebP sont disponibles sur la branche '$branchName'" -ForegroundColor Green
    Write-Host "URL raw: https://raw.githubusercontent.com/DeVerino-DVR/images/main/webp" -ForegroundColor Green
    Write-Host "Exemple fichier: https://raw.githubusercontent.com/DeVerino-DVR/images/main/webp/female_1_0.webp" -ForegroundColor Green
} else {
    Write-Host 'Aucun changement a commiter.' -ForegroundColor Yellow
}
