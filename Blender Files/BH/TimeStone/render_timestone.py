import sys, bpy
sys.path.append('../../RenderPipeline/');
import render_fetus2021

scene = bpy.context.scene

render_fetus2021.set_offsets((32, 72));
render_fetus2021.set_path("//../../../TSP PK3/sprites/bh/timestone/");

scene.layers = [l in [0] for l in range(20)];

for m in scene.timeline_markers:
	scene.timeline_markers.remove(m);

for curFrame in range(scene.frame_start, scene.frame_end+1):
	scene.timeline_markers.new("BHTS"+chr(65 + curFrame)+"0", frame=curFrame);

render_fetus2021.refresh_markers();
render_fetus2021.render_frames_by_markers("POSS", "finalrender");

scene.layers = [l in [1] for l in range(20)];

for m in scene.timeline_markers:
	scene.timeline_markers.remove(m);

for curFrame in range(scene.frame_start, scene.frame_end+1):
	scene.timeline_markers.new("BHTF"+chr(65 + curFrame)+"0", frame=curFrame);

render_fetus2021.set_offsets((32, 32));
render_fetus2021.refresh_markers();
render_fetus2021.render_frames_by_markers("POSS", "finalrender");
