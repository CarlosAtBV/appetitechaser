import os, subprocess
from PIL import Image, ImageDraw

myPath = (os.path.dirname(os.path.realpath(__file__)))+"/"
gamePath = myPath+"../../../TSP PK3/sprites/"

yOffset = -32

pics = [
	[ "comp/melee_idle-1-0.png", "weapons/mel/Bare Knuckle/111GA0.png" ],
	[ "comp/melee_idle-2-0.png", "weapons/mel/Bare Knuckle/111GB0.png" ],
	[ "comp/melee_idle-3-0.png", "weapons/mel/Bare Knuckle/111GC0.png" ],
	[ "comp/melee_idle-1-1.png", "weapons/mel/Bare Knuckle/111GD0.png" ],
	[ "comp/melee_idle-2-1.png", "weapons/mel/Bare Knuckle/111GE0.png" ],
	[ "comp/melee_idle-3-1.png", "weapons/mel/Bare Knuckle/111GF0.png" ],
	[ "comp/testpoke-1.png", "weapons/mel/Bare Knuckle/111YA0.png" ],
]

for picPair in pics:
	pic = picPair[0]
	path = picPair[1]
	toConvert = Image.open(myPath+pic)
	
	daBox = toConvert.getbbox()
	daSize = toConvert.size
	toConvert = toConvert.crop(daBox)
	offX = -(daBox[0] - daSize[0]) - (daSize[0]/2) - 160
	offY = -(daBox[1] - daSize[1]) - (daSize[1]/2) - 100 + 32
	
	picPath = gamePath+path
	print(picPath)
	toConvert.save(picPath)
	process = subprocess.Popen(['D:/Projects/RenderPipeline/grabpng.exe', '-grab', str(offX), str(offY), picPath]);