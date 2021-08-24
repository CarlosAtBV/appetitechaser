import sys, bpy
sys.path.append('../../RenderPipeline/');
import render_fetus2021

scene = bpy.context.scene

render_fetus2021.set_offsets((100, 32));
render_fetus2021.set_path("//../../../TSP PK3/sprites/weapons/mel/Suzuka/");

for m in scene.timeline_markers:
	scene.timeline_markers.remove(m);

scene.timeline_markers.new("131XA0", frame=1);

render_fetus2021.refresh_markers();
render_fetus2021.render_frames_by_markers("POSS", "finalrender");
