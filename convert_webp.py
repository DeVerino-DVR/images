import os
from PIL import Image

def convert_png_to_webp(directory="webp"):
    """
    Convertit toutes les images PNG en WebP dans le répertoire spécifié.
    Les fichiers PNG originaux sont conservés.
    """
    converted_count = 0
    
    if not os.path.exists(directory):
        print(f"Le dossier '{directory}' n'existe pas.")
        return
    
    # Parcourir tous les fichiers dans le répertoire
    for file in os.listdir(directory):
        if file.lower().endswith('.png'):
            png_path = os.path.join(directory, file)
            # Créer le nom du fichier WebP (même nom mais extension .webp)
            webp_path = os.path.join(directory, os.path.splitext(file)[0] + '.webp')
            
            # Ignorer si le fichier WebP existe déjà
            if os.path.exists(webp_path):
                print(f"[SKIP] {webp_path} existe déjà")
                continue
            
            try:
                # Ouvrir l'image PNG
                img = Image.open(png_path)
                
                # Préserver la transparence si présente
                if img.mode == 'P':
                    img = img.convert('RGBA')
                elif img.mode not in ('RGBA', 'LA', 'RGB', 'L'):
                    img = img.convert('RGB')
                
                # CORRECTION: Remplacer les pixels transparents blancs par des pixels noirs transparents
                if img.mode == 'RGBA':
                    try:
                        import numpy as np
                        img_array = np.array(img)
                        
                        alpha_channel = img_array[:, :, 3]
                        transparent_mask = alpha_channel < 255
                        
                        img_array[transparent_mask, 0] = 0  # R
                        img_array[transparent_mask, 1] = 0  # G
                        img_array[transparent_mask, 2] = 0  # B
                        
                        img = Image.fromarray(img_array, 'RGBA')
                    except ImportError:
                        new_img = Image.new('RGBA', img.size, (0, 0, 0, 0))
                        pixels = img.load()
                        new_pixels = new_img.load()
                        
                        for y in range(img.size[1]):
                            for x in range(img.size[0]):
                                r, g, b, a = pixels[x, y]
                                if a < 255:
                                    new_pixels[x, y] = (0, 0, 0, a)
                                else:
                                    new_pixels[x, y] = (r, g, b, a)
                        
                        img = new_img
                
                # Sauvegarder en WebP avec une qualité élevée
                img.save(webp_path, 'WEBP', quality=85, method=6, lossless=False)
                
                print(f"[OK] Converti: {png_path} -> {webp_path}")
                converted_count += 1
                
            except Exception as e:
                print(f"[ERREUR] Erreur lors de la conversion de {png_path}: {str(e)}")
    
    if converted_count == 0:
        print("Aucune nouvelle image PNG à convertir.")
    else:
        print(f"\nConversion terminée! {converted_count} image(s) convertie(s).")

if __name__ == "__main__":
    print("Conversion des images PNG en WebP dans le dossier 'webp'...")
    print("-" * 50)
    convert_png_to_webp()
