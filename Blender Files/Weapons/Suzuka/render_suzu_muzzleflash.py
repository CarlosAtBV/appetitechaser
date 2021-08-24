import sys, bpy
sys.path.append('../../RenderPipeline/');
import render_fetus2021

scene = bpy.context.scene

frame_names = [
	"131FA0",
	"131FB0",
	"131FC0",
	"131FD0",
];

render_fetus2021.set_offsets((159, 50+32));
render_fetus2021.set_path("//../../../TSP PK3/sprites/weapons/mel/Suzuka/");

for m in scene.timeline_markers:
	scene.timeline_markers.remove(m);

for cnt, frame in enumerate(frame_names):
	scene.timeline_markers.new(frame, frame=cnt+1);

render_fetus2021.refresh_markers();
render_fetus2021.render_frames_by_markers("POSS", "finalrender");
