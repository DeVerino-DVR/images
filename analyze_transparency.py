from PIL import Image
import sys

img_path = sys.argv[1] if len(sys.argv) > 1 else 'barber/male_2_4.webp'
img = Image.open(img_path)

print(f'Fichier: {img_path}')
print(f'Mode: {img.mode}')
print(f'Size: {img.size}')

if img.mode == 'RGBA':
    alpha = img.split()[3]
    pixels = list(alpha.getdata())
    total = len(pixels)
    transparent = sum(1 for p in pixels if p < 255)
    opaque = total - transparent
    
    print(f'Total pixels: {total}')
    print(f'Pixels opaques (alpha=255): {opaque} ({opaque*100/total:.1f}%)')
    print(f'Pixels transparents (alpha<255): {transparent} ({transparent*100/total:.1f}%)')
    
    # Vérifier les coins pour voir s'il y a de la transparence
    corners = [
        (0, 0),  # Top-left
        (img.size[0]-1, 0),  # Top-right
        (0, img.size[1]-1),  # Bottom-left
        (img.size[0]-1, img.size[1]-1)  # Bottom-right
    ]
    print('\nAlpha values aux coins:')
    for x, y in corners:
        alpha_val = alpha.getpixel((x, y))
        print(f'  ({x}, {y}): alpha={alpha_val}')
else:
    print('Pas de canal alpha (mode:', img.mode, ')')

