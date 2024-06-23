import bpy, bgl, blf, sys
import subprocess, math

scene = bpy.context.scene
marker_curName = ""
marker_names = []
marker_it = 0

for frame in range(scene.frame_start, scene.frame_end+1):
	for m in scene.timeline_markers:
		if m.frame == frame:
			marker_it = 0
			marker_curName = m.name
	marker_names.append(marker_curName+"_"+str(marker_it))
	marker_it += 1
	
for frame in range(scene.frame_start, scene.frame_end+1):
	scene.frame_set(frame);
	
	scene.render.filepath = "//render/"+marker_names[0]
	marker_names.pop(0)
	bpy.ops.render.render(write_still=True)