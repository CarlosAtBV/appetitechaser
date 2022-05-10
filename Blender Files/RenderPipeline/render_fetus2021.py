import bpy, bgl, blf, sys
import subprocess, math
import winsound

from bpy import data, ops, props, types, context

sys.path.append('D:/Projects/RenderPipeline/');

mirrorFrames = ['', '8', '7', '6', ''];

import render_crop2021

scene = bpy.context.scene;

frameStart = int(bpy.context.scene.frame_start);
frameEnd = int(bpy.context.scene.frame_end);

frameInfo = []
pathOverride = ""

dirLock = -1;
b_doCrop = True;

offsets = (0, 0);

def refresh_markers():
	frameInfo.clear();
	global dirLock;
	global frameEnd;
	
	frameEnd = int(bpy.context.scene.frame_end);
	
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
					dirLock = 1;
				elif m.name == "dirmirror":
					dirLock = 2;
				elif m.name == "sitframe":
					dirLock = -1;
				else:
					newInfo["name"] = m.name;
					
		if dirLock == 1:
			newInfo["dirfront"] = True;
			newInfo["dirmirror"] = False;
		elif dirLock == 2:
			newInfo["dirmirror"] = True;
			newInfo["dirfront"] = False;
		else:
			newInfo["dirmirror"] = False;
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
	#print("Setting offsets.");
	
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
	
	willCrop = get_crop();
	theseOffsets = get_offsets();
	
	scene.layers = [l in layersToActivate for l in range(20)]
	frameNum = 0
	rotateEmpty = bpy.data.objects["rotate"];
	
	for curFrame in range(frameStart, frameEnd+1):
		if ( frameInfo[curFrame]["ignore"] ) == True:
			continue;
		scene.frame_set(curFrame);
		render_doFront = ( frameInfo[curFrame]["dirfront"] or frameInfo[curFrame]["cssicon"] );
		render_doMirror = ( frameInfo[curFrame]["dirmirror"] );
		
		renderFramesMax = 8;
		if ( render_doMirror ):
			renderFramesMax = 5;
		elif ( render_doFront ):
			renderFramesMax = 1;
		
		for renderAngle in range(0, renderFramesMax):
			rotateEmpty.rotation_euler[2] = math.radians(360 * (renderAngle/8));
			stringAngle = str(renderAngle+1) if not render_doFront else str(0);
		
			if ( frameInfo[curFrame]["cssicon"] ):
				renderPath = 'D:/Projects/TombFetus/gamefiles/UI/patches/cssicons/CPOS' + frameName;
				renderedFirst = True;
			else:
				if ( render_doMirror and len(mirrorFrames[renderAngle]) > 0 ):
					frameBaseName = frameName + chr(65 + frameNum) + stringAngle + chr(65 + frameNum) + mirrorFrames[renderAngle];
				else:
					frameBaseName = frameName + chr(65 + frameNum) + stringAngle;
				if ( len(pathOverride) ):
					renderPath = pathOverride + '/' + frameBaseName;
				else:
					renderPath = '//render/' + folderName + '/' + frameBaseName;
			scene.render.filepath = renderPath;
			bpy.ops.render.render( write_still=True );
			origImg = bpy.data.images.load(scene.render.filepath+str('.png'))
			
			#print("Proceeding to crop.");
			
			if ( willCrop ):
				cropImg, pX, pY = render_crop2021.crop_image_to_offset(origImg, theseOffsets[0], theseOffsets[1]);
			else:
				cropImg, pX, pY = origImg, theseOffsets[0], theseOffsets[1];
			
			#print("Finished cropping.");
			
			cropImg.file_format = 'PNG';
			cropImg.filepath_raw = scene.render.filepath+str('.png');
			cropImg.save();

			if ( willCrop ):
				process = subprocess.Popen(['D:\Projects\RenderPipeline\compresssprite.bat', str(pX), str(pY), bpy.path.abspath(cropImg.filepath_raw)]);
			
			if ( renderAngle < renderFramesMax-1 ):
				print("f");
				#winsound.PlaySound("D:\\Projects\\RenderPipeline\\sounds\\switch.wav", winsound.SND_FILENAME|winsound.SND_ASYNC);
			else:
				if ( curFrame < frameEnd ):
					winsound.PlaySound("D:\\Resources\\Sound Effects\\Windows98Sounds\\Windows 98\\Windows 98 maximize.wav", winsound.SND_FILENAME|winsound.SND_ASYNC);
				else:
					winsound.PlaySound("D:\\Resources\\Sound Effects\\Windows98Sounds\\Inside Your Computer\\Inside your Computer startup.wav", winsound.SND_FILENAME|winsound.SND_ASYNC);
		frameNum = frameNum + 1;
	#winsound.PlaySound("D:\\Resources\\Sound Effects\\Windows98Sounds\\Windows 98\\Windows 98 maximize.wav", winsound.SND_FILENAME|winsound.SND_ASYNC);
	
def render_frames_by_markers(frameName, folderName):
	print("----------------------------------------------");
	print("----------------------------------------------");
	print("----------------------------------------------");
	print("Rendering by markers.");
	
	global pathOverride;
	global frameEnd;
	
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
		
		#print("Proceeding to crop.");
		
		if ( willCrop ):
			cropImg, pX, pY = render_crop2021.crop_image_to_offset(origImg, theseOffsets[0], theseOffsets[1]);
		else:
			cropImg, pX, pY = origImg, theseOffsets[0], theseOffsets[1];
		
		#print("Finished cropping.");
		
		cropImg.file_format = 'PNG';
		cropImg.filepath_raw = thisScene.render.filepath+str('.png');
		cropImg.save();

		if ( willCrop ):
			process = subprocess.Popen(['D:\Projects\RenderPipeline\compresssprite.bat', str(pX), str(pY), bpy.path.abspath(cropImg.filepath_raw)]);
			
		#winsound.PlaySound("D:/Projects/RenderPipeline/wooeep.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
	winsound.PlaySound("D:/Projects/RenderPipeline/dsk_warn.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
	
def its_done_now():
	winsound.PlaySound("D:\\Resources\\Sound Effects\\Windows98Sounds\\Inside Your Computer\\Inside your Computer startup.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)