import sys, bpy, subprocess
sys.path.append('../../RenderPipeline/');
import render_base

scene = bpy.context.scene

mods = [
	{
		"number":"1",
		"path":"//../../../TSP PK3/sprites/weapons/mel/Suzuka/",
		"visual":"GunStrip_Normal"
	},
	{
		"number":"2",
		"path":"//../../../TSP PK3/sprites/weapons/mel/Suzuka/Shotgun/",
		"visual":"GunStrip_Shotgun"
	},
	{
		"number":"3",
		"path":"//../../../TSP PK3/sprites/weapons/mel/Suzuka/Nails/",
		"visual":"GunStrip_Nails"
	},
	
	{
		"number":"2",
		"path":"//../../../TSP PK3/brightmaps/weapons/",
		"visual":"GunStrip_Shotgun_BM"
	},
	
	{
		"number":"1",
		"path":"//../../../TSP PK3/brightmaps/weapons/",
		"visual":"GunStrip_Normal_BM"
	},
]

frame_names = [
	["13{mod}GA0"] * 3,
	["13{mod}GB0"] * 3,
	
	["13{mod}AA0", "13{mod}AA0",  "ignore"],
	["13{mod}AB0", "13{mod}AB0",  "ignore"],
	["13{mod}AC0", "13{mod}AC0",  "ignore"],
	["ignore", "13{mod}AD0",  "ignore"],
	["ignore", "13{mod}AE0",  "ignore"],
	["ignore", "13{mod}AF0",  "ignore"],
	
	["13{mod}RA0"] * 3,
	["13{mod}RB0"] * 3,
	["13{mod}RC0"] * 3,
	["13{mod}RD0"] * 3,
	
	["130HA0", "ignore",  "ignore"],
	["130HB0", "ignore",  "ignore"],
	["130HC0", "ignore",  "ignore"],
	
	["13{mod}RE0"] * 3,
	["13{mod}RF0"] * 3,
];

for cntmod, mod in enumerate(mods):
	offsets = (159, 50+32);
	path = mod["path"];
	modnum = int(mod["number"])-1;
	
	for i in mods:
		scene.sequence_editor.sequences_all[i["visual"]].mute = not (i == mod);

	for m in scene.timeline_markers:
		scene.timeline_markers.remove(m);
	
	for cnt, frame in enumerate(frame_names):
		if ( frame[modnum] == "ignore" ):
			continue;
		scene.frame_set(cnt);
		#framename = frame[int(mod["number"])-1].replace("{mod}",mod["number"]);
		framename = frame[modnum].format(mod = mod["number"]);
		scene.render.filepath = path+framename;#+chr(65+cnt-1)+'0';
		bpy.ops.render.render(write_still = True);
		origImg = bpy.data.images.load(bpy.context.scene.render.filepath+str('.png'))
		cropImg, pX, pY = render_base.crop_image(origImg, offsets[0], offsets[1]);

		cropImg.file_format = 'PNG';
		cropImg.filepath_raw = scene.render.filepath+str('.png');
		cropImg.save();

		process = subprocess.Popen(['D:\Projects\RenderPipeline\compresssprite_256colors.bat', str(pX), str(pY), bpy.path.abspath(cropImg.filepath_raw)])