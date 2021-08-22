import sys, bpy
sys.path.append('../../RenderPipeline/');
import render_fetus2021

scene = bpy.context.scene

mods = [
	{
		"number":"1",
		"path":"//../../../TSP PK3/sprites/weapons/mel/Darling Nikki/",
		"visual":"GunStrip_Normal"
	},
	{
		"number":"2",
		"path":"//../../../TSP PK3/sprites/weapons/mel/Darling Nikki/Spitfire/",
		"visual":"GunStrip_Spitfire"
	}
]

frame_names = [
	["12{mod}GA0"] * 2,
	["12{mod}GB0"] * 2,
	["12{mod}GC0"] * 2,
	["12{mod}GD0"] * 2,
	["12{mod}GE0"] * 2,
	
	["12{mod}RA0"] * 2,
	["12{mod}RB0"] * 2,
	["12{mod}RC0"] * 2,
	["12{mod}RD0"] * 2,
	
	["12{mod}SA0"] * 2,
	["12{mod}SB0"]  * 2,
	["12{mod}SC0"]  * 2,
	
	["120HA0", "ignore"],
	["120HB0", "ignore"],
	["120HC0", "ignore"],
	
	["ignore", "12{mod}AA0"],
	["ignore", "12{mod}AB0"],
	
	["120HD0", "ignore"],
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
