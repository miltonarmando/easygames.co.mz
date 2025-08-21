from PIL import Image
import sys

in_path = r"c:\Projects\easygames\Camada-69.png"
out_path = r"c:\Projects\easygames\favicon.ico"

try:
    img = Image.open(in_path).convert('RGBA')
    sizes = [(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)]
    img.save(out_path, format='ICO', sizes=sizes)
    print('Created', out_path)
except Exception as e:
    print('ERROR:', e)
    sys.exit(1)
