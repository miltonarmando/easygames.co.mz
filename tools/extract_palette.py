from PIL import Image
from collections import Counter
import sys

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

if __name__ == '__main__':
    path = r"c:\Projects\easygames\Camada-69.png"
    try:
        img = Image.open(path).convert('RGBA')
    except Exception as e:
        print('ERROR: Could not open image:', e)
        sys.exit(1)

    # Resize to speed up
    img = img.resize((100, 100))

    pixels = list(img.getdata())
    # Filter out fully transparent pixels
    pixels = [p[:3] for p in pixels if p[3] > 128]

    if not pixels:
        print('ERROR: No opaque pixels found')
        sys.exit(2)

    # Count colors
    counts = Counter(pixels)
    most_common = counts.most_common(8)

    # Convert to hex and print
    hexes = [rgb_to_hex(c[0]) for c in most_common]
    print(' '.join(hexes))
