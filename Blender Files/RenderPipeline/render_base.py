import math, bpy 

def crop_image(orig_img, origin_x = -1, origin_y = -1):#, cropped_min_x, cropped_max_x, cropped_min_y, cropped_max_y):
	num_channels=orig_img.channels
		
	orig_size_x = math.floor(orig_img.size[0])
	orig_size_y = math.floor(orig_img.size[1])
	
	if (origin_x == -1 and origin_y == -1):
		origin_x = orig_size_x//2
		origin_y = orig_size_y
	
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
	
	origin_x = origin_x - cropped_min_x
	print('New offset is '+str(origin_x))
		
	#calculate cropped image size
	cropped_size_x = cropped_max_x - cropped_min_x
	cropped_size_y = cropped_max_y - cropped_min_y
	#img_offY = img_offY - ((cropped_size_y) + cropped_min_y)
	#img_offY = (cropped_size_y) + cropped_min_y
	origin_y = origin_y-(orig_size_y-cropped_max_y)

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
		
	return cropped_img, origin_x, origin_y
	
def crop_image_weapon(orig_img):
	return crop_image(orig_img, (orig_img.size[0]/2)-160, 32)