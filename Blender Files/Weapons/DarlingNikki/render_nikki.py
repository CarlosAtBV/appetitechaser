import sys, bpy, os
sys.path.append('../../RenderPipeline/');
import render_fetus2021

scene = bpy.context.scene

for m in scene.timeline_markers:
	scene.timeline_markers.remove(m);
    
for i in range(scene.frame_start, scene.frame_end+1):
	scene.timeline_markers.new("P_122_"+str(i), frame=i);

render_fetus2021.refresh_markers();

render_fetus2021.set_offsets((0, 0));
render_fetus2021.set_path("//../../../TSP PK3/patches/weapons/nikki/spitfire/");
render_fetus2021.render_frames_by_markers("POSS", "finalrender");