import subprocess

import os
daPath = os.path.dirname(os.path.realpath(__file__));

dir_output = daPath+"/../../../TSP PK3/graphics/hud/weapons/";
dir_sources = daPath+"/sources/";
bat_makeshot = daPath+"/makeshot_forhud.bat";
print(bat_makeshot);

charDefs = [
	{
		"name": "nikki_unmodded",
		"pic": "nikki_unmodded",
	},
	{
		"name": "nikki_spitfire",
		"pic": "nikki_spitfire",
	},
	{
		"name": "suzu_scope",
		"pic": "suzu_scope",
	},
	{
		"name": "suzu_shotgun",
		"pic": "suzu_shotgun",
	},
	{
		"name": "mel_pawnch",
		"pic": "mel_fisting",
	},
];

for doWeapon in charDefs:
	process = subprocess.call([bat_makeshot, str(dir_sources+doWeapon["pic"]+".png"), dir_output, doWeapon["name"]]);