import sys, bpy
sys.path.append('../../RenderPipeline/');
import render_fetus2021

scene = bpy.context.scene

def srgb_to_linearrgb(c):
	if   c < 0: 	  return 0
	elif c < 0.04045: return c/12.92
	else:   		  return ((c+0.055)/1.055)**2.4

def hex_to_rgb(h,alpha=1):
	r = (h & 0xff0000) >> 16
	g = (h & 0x00ff00) >> 8
	b = (h & 0x0000ff)
	return tuple([srgb_to_linearrgb(c/0xff) for c in (r,g,b)] + [alpha])

daPickups = [
	{
		"image":"health.png",
		"color":hex_to_rgb(0x00C5FF),
	},
	{
		"image":"ammo.png",
		"color":hex_to_rgb(0xFF7C00),
	},
]

render_fetus2021.set_offsets((18/2, 18));
render_fetus2021.set_path("//../../../TSP PK3/sprites/bh/pickups/");

curFrame = 0;

for pickup in daPickups:
	scene.node_tree.nodes["Image.001"].image = bpy.data.images[pickup["image"]];
	scene.node_tree.nodes["RGB.001"].outputs[0].default_value = pickup["color"];

	for m in scene.timeline_markers:
		scene.timeline_markers.remove(m);

	scene.timeline_markers.new("BHPU"+chr(65 + curFrame)+"0", frame=1);
		
	render_fetus2021.refresh_markers();
	render_fetus2021.render_frames_by_markers("POSS", "finalrender");
	
	curFrame += 1;
