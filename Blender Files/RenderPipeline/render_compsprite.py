# Render all cameras or cameras containing text given with command line argument "cameras".
# Example:
# Let's say test.blend file contains cameras "east.01", "east.02", "west.01", "west.02"
# By executing command "blender -b your_file.blend -P render_all_cameras.py" all 4 cameras will be rendered.
# Command "blender -b your_file.blend -P render_all_cameras.py  cameras=east" will render "east.01" and "east.02" cameras.
# Command "blender -b your_file.blend -P render_all_cameras.py  cameras=01" will render "east.01" and "west.01.02" cameras.

# For some reason, the cropping method here is WAY slower than the Tomb Fetus weapon renderer. Fix?


import bpy, bgl, blf,sys
import subprocess, time, math
from bpy import data, ops, props, types, context
print("\nThis Python script will render your scene with all available cameras")
print("or with camera(s) matching command line argument 'cameras'")
print("")
print("Usage:")
print("Render all cameras:")
print("blender -b your_file.blend -P render_all_cameras.py\n")
print("Render only matching cameras:")
print("blender -b your_file.blend -P render_all_cameras.py  cameras=east\n")

img_offX = 0
img_offY = 0
doCrop = bpy.data.scenes["Scene"].get("doCrop", 1)
isFont = bpy.data.scenes["Scene"].get("isFont", 0)
fontNum = 0
fontSuffix = 0

def crop_image(orig_img):#, cropped_min_x, cropped_max_x, cropped_min_y, cropped_max_y):
	'''Crops an image object of type <class 'bpy.types.Image'>.  For example, for a 10x10 image, 
	if you put cropped_min_x = 2 and cropped_max_x = 6,
	you would get back a cropped image with width 4, and 
	pixels ranging from the 2 to 5 in the x-coordinate

	Note: here y increasing as you down the image.  So, 
	if cropped_min_x and cropped_min_y are both zero, 
	you'll get the top-left of the image (as in GIMP).

	Returns: An image of type  <class 'bpy.types.Image'>
	'''

	num_channels=orig_img.channels
	#original image size
	orig_size_x = orig_img.size[0]
	orig_size_y = orig_img.size[1]
	
	global img_offX
	global img_offY
	
	img_offX = bpy.data.scenes["Scene"].get("cx", orig_size_x//2)#orig_size_x//2
	img_offY = bpy.data.scenes["Scene"].get("cy", orig_size_y)
	
	if(isFont):
		img_offX = 0
		img_offY = 0
	#img_offY = orig_size_y
	
	cropped_min_x = math.inf#orig_size_x//2
	cropped_max_x = -math.inf#orig_size_x//2
	cropped_min_y = math.inf#orig_size_y//2
	cropped_max_y = -math.inf#orig_size_y//2

	print("Exctracting image fragment, this could take a while...")
	
	current_cropped_row = 0
	for yy in range(0, orig_size_y):
		#the index we start at for copying this row of pixels from the original image
		orig_start_index = (0 + yy*orig_size_x) * num_channels
		#and to know where to stop we add the amount of pixels we must copy
		orig_end_index = orig_start_index + (orig_size_x * num_channels)

		#copy over pixels 	for bx in range(orig_start_index, orig_end_index):
		
		safePixels = orig_img.pixels[orig_start_index : orig_end_index]
		sizeIt = 0
		for bx in range(0, len(safePixels), 4):
			#pixelAlpha = safePixels[bx+3]
			pixelAlpha = orig_img.pixels[(orig_start_index)+(bx+3)]
			#orig_img.pixels[orig_start_index+bx] = orig_img.pixels[orig_start_index+bx+3]
			#orig_img.pixels[orig_start_index+bx+1] = 0.0
			#orig_img.pixels[orig_start_index+bx+2] = 0.0
			#orig_img.pixels[orig_start_index+bx+3] = 0.0
			#print(str(pixelAlpha))
			#print(str(sizeIt))
			#print(str(sizeIt)+" < +"+str(cropped_min_x)+" = "+str(sizeIt < cropped_min_x))
			if(pixelAlpha >= 0.1):
				if(yy > cropped_max_y):
					#print('Max Y changed from '+str(cropped_max_y)+' to '+str(yy))
					cropped_max_y = yy
				if(yy < cropped_min_y):
					#print('Min Y changed from '+str(cropped_min_y)+' to '+str(yy))
					cropped_min_y = yy
				if(sizeIt > cropped_max_x):
					#print('Max X changed from '+str(cropped_max_x)+' to '+str(sizeIt))
					#print('Max X changed from '+str(cropped_max_x)+' to '+str(sizeIt))
					cropped_max_x = sizeIt
					#orig_img.pixels[bx] = 1.0
					#orig_img.pixels[bx+1] = 0.0
					#orig_img.pixels[bx+2] = 0.0
				if(sizeIt < cropped_min_x):
					#print('Min X changed from '+str(cropped_min_x)+' to '+str(sizeIt))
					#print('Min X changed from '+str(cropped_min_x)+' to '+str(sizeIt))
					cropped_min_x = sizeIt
					#orig_img.pixels[bx] = 1.0
					#orig_img.pixels[bx+1] = 0.0
					#orig_img.pixels[bx+2] = 0.0
			sizeIt = sizeIt + 1
		#if(cropped_min_x!=math.inf):
		#	thisPixel = orig_start_index + cropped_min_x*num_channels
		#	orig_img.pixels[thisPixel] = 1.0
		#	orig_img.pixels[thisPixel+1] = 0.0
		#	orig_img.pixels[thisPixel+2] = 0.0
		#	orig_img.pixels[thisPixel+3] = 1.0

		#move to the next row before restarting loop
		current_cropped_row += 1
		
	#cropped_max_y = min(cropped_max_y + 2,orig_size_y)
	
	cropped_max_y = cropped_max_y+1
	cropped_max_x = cropped_max_x+1
	
	#the slightest correction
	cropped_min_x = max(cropped_min_x, 0)#max(cropped_min_x - 1, 0)
	cropped_min_y = max(cropped_min_y, 0)#max(cropped_min_y - 1, 0)
	cropped_max_x = min(cropped_max_x, orig_size_x)#min(cropped_max_x + 1, orig_size_x)
	cropped_max_y = min(cropped_max_y, orig_size_y)#min(cropped_max_y + 1, orig_size_y)
	
	img_offX = img_offX - cropped_min_x
	print('New offset is '+str(img_offX))
		
	#calculate cropped image size
	cropped_size_x = cropped_max_x - cropped_min_x
	cropped_size_y = cropped_max_y - cropped_min_y
	#img_offY = img_offY - ((cropped_size_y) + cropped_min_y)
	#img_offY = (cropped_size_y) + cropped_min_y
	img_offY = img_offY-(orig_size_y-cropped_max_y)

	cropped_img = bpy.data.images.new(name="cropped_img", alpha=True, width=cropped_size_x, height=cropped_size_y)
	cropped_img.use_alpha = True
	cropped_img.alpha_mode = 'STRAIGHT'

	#loop through each row of the cropped image grabbing the appropriate pixels from original
	#the reason for the strange limits is because of the 
	#order that Blender puts pixels into a 1-D array.
	
	current_cropped_row = 0
	for yy in range(cropped_min_y, cropped_max_y):#range(orig_size_y - cropped_max_y, orig_size_y - cropped_min_y):
		#the index we start at for copying this row of pixels from the original image
		orig_start_index = (cropped_min_x + yy*orig_size_x) * num_channels
		#and to know where to stop we add the amount of pixels we must copy
		orig_end_index = orig_start_index + (cropped_size_x * num_channels)
		#the index we start at for the cropped image
		cropped_start_index = (current_cropped_row * cropped_size_x) * num_channels 
		cropped_end_index = cropped_start_index + (cropped_size_x * num_channels)

		#copy over pixels 
		cropped_img.pixels[cropped_start_index : cropped_end_index] = orig_img.pixels[orig_start_index : orig_end_index]

		#move to the next row before restarting loop
		current_cropped_row += 1

	return cropped_img

myList=["1","9","2","A","3","B","4","C","5","D","6","E","7","F","8","G"]
myMirror=["","G","8","F","7","E","6","D",""]
myMirrorLess=["","8","7","6",""]
myAlph=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
picNames=["RND0","RND1","RND2","RND3","RND4","RND5","RND6","RND7","RND8","RND9"]
moreVisible=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
rotations_allAround = ["*1","*2","*3","*4","*5","*6","*7","*8"]
rotations_mirrored = ["*1","*2*8","*3*7","*4*6","*5"]

fontNames=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

cameraNames=''
scene = bpy.context.scene
framesleft = int(bpy.context.scene.frame_end)

# Loop all command line arguments and try to find "cameras=east" or similar
for arg in sys.argv:
	words=arg.split('=')	
	if ( words[0] == 'cameras'):
		cameraNames = words[1]

print('rendering cameras containing [' + cameraNames + ']')

print('\nPrint Scenes...')
sceneKey = bpy.data.scenes.keys()[0]
print('Using Scene['  + sceneKey + ']')

# Loop all objects and try to find Cameras
c=0
curFrame = 1

render_framePrefix = bpy.data.scenes["Scene"].get("sprName", "RND0")
render_frameFrame = "A"
render_frameRotate = 0
render_mirror = False

while (curFrame<=framesleft):
#for x in range(0, 8):
	render_frameName = "AAFUCKIT"
	markers = bpy.context.scene.timeline_markers
	doRender = True#0
	addFontFrame = True
	for m in markers:
		#print(m.name + ' frame is ' + m.frame + ' and the current frame is ' + curFrame)
		if m.frame == curFrame:
			if(isFont):
				fontNum = int(m.name[0])
				for fuk in range(0,len(fontNames)):
					if(m.name[1] == fontNames[fuk]):
						fontSuffix = fuk
						break
				addFontFrame = False
			else:
				render_mirror = False
				if(m.name.find("[mir]")!=-1):
					render_mirror = True
				if(m.name.find("[new]")!=-1):
					render_framePrefix = "RND1"
				newStr = m.name.replace("[mir]","")
				newStr = newStr.replace("[new]","")
				render_frameFrame = newStr[0]
				render_frameRotate = 0
			#doRender = 1
			
	if(isFont):
		if(addFontFrame==True):
			fontSuffix = fontSuffix+1
			if(fontSuffix >= len(fontNames)):
				fontSuffix = 0
				fontNum = fontNum+1
		render_frameName = "00"+str(fontNum)+str(fontNames[fontSuffix])
	else:
		if(render_mirror):
			render_frameName = render_framePrefix+str(rotations_mirrored[render_frameRotate].replace("*",render_frameFrame))
		else:
			render_frameName = render_framePrefix+render_frameFrame+"0"
		render_frameRotate = render_frameRotate+1
			
	if(doRender == False and isFont==False):
		curFrame = curFrame+1
		continue
	
	scene.frame_set(curFrame)
	
	bpy.data.scenes[sceneKey].render.filepath = '//render_blend/'+str(render_frameName)
	bpy.ops.render.render( write_still=True )
	
	orig_img = bpy.data.images.load(bpy.data.scenes[sceneKey].render.filepath+str('.png'))
	print('obtaining sizes')
	orig_size_x = orig_img.size[0]
	orig_size_y = orig_img.size[1]
	num_channels=orig_img.channels

	#cropped_img = crop_image(orig_img, 0, 64, 0, 64)
	if (doCrop):
		cropped_img = crop_image(orig_img)
	
		cropped_img.file_format = 'PNG'
		cropped_img.filepath_raw = bpy.data.scenes[sceneKey].render.filepath+str('.png')
		cropped_img.save()
	
	process = subprocess.Popen(['D:/Projects/TombFetus/models/player/grabpng', '-grab',str(img_offX),str(img_offY), bpy.path.abspath(bpy.data.scenes[sceneKey].render.filepath+str('.png'))])
	#bpy.path.abspath(cropped_img.filepath_raw)])#, '.png"'])
	process.wait()
	process = subprocess.Popen(['D:/Projects/TombFetus/models/player/pngout', bpy.path.abspath(bpy.data.scenes[sceneKey].render.filepath+str('.png')), '-kgrAb','-y','-c6', ])
	process.wait()
	
	curFrame = curFrame + 1
print('Done!') 