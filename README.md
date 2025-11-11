# Images pour inventaire, vêtements et coiffeur

Ce dépôt contient les images utilisées pour les inventaires, les vêtements et les coiffeurs.

## Installation

### Étape 1 - Installer Pillow

Installez la bibliothèque Pillow pour Python :

```bash
pip install Pillow
```

### Étape 2 - Convertir les images PNG en WebP (Recommandé)

Les images WebP sont plus légères et se chargent plus rapidement que les images PNG.

Exécutez le script de conversion :

```bash
python convert.py
```

Toutes les images PNG dans le dossier et ses sous-dossiers seront converties au format WebP.

### Étape 3 - Configuration Git

Si ce n'est pas déjà fait, initialisez le dépôt Git :

```bash
git init
git remote add origin <your-repository-link>
git branch -M main
```

⚠️ Remplacez `<your-repository-link>` par le lien HTTPS de votre dépôt GitHub.

### Étape 4 - Télécharger les images sur GitHub

```bash
git add .
git commit -m "add clothes"
git push -u origin main
```

### Étape 5 - Obtenir les liens des images

1. Accédez à votre dépôt GitHub
2. Cliquez sur une image pour l'ouvrir
3. Cliquez sur **Raw** (Brut)
4. Copiez l'URL depuis votre navigateur

Ce lien direct peut désormais être utilisé dans votre configuration, par exemple dans MClothes.

## Structure

- `clothing/` - Images de vêtements
- `barber/` - Images de coiffeur
