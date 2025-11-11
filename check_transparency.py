from PIL import Image
import sys

img_path = sys.argv[1] if len(sys.argv) > 1 else 'barber/male_2_4.png'
img = Image.open(img_path)
has_transparency = img.mode in ('RGBA', 'LA') or (hasattr(img, 'info') and 'transparency' in img.info)
print(f'Fichier: {img_path}')
print(f'Mode: {img.mode}')
print(f'A transparence: {has_transparency}')

