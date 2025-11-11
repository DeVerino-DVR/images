from PIL import Image
import sys

img_path = sys.argv[1] if len(sys.argv) > 1 else 'barber/male_2_4.png'
img = Image.open(img_path)

print(f'Fichier: {img_path}')
print(f'Mode: {img.mode}')
print(f'Size: {img.size}')

if img.mode == 'RGBA':
    r, g, b, a = img.split()
    
    # Vérifier les coins pour voir les valeurs RGB
    corners = [
        (0, 0),  # Top-left
        (img.size[0]-1, 0),  # Top-right
        (0, img.size[1]-1),  # Bottom-left
        (img.size[0]-1, img.size[1]-1)  # Bottom-right
    ]
    
    print('\nAnalyse des coins (RGB + Alpha):')
    for x, y in corners:
        rgb_val = img.getpixel((x, y))
        alpha_val = rgb_val[3] if len(rgb_val) == 4 else 255
        rgb_only = rgb_val[:3]
        print(f'  ({x}, {y}): RGB={rgb_only}, Alpha={alpha_val}')
        
        # Vérifier si c'est blanc
        if rgb_only == (255, 255, 255) and alpha_val < 255:
            print(f'    [PROBLEME] Fond blanc dans RGB avec alpha transparent!')
        elif rgb_only == (255, 255, 255) and alpha_val == 255:
            print(f'    [PROBLEME] Fond blanc opaque dans l\'image originale!')
    
    # Vérifier une zone centrale pour voir si c'est vraiment transparent
    center_x, center_y = img.size[0] // 2, img.size[1] // 2
    center_rgb = img.getpixel((center_x, center_y))
    print(f'\nCentre de l\'image: RGB={center_rgb[:3]}, Alpha={center_rgb[3]}')
    
    # Compter les pixels blancs avec alpha transparent
    pixels = list(img.getdata())
    white_transparent = sum(1 for p in pixels if p[:3] == (255, 255, 255) and p[3] < 255)
    white_opaque = sum(1 for p in pixels if p[:3] == (255, 255, 255) and p[3] == 255)
    total = len(pixels)
    
    print(f'\nStatistiques:')
    print(f'  Pixels blancs opaques (fond blanc réel): {white_opaque} ({white_opaque*100/total:.1f}%)')
    print(f'  Pixels blancs transparents (problème): {white_transparent} ({white_transparent*100/total:.1f}%)')
    
else:
    print('Mode non-RGBA:', img.mode)

