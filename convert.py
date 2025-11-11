import os
from PIL import Image

def convert_png_to_webp(directory="."):
    """
    Convertit toutes les images PNG en WebP dans le répertoire spécifié
    et ses sous-répertoires.
    """
    converted_count = 0
    
    # Parcourir tous les fichiers dans le répertoire et ses sous-répertoires
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.png'):
                png_path = os.path.join(root, file)
                # Créer le nom du fichier WebP (même nom mais extension .webp)
                webp_path = os.path.join(root, os.path.splitext(file)[0] + '.webp')
                
                try:
                    # Ouvrir l'image PNG
                    img = Image.open(png_path)
                    
                    # Convertir en RGB si nécessaire (WebP ne supporte pas la transparence RGBA directement)
                    if img.mode in ('RGBA', 'LA'):
                        # Créer un fond blanc pour les images avec transparence
                        background = Image.new('RGB', img.size, (255, 255, 255))
                        if img.mode == 'RGBA':
                            background.paste(img, mask=img.split()[3])  # Utiliser le canal alpha comme masque
                        else:
                            background.paste(img)
                        img = background
                    elif img.mode != 'RGB':
                        img = img.convert('RGB')
                    
                    # Sauvegarder en WebP avec une qualité élevée
                    img.save(webp_path, 'WEBP', quality=85)
                    print(f"✓ Converti: {png_path} -> {webp_path}")
                    converted_count += 1
                    
                except Exception as e:
                    print(f"✗ Erreur lors de la conversion de {png_path}: {str(e)}")
    
    if converted_count == 0:
        print("Aucune image PNG trouvée à convertir.")
    else:
        print(f"\nConversion terminée! {converted_count} image(s) convertie(s).")

if __name__ == "__main__":
    print("Conversion des images PNG en WebP...")
    print("-" * 50)
    convert_png_to_webp()

