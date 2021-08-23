import sys, bpy
sys.path.append('../../RenderPipeline/');
import render_fetus2021

scene = bpy.context.scene

mods = [
	{
		"number":"1",
		"path":"//../../../TSP PK3/sprites/weapons/mel/Suzuka/",
		"visual":"GunStrip_Normal"
	}
]

frame_names = [
	["13{mod}GA0"] * 2,
	["13{mod}GB0"] * 2,
];

for cntmod, mod in enumerate(mods):
	render_fetus2021.set_offsets((159, 50+32));
	render_fetus2021.set_path(mod["path"]);
	
	for i in mods:
		scene.sequence_editor.sequences_all[i["visual"]].mute = not (i == mod);

	for m in scene.timeline_markers:
		scene.timeline_markers.remove(m);
	
	for cnt, frame in enumerate(frame_names):
		scene.timeline_markers.new(frame[cntmod].format(mod = mod["number"]), frame=cnt);

	render_fetus2021.refresh_markers();
	render_fetus2021.render_frames_by_markers("POSS", "finalrender");
