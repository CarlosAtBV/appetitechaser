import sys, bpy
sys.path.append('../../RenderPipeline/');
import render_fetus2021

scene = bpy.context.scene

frame_names = [
	"121FA0",
	"121FB0",
	"121FC0",
	"121FD0",
	"122FA0",
	"122FB0",
	"122FC0",
	"122FD0",
	
	"122FE0",
	"122FF0",
	"122FG0",
	"122FH0",
	
	"121FE0",
	"121FF0",
	"121FG0",
	"121FH0",
];

render_fetus2021.set_offsets((159, 50+32));
render_fetus2021.set_path("//../../../TSP PK3/sprites/weapons/mel/Darling Nikki/");

for m in scene.timeline_markers:
	scene.timeline_markers.remove(m);

for cnt, frame in enumerate(frame_names):
	scene.timeline_markers.new(frame, frame=cnt+1);

render_fetus2021.refresh_markers();
render_fetus2021.render_frames_by_markers("POSS", "finalrender");
