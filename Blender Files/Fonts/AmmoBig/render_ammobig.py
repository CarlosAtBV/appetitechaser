import sys, bpy, os
import subprocess, math
sys.path.append('../../RenderPipeline/');
import render_crop2021

scene = bpy.context.scene

def renderFont(basePath):
	for curFrame in range(48, 57+1):
		getCode = format(curFrame, 'x');

		frameName = format(getCode, "0>4");

		bpy.data.objects["Text"].data.body = chr(curFrame);
		
		scene.render.filepath = basePath+frameName;
		bpy.ops.render.render(write_still = True);
		origImg = bpy.data.images.load(bpy.context.scene.render.filepath+str('.png'));
		cropImg, pX, pY = render_crop2021.crop_image_to_offset(origImg, 0, 0);

		cropImg.file_format = 'PNG';
		cropImg.filepath_raw = scene.render.filepath+str('.png');
		cropImg.save();

		process = subprocess.Popen([bpy.path.abspath('//../../RenderPipeline/compresssprite.bat'), str(0), str(pY), bpy.path.abspath(cropImg.filepath_raw)]);
		
renderFont('//../../../TSP PK3/fonts/tsp_ammo_big/');

bpy.data.objects["Text"].data.size *= 0.5;

renderFont('//../../../TSP PK3/fonts/tsp_ammo_small/');