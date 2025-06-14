import os, subprocess
from PIL import Image, ImageDraw

myPath = (os.path.dirname(os.path.realpath(__file__)))+"/"
gamePath = myPath+"../../../../TSP PK3/sprites/"

yOffset = -32

pics = [
	[ "0000.png", "weapons/mel/Darling Nikki/Spitfire/122GA0.png" ],
	[ "0001.png", "weapons/mel/Darling Nikki/Spitfire/122GB0.png" ],
	[ "0002.png", "weapons/mel/Darling Nikki/Spitfire/122GC0.png" ],
	[ "0003.png", "weapons/mel/Darling Nikki/Spitfire/122GD0.png" ],
	[ "0004.png", "weapons/mel/Darling Nikki/Spitfire/122GE0.png" ],
    
    # reload frames
    
	[ "0005.png", "weapons/mel/Darling Nikki/Spitfire/122RA0.png" ],
	[ "0006.png", "weapons/mel/Darling Nikki/Spitfire/122RB0.png" ],
	[ "0007.png", "weapons/mel/Darling Nikki/Spitfire/122RC0.png" ],
	[ "0008.png", "weapons/mel/Darling Nikki/Spitfire/122RD0.png" ],
	[ "0009.png", "weapons/mel/Darling Nikki/Spitfire/122RE0.png" ],
	[ "0010.png", "weapons/mel/Darling Nikki/Spitfire/122RF0.png" ],
	[ "0011.png", "weapons/mel/Darling Nikki/Spitfire/122RG0.png" ],
    
	[ "0012.png", "weapons/mel/Darling Nikki/Spitfire/122RQ0.png" ],
	[ "0013.png", "weapons/mel/Darling Nikki/Spitfire/122RR0.png" ],
	[ "0014.png", "weapons/mel/Darling Nikki/Spitfire/122RS0.png" ],
	[ "0015.png", "weapons/mel/Darling Nikki/Spitfire/122RT0.png" ],
	[ "0016.png", "weapons/mel/Darling Nikki/Spitfire/122RU0.png" ],
    
	[ "0026.png", "weapons/mel/Darling Nikki/Spitfire/122DA0.png" ],
	[ "0027.png", "weapons/mel/Darling Nikki/Spitfire/122DB0.png" ],
	[ "0028.png", "weapons/mel/Darling Nikki/Spitfire/122DC0.png" ],
	[ "0029.png", "weapons/mel/Darling Nikki/Spitfire/122DD0.png" ],
	[ "0030.png", "weapons/mel/Darling Nikki/Spitfire/122DE0.png" ],
    
	[ "0018.png", "weapons/mel/Darling Nikki/Spitfire/122AC0.png" ],
]

for picPair in pics:
	pic = "composite/"+picPair[0]
	path = picPair[1]
	toConvert = Image.open(myPath+pic)
	
	daBox = toConvert.getbbox()
	daSize = toConvert.size
	toConvert = toConvert.crop(daBox)
	offX = -(daBox[0] - daSize[0]) - (daSize[0]/2) - 160
	offY = -(daBox[1] - daSize[1]) - (daSize[1]/2) - 120 + 72
	
	picPath = gamePath+path
	print(picPath)
	toConvert.save(picPath)
	process = subprocess.Popen(['D:/Projects/RenderPipeline/grabpng.exe', '-grab', str(offX), str(offY), picPath]);