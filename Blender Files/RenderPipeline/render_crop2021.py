import math, bpy

doCropLeft = True;
doCropTop = True;

def crop_image_to_offset(orig_img, origin_x = -1, origin_y = -1):
	num_channels=orig_img.channels
	image_size_X = orig_img.size[0]
	image_size_Y = orig_img.size[1]
	
	global doCropLeft;
	global doCropTop;
	
	simpleArray = []

	#print("Creating array ...")
	
	for py in range(0, image_size_Y):
		simpleArray.append([]);
		startPos = (image_size_X * py) * 4;
		endPos = startPos + (image_size_X * 4);
		grabRow = orig_img.pixels[startPos : endPos];
		for px in range(0, len(grabRow), 4):
			newPixel = (grabRow[px], grabRow[px+1], grabRow[px+2], grabRow[px+3]);
			simpleArray[py].append(newPixel);

	#print("Image converted to array. Cropping now...")
	
	crop_right_X = 0;
	crop_left_X = image_size_X;
	
	crop_bottom_Y = 0;
	crop_top_Y = image_size_Y;
	
	for iy, py in enumerate(simpleArray):
		for ix, px in enumerate(py):
			pixelAlpha = px[3];
			if ( pixelAlpha != 0.0 ):
				#-------------------------
				if ( crop_right_X < ix+1 ):
					crop_right_X = ix+1;
				if ( crop_left_X > ix ):
					crop_left_X = ix;
				#-------------------------
				if ( crop_bottom_Y < iy+1 ):
					crop_bottom_Y = iy+1;
				if ( crop_top_Y > iy ):
					crop_top_Y = iy;

	#print("Grabbing modified size ...")
	
	if ( not doCropLeft ) : crop_left_X = 0;
	if ( not doCropTop ) : crop_bottom_Y = image_size_Y;
	
	final_size_X = crop_right_X - crop_left_X;
	final_size_Y = crop_bottom_Y - crop_top_Y;
	
	#print(final_size_X)
			
	final_img = bpy.data.images.new(name=orig_img.name+"_alt", alpha=True, width=final_size_X, height=final_size_Y)
	final_img.use_alpha = True
	final_img.alpha_mode = 'STRAIGHT'
	
	#print("Reconstruct the image ...");
	
	for py in range(0, final_size_Y):
		startFinal = (final_size_X * py) * 4;
		endFinal = startFinal + (final_size_X * 4);
		startOriginal = ((image_size_X * (crop_top_Y + py)) + crop_left_X) * 4;
		endOriginal = startOriginal + (final_size_X * 4);
		final_img.pixels[ startFinal : endFinal ] = orig_img.pixels[ startOriginal : endOriginal ];
	
	#print("COMPLETE!");
	
	# Now, fix up the origins
	#print(origin_x);
	#print(crop_left_X);
	#print("Crop bottom Y: "+str(crop_bottom_Y));
	#print("Image size is ("+str(image_size_X)+", "+str(image_size_Y)+")");
	#print("Old origin is ("+str(origin_x)+", "+str(origin_y)+")");
	origin_x = origin_x - crop_left_X;
	origin_y = origin_y - (image_size_Y - crop_bottom_Y);
	#print("New origin is ("+str(origin_x)+", "+str(origin_y)+")");

	return final_img, origin_x, origin_y;