import os
from PIL import Image

def convert_png_to_webp(directory="."):
    """
    Convertit toutes les images PNG en WebP dans le répertoire spécifié
    et ses sous-répertoires.
    
    Les fichiers PNG originaux sont automatiquement supprimés après conversion réussie.
    La transparence est préservée et les pixels blancs transparents sont corrigés.
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
                    
                    # Préserver la transparence si présente (WebP supporte RGBA et LA)
                    # Convertir seulement les modes qui ne supportent pas la transparence
                    if img.mode == 'P':
                        # Mode palette : convertir en RGBA pour préserver la transparence
                        img = img.convert('RGBA')
                    elif img.mode not in ('RGBA', 'LA', 'RGB', 'L'):
                        # Convertir les autres modes en RGB
                        img = img.convert('RGB')
                    
                    # CORRECTION: Remplacer les pixels transparents blancs par des pixels noirs transparents
                    # Cela évite l'affichage d'un fond blanc quand alpha < 255
                    # Certains PNG ont des pixels blancs (255,255,255) avec alpha=0, ce qui crée un fond blanc visible
                    if img.mode == 'RGBA':
                        try:
                            # Méthode optimisée avec numpy (plus rapide)
                            import numpy as np
                            img_array = np.array(img)
                            
                            # Trouver les pixels transparents (alpha < 255)
                            alpha_channel = img_array[:, :, 3]
                            transparent_mask = alpha_channel < 255
                            
                            # Remplacer RGB par noir (0,0,0) pour les pixels transparents
                            img_array[transparent_mask, 0] = 0  # R
                            img_array[transparent_mask, 1] = 0  # G
                            img_array[transparent_mask, 2] = 0  # B
                            # Alpha reste inchangé
                            
                            # Reconvertir en Image PIL
                            img = Image.fromarray(img_array, 'RGBA')
                        except ImportError:
                            # Fallback si numpy n'est pas disponible (méthode plus lente mais fonctionnelle)
                            new_img = Image.new('RGBA', img.size, (0, 0, 0, 0))
                            pixels = img.load()
                            new_pixels = new_img.load()
                            
                            for y in range(img.size[1]):
                                for x in range(img.size[0]):
                                    r, g, b, a = pixels[x, y]
                                    # Si le pixel est transparent (alpha < 255), mettre RGB à noir
                                    if a < 255:
                                        new_pixels[x, y] = (0, 0, 0, a)  # Noir transparent
                                    else:
                                        new_pixels[x, y] = (r, g, b, a)  # Couleur originale
                            
                            img = new_img
                    
                    # Sauvegarder en WebP avec une qualité élevée
                    # La transparence sera préservée automatiquement pour RGBA et LA
                    # Utiliser lossless=False pour forcer la compression et éviter les problèmes de cache
                    img.save(webp_path, 'WEBP', quality=85, method=6, lossless=False)
                    
                    # Supprimer le fichier PNG original après conversion réussie
                    try:
                        os.remove(png_path)
                        print(f"[OK] Converti et supprimé: {png_path} -> {webp_path}")
                    except Exception as e:
                        print(f"[OK] Converti: {png_path} -> {webp_path}")
                        print(f"[AVERTISSEMENT] Impossible de supprimer {png_path}: {str(e)}")
                    
                    converted_count += 1
                    
                except Exception as e:
                    print(f"[ERREUR] Erreur lors de la conversion de {png_path}: {str(e)}")
    
    if converted_count == 0:
        print("Aucune image PNG trouvée à convertir.")
    else:
        print(f"\nConversion terminée! {converted_count} image(s) convertie(s).")

if __name__ == "__main__":
    print("Conversion des images PNG en WebP...")
    print("-" * 50)
    convert_png_to_webp()

