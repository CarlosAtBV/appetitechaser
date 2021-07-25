import bpy, bgl, blf, sys
import subprocess, math
import winsound

from bpy import data, ops, props, types, context

#sys.path.append('D:/Projects/RenderPipeline/');

import render_crop2021

scene = bpy.context.scene;

frameStart = int(bpy.context.scene.frame_start);
frameEnd = int(bpy.context.scene.frame_end);

frameInfo = []
pathOverride = ""

dirLock_front = False;
b_doCrop = True;

offsets = (0, 0);

def refresh_markers():
	frameInfo.clear();
	global dirLock_front;
	
	for frame in range(0, frameEnd+1):
		newInfo = {}
		newInfo["ignore"] = False;
		newInfo["cssicon"] = False;
		newInfo["name"] = ""
		
		for m in scene.timeline_markers:
			if m.frame == frame:
				if m.name == "ignore":
					newInfo["ignore"] = True;
				elif m.name == "cssicon":
					newInfo["cssicon"] = True;
				elif m.name == "dirfront":
					dirLock_front = True;
				elif m.name == "sitframe":
					dirLock_front = False;
				else:
					newInfo["name"] = m.name;
					
		if dirLock_front:
			newInfo["dirfront"] = True;
		else:
			newInfo["dirfront"] = False;
			
		frameInfo.append(newInfo);
		
refresh_markers();

def set_scene(newScene):
	global scene;
	scene = newScene;
	bpy.context.screen.scene = newScene;
	
def set_offsets(offset):
	global offsets;
	offsets = offset;
	print("Setting offsets.");
	
def set_path(newPath):
	global pathOverride;
	pathOverride = newPath;
	
def set_crop(cropify):
	global b_doCrop;
	b_doCrop = cropify;
	
def get_offsets():
	global offsets;
	return offsets;
	
def get_scene():
	global scene;
	return scene;
	
def get_crop():
	global b_doCrop;
	return b_doCrop;

def render_frames(layersToActivate, frameName, folderName):
	global scene;
	global offsets;
	global b_doCrop;
	global renderedFirst;
	global pathOverride;
	
	scene.layers = [l in layersToActivate for l in range(20)]
	frameNum = 0
	rotateEmpty = bpy.data.objects["rotate"];
	
	for curFrame in range(frameStart, frameEnd+1):
		if ( frameInfo[curFrame]["ignore"] ) == True:
			continue;
		scene.frame_set(curFrame);
		render_doFront = ( frameInfo[curFrame]["dirfront"] or frameInfo[curFrame]["cssicon"] );
		for renderAngle in range(0, 8 if not render_doFront else 1):
			rotateEmpty.rotation_euler[2] = math.radians(360 * (renderAngle/8));
			stringAngle = str(renderAngle+1) if not render_doFront else str(0);
		
			if ( frameInfo[curFrame]["cssicon"] ):
				renderPath = 'D:/Projects/TombFetus/gamefiles/UI/patches/cssicons/CPOS' + frameName;
				renderedFirst = True;
			else:
				if ( len(pathOverride) ):
					renderPath = pathOverride + '/' + frameName + chr(65 + frameNum) + stringAngle;
				else:
					renderPath = '//render/' + folderName + '/' + frameName + chr(65 + frameNum) + stringAngle;
			scene.render.filepath = renderPath;
			bpy.ops.render.render( write_still=True );
			origImg = bpy.data.images.load(scene.render.filepath+str('.png'))
			
			print("Proceeding to crop.");
			
			if ( b_doCrop ):
				cropImg, pX, pY = render_crop2021.crop_image_to_offset(origImg, offsets[0], offsets[1]);
			else:
				cropImg, pX, pY = origImg, offsets[0], offsets[1];
			
			print("Finished cropping.");
			
			cropImg.file_format = 'PNG';
			cropImg.filepath_raw = scene.render.filepath+str('.png');
			cropImg.save();

			if ( b_doCrop ):
				process = subprocess.Popen(['D:\Projects\RenderPipeline\compresssprite.bat', str(pX), str(pY), bpy.path.abspath(cropImg.filepath_raw)]);
			
		winsound.PlaySound("D:/Projects/RenderPipeline/wooeep.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
		frameNum = frameNum + 1;
	winsound.PlaySound("D:/Projects/RenderPipeline/dsk_warn.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
	
def render_frames_by_markers(frameName, folderName):
	print("----------------------------------------------");
	print("----------------------------------------------");
	print("----------------------------------------------");
	print("Rendering by markers.");
	
	global pathOverride;
	
	willCrop = get_crop();
	theseOffsets = get_offsets();
	thisScene = get_scene();
	
	frameNum = 0
	
	for curFrame in range(frameStart, frameEnd+1):
		if ( frameInfo[curFrame]["ignore"] ) == True:
			continue;
			
		thisScene.frame_set(curFrame);
		
		if ( len(pathOverride) ):
			renderPath = pathOverride + '/' + frameInfo[curFrame]["name"];
		else:
			renderPath = '//render/' + folderName + "/" + frameInfo[curFrame]["name"];
		
		thisScene.render.filepath = renderPath;
		bpy.ops.render.render( write_still=True, scene=thisScene.name );
		origImg = bpy.data.images.load(thisScene.render.filepath+str('.png'))
		
		print("Proceeding to crop.");
		
		if ( willCrop ):
			cropImg, pX, pY = render_crop2021.crop_image_to_offset(origImg, theseOffsets[0], theseOffsets[1]);
		else:
			cropImg, pX, pY = origImg, theseOffsets[0], theseOffsets[1];
		
		print("Finished cropping.");
		
		cropImg.file_format = 'PNG';
		cropImg.filepath_raw = thisScene.render.filepath+str('.png');
		cropImg.save();

		if ( willCrop ):
			process = subprocess.Popen(['D:\Projects\RenderPipeline\compresssprite.bat', str(pX), str(pY), bpy.path.abspath(cropImg.filepath_raw)]);
			
		#winsound.PlaySound("D:/Projects/RenderPipeline/wooeep.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
	winsound.PlaySound("D:/Projects/RenderPipeline/dsk_warn.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)