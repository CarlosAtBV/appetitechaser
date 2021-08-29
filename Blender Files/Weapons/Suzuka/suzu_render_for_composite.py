import bpy, sys
sys.path.append('../../RenderPipeline/');
import render_fetus2021

scene = bpy.context.scene;

skipframes = [12, 19];

layers = [
    {
        "layers":[2],
        "name":"render_default"
    },
    {
        "layers":[0],
        "name":"render_shotgun"
    },
    {
        "layers":[1],
        "name":"render_nails"
    },
    {
        "layers":[3],
        "name":"render_shotgun_bm"
    },
    {
        "layers":[4],
        "name":"render_default_bm"
    },
];

for layer in layers:
	for m in scene.timeline_markers:
		scene.timeline_markers.remove(m);
	
	for i in range(scene.frame_start, scene.frame_end+1):
		if skipframes.count(i):
			scene.timeline_markers.new("ignore", frame=i);
		else:
			filename = "{:0>4d}".format(i);
			scene.timeline_markers.new(filename, frame=i);

	render_fetus2021.refresh_markers();

	scene.layers = [l in layer["layers"] for l in range(20)];
	render_fetus2021.set_crop(False);
	render_fetus2021.set_path("//"+layer["name"]+"/");
	render_fetus2021.render_frames_by_markers("POSS", "finalrender");