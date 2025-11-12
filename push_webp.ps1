# Script PowerShell pour pousser les fichiers WebP dans une branche GitHub

$repoPath = Get-Location
$branchName = "webp"

Write-Host "Répertoire de travail: $repoPath" -ForegroundColor Cyan

# Vérifier si c'est un dépôt Git
if (-not (Test-Path ".git")) {
    Write-Host "Initialisation du dépôt Git..." -ForegroundColor Yellow
    git init
    git remote add origin https://github.com/jbaliveagain/fivem-clothes-images.git
}

# Vérifier le remote
Write-Host "`nVérification du remote..." -ForegroundColor Cyan
git remote -v

# Créer ou basculer sur la branche webp
Write-Host "`nCréation/basculement sur la branche '$branchName'..." -ForegroundColor Cyan
$branchExists = git branch -a | Select-String -Pattern $branchName
if ($branchExists) {
    Write-Host "La branche existe déjà, basculement..." -ForegroundColor Yellow
    git checkout $branchName
} else {
    Write-Host "Création de la nouvelle branche..." -ForegroundColor Yellow
    git checkout -b $branchName
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
    Write-Host "URL raw: https://raw.githubusercontent.com/jbaliveagain/fivem-clothes-images/$branchName/webp/" -ForegroundColor Green
} else {
    Write-Host "Aucun changement à commiter." -ForegroundColor Yellow
}
