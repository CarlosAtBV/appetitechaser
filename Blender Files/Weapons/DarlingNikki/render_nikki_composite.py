import sys, bpy
sys.path.append('../../RenderPipeline/');
import render_fetus2021

scene = bpy.context.scene

frame_names = [
	"121GA0",
	"121GB0",
	"121GC0",
	"121GD0",
	"121GE0",
	
	"121RA0",
	"121RB0",
	"121RC0",
	
	"120HA0",
	"120HB0",
	"120HC0",
];

render_fetus2021.set_offsets((159, 50+32));
render_fetus2021.set_path("//../../../TSP PK3/sprites/weapons/mel/Darling Nikki/");

for cnt, frame in enumerate(frame_names):
	scene.timeline_markers.new(frame, frame=cnt);

render_fetus2021.refresh_markers();
render_fetus2021.render_frames_by_markers("POSS", "finalrender");
