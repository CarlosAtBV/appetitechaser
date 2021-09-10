import sys, bpy, os
import subprocess, math
sys.path.append('../../RenderPipeline/');
import render_crop2021

scene = bpy.context.scene

lengths = [];

render_crop2021.doCropLeft = False;

layers = [
    {
        "layers":[0],
		"path":'//../../../TSP PK3/fonts/tsp_ammo_big/',
    },
    {
        "layers":[1],
		"path":'//../../../TSP PK3/fonts/tsp_ammo_small/',
    },
    {
        "layers":[2],
		"path":'//../../../TSP PK3/fonts/tsp_ammo_tag/',
    },
];


def renderFont(basePath):
	for curFrame in range(48, 122+1):#57
		getCode = format(curFrame, 'x');

		frameName = format(getCode, "0>4");

		bpy.data.objects["Text"].data.body = chr(curFrame);
		bpy.data.objects["Text.002"].data.body = chr(curFrame);
		
		scene.render.filepath = basePath+frameName;
		bpy.ops.render.render(write_still = True);
		origImg = bpy.data.images.load(bpy.context.scene.render.filepath+str('.png'));
		cropImg, pX, pY = render_crop2021.crop_image_to_offset(origImg, 0, 0);

		cropImg.file_format = 'PNG';
		cropImg.filepath_raw = scene.render.filepath+str('.png');
		cropImg.save();

		process = subprocess.Popen([bpy.path.abspath('//../../RenderPipeline/compresssprite.bat'), str(0), str(pY), bpy.path.abspath(cropImg.filepath_raw)]);
		
for layer in layers:
	scene.layers = [l in layer["layers"] for l in range(20)];
	renderFont(layer["path"]);