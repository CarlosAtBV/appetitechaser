import bpy, bgl, blf,sys
import subprocess, time, math
import winsound

from bpy import data, ops, props, types, context

img_offX = 0
img_offY = 0
doCrop = bpy.data.scenes["Scene"].get("doCrop", 1)
bv_sitDist = 12#bpy.data.scenes["Scene"].get("sitdist", 0)
areWeSittin = False
render_angle = 0

import sys

def crop_image(orig_img):#, cropped_min_x, cropped_max_x, cropped_min_y, cropped_max_y):
	num_channels=orig_img.channels
	
	orig_size_x = orig_img.size[0]
	orig_size_y = orig_img.size[1]
	
	global img_offX
	global img_offY
	global areWeSittin
	global render_angle
	
	img_offX = bpy.data.scenes["Scene"].get("cx", orig_size_x//2)
	img_offY = bpy.data.scenes["Scene"].get("cy", orig_size_y)
	
	if(areWeSittin):
		print("we do be sittin")
		if(render_angle == 1 or render_angle == 3):
			img_offX -= bv_sitDist/2
		elif(render_angle == 2):
			img_offX -= bv_sitDist
		elif(render_angle == 5 or render_angle == 7):
			img_offX += bv_sitDist/2
		elif(render_angle == 6):
			img_offX += bv_sitDist
	
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
			pixelAlpha = safePixels[bx+3]
			#orig_img.pixels[orig_start_index+bx] = orig_img.pixels[orig_start_index+bx+3]
			#orig_img.pixels[orig_start_index+bx+1] = 0.0
			#orig_img.pixels[orig_start_index+bx+2] = 0.0
			#orig_img.pixels[orig_start_index+bx+3] = 0.0
			#print(str(pixelAlpha))
			if(pixelAlpha > 0.0):
				if(yy > cropped_max_y):
					#print('Max Y changed from '+str(cropped_max_y)+' to '+str(yy))
					cropped_max_y = yy
				elif(yy < cropped_min_y):
					#print('Min Y changed from '+str(cropped_min_y)+' to '+str(yy))
					cropped_min_y = yy
				elif(sizeIt > cropped_max_x):
					#print('Max X changed from '+str(cropped_max_x)+' to '+str(sizeIt))
					cropped_max_x = sizeIt
				elif(sizeIt < cropped_min_x):
					#print('Min X changed from '+str(cropped_min_x)+' to '+str(sizeIt))
					cropped_min_x = sizeIt
			sizeIt = sizeIt + 1

		#move to the next row before restarting loop
		current_cropped_row += 1
		
	cropped_max_y = min(cropped_max_y + 2,orig_size_y)
	
	#the slightest correction
	cropped_min_x = max(cropped_min_x - 1, 0)
	cropped_min_y = max(cropped_min_y - 1, 0)
	cropped_max_x = min(cropped_max_x + 1, orig_size_x)
	cropped_max_y = min(cropped_max_y + 1, orig_size_y)
	
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

cameraNames=''
scene = bpy.context.scene
framesgo = int(bpy.context.scene.frame_start)
framesleft = int(bpy.context.scene.frame_end)

def render_frames(layersToActivate, frameName, folderName):
	scene.layers = [l in layersToActivate for l in range(20)]
	
	c=0
	global areWeSittin
	global render_angle
	curFrame = framesgo
	render_onlyFront = 0

	render_angle = 0
	render_finalAngle = 8
	render_mirror = 0

	render_angleName = 0
			
	markers = bpy.context.scene.timeline_markers
	
	while (curFrame<=framesleft):
		render_angle = 0
		while (render_mirror == 1 and render_angle < (render_finalAngle/2)+1) or (render_mirror == 0 and render_angle < render_finalAngle):
			print("rendering new frame")
			
			areWeSittin = False
			print("check markers")
			for m in markers:
				if m.frame == curFrame:
					if m.name == 'ignore':
						curFrame = curFrame+1
						print("Ignored frame "+str(curFrame))
					elif m.name == 'dirfront':
						render_finalAngle = 1
						render_mirror = 0
					elif m.name == 'dirmirror':
						render_finalAngle = 8
						render_mirror = 1
					elif m.name == 'dirall':
						render_finalAngle = 8
					elif m.name == 'dirdouble':
						render_finalAngle = 16
					elif m.name == 'dirdoublemirror':
						render_finalAngle = 16
						render_mirror = 1
					elif m.name == 'dirkart':
						render_finalAngle = 40
						render_mirror = 1
					elif m.name == 'dirsit':
						render_finalAngle = 8
						print("Sit has been activated.\n\n\n")
						areWeSittin = True
					elif m.name == 'dirsitmirror':
						areWeSittin = True
			
			print("rotating")
			targetobj = bpy.data.objects['rotate']
			if(render_finalAngle == 16):
				targetobj.rotation_euler = (0,0,(0.392699)*render_angle)
			elif(render_finalAngle == 40):
				targetobj.rotation_euler = (0,0,3.14159-(0.157080)*render_angle)
			else:
				targetobj.rotation_euler = (0,0,(0.785398)*render_angle)
			print("setting frame")
			scene.frame_set(curFrame)
			
			print("setting sprite name")
			
			if(render_finalAngle == 1):
				render_angleName = str(myAlph[c])+str("0")
			elif (render_mirror == 1):
				myAmend = ""
				myAlphabet = ""
				
				if(render_finalAngle == 8):
					myAmend = myMirrorLess[render_angle]
					myAlphabet = str(render_angle+1)
				else:
					myAmend = myMirror[render_angle]
					myAlphabet = myList[render_angle]
				
				if(myAmend==""):
					render_angleName = str(myAlph[c])+myAlphabet
				else:
					render_angleName = str(myAlph[c])+myAlphabet+str(myAlph[c])+myAmend
					
			elif (render_finalAngle == 16):
				render_angleName = str(myAlph[c])+myList[render_angle]
			else:
				render_angleName = str(myAlph[c])+str(render_angle+1)
			
			print("creating render path")
			layerName_folder = folderName
			layerName_sprite = frameName
			renderPath = '//render/'+layerName_folder+'/'+layerName_sprite+str(render_angleName)
			
			print("setting render path")
			scene.render.filepath = renderPath
			
			print("rendering NOW!")
			bpy.ops.render.render( write_still=True )
			print("rendering DONE!")
			
			orig_img = bpy.data.images.load(scene.render.filepath+str('.png'))
			orig_size_x = orig_img.size[0]
			orig_size_y = orig_img.size[1]
			num_channels=orig_img.channels

			if (doCrop):
				cropped_img = crop_image(orig_img)
			
				cropped_img.file_format = 'PNG'
				cropped_img.filepath_raw = scene.render.filepath+str('.png')
				cropped_img.save()
			
			process = subprocess.Popen(['D:\Projects\RenderPipeline\compresssprite.bat', str(img_offX),str(img_offY), bpy.path.abspath(renderPath+str('.png'))])
			#winsound.PlaySound("D:/Projects/RenderPipeline/twip.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)

			render_angle = render_angle + 1
			
			overallProg = (curFrame/(framesleft))*100
			curProg = ((render_finalAngle-render_angle)/render_finalAngle)*(100/framesleft)
			print("~~~~ "+str(overallProg  -curProg)+"% Completed ~~~~", flush=True)
		
		c = c + 1
		curFrame = curFrame + 1
		winsound.PlaySound("D:/Projects/RenderPipeline/wooeep.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
	winsound.PlaySound("D:/Projects/RenderPipeline/dsk_warn.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)