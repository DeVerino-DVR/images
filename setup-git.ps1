# Script pour initialiser et pousser les images sur GitHub
# Usage: .\setup-git.ps1 <your-repository-link>

param(
    [Parameter(Mandatory=$false)]
    [string]$RepositoryLink = ""
)

Write-Host "=== Configuration Git pour le dépôt d'images ===" -ForegroundColor Cyan
Write-Host ""

# Vérifier si git est installé
try {
    $gitVersion = git --version
    Write-Host "✓ Git trouvé: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Git n'est pas installé. Veuillez installer Git d'abord." -ForegroundColor Red
    exit 1
}

# Initialiser le dépôt si nécessaire
if (-not (Test-Path .git)) {
    Write-Host "Initialisation du dépôt Git..." -ForegroundColor Yellow
    git init
    Write-Host "✓ Dépôt Git initialisé" -ForegroundColor Green
} else {
    Write-Host "✓ Dépôt Git déjà initialisé" -ForegroundColor Green
}

# Configurer la branche main
Write-Host "Configuration de la branche main..." -ForegroundColor Yellow
git branch -M main
Write-Host "✓ Branche main configurée" -ForegroundColor Green

# Ajouter le remote si fourni
if ($RepositoryLink -ne "") {
    Write-Host "Ajout du remote origin..." -ForegroundColor Yellow
    git remote remove origin 2>$null
    git remote add origin $RepositoryLink
    Write-Host "✓ Remote origin configuré: $RepositoryLink" -ForegroundColor Green
} else {
    Write-Host "⚠ Aucun lien de dépôt fourni. Ajoutez-le manuellement avec:" -ForegroundColor Yellow
    Write-Host "  git remote add origin <your-repository-link>" -ForegroundColor Gray
}

Write-Host ""
Write-Host "=== Ajout des fichiers ===" -ForegroundColor Cyan
git add .
Write-Host "✓ Fichiers ajoutés" -ForegroundColor Green

Write-Host ""
Write-Host "=== Création du commit ===" -ForegroundColor Cyan
git commit -m "add clothes"
Write-Host "✓ Commit créé" -ForegroundColor Green

Write-Host ""
Write-Host "=== Pousser vers GitHub ===" -ForegroundColor Cyan
if ($RepositoryLink -ne "") {
    Write-Host "Poussage vers origin/main..." -ForegroundColor Yellow
    git push -u origin main
    Write-Host "✓ Images poussées sur GitHub!" -ForegroundColor Green
} else {
    Write-Host "⚠ Pour pousser vers GitHub, exécutez:" -ForegroundColor Yellow
    Write-Host "  git push -u origin main" -ForegroundColor Gray
}

Write-Host ""
Write-Host "=== Terminé! ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Pour obtenir les liens des images:" -ForegroundColor Yellow
Write-Host "1. Accédez à votre dépôt GitHub" -ForegroundColor Gray
Write-Host "2. Cliquez sur une image pour l'ouvrir" -ForegroundColor Gray
Write-Host "3. Cliquez sur 'Raw' (Brut)" -ForegroundColor Gray
Write-Host "4. Copiez l'URL depuis votre navigateur" -ForegroundColor Gray

