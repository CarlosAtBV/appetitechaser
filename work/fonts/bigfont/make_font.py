import os
import sys
import pyperclip
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path);

from PIL import Image, ImageDraw, ImageFont

# 1. Open an image or create a new one (here, creating a white image)
# If you have an image file, use: img = Image.open("your_image.jpg").convert("RGB")
img = Image.new('RGBA', (2048, 2048), color = (255, 255, 255, 0)) # white background
imgTest = Image.new('RGBA', (2048, 2048), color = (255, 255, 255, 0)) # white background

# 2. Create an ImageDraw object
draw = ImageDraw.Draw(img)

#font = ImageFont.truetype("D:/Fonts/unknown/c_c_red_alert_inet/C&C Red Alert [LAN].ttf", 26)
font = ImageFont.truetype(dir_path+"/Audiowide-Regular.ttf", 72)

letters = """
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789
.,:;'!?@#$%^&*()
-_/\\^*[]{}\"Ññ
"""

offY = -20
offY = -4

for ltr in letters:
	print("Doing "+ltr)
	img = Image.new('RGBA', (128, 88), (0, 0, 0, 0))
	draw = ImageDraw.Draw(img)
	#draw.text((6,3+offY), ltr, fill=(0,0,0), font=font)
	#draw.text((5,2+offY), ltr, fill=(16,16,16), font=font)
	#draw.text((4,1+offY), ltr, fill=(32,32,32), font=font)
	draw.text((5,2+offY), ltr, fill=(0,0,0), font=font)
	draw.text((4,1+offY), ltr, fill=(32,32,32), font=font)
	draw.text((3,offY), ltr, fill=(255,255,255), font=font)
	#img = img.resize((int(img.size[0]*0.95), img.size[1]), Image.Resampling.LANCZOS)
	bbox = img.getbbox()
	if ( bbox == None ): continue
	img = img.crop((bbox[0], 0, bbox[2], bbox[1]+bbox[3]))
	outPath = dir_path+f"/../../../TSP PK3/fonts/tsp_large/{ord(ltr):04x}.png"
	img.save(outPath)
	print(ltr)