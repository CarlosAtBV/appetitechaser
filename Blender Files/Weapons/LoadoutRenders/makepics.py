import subprocess

import os
daPath = os.path.dirname(os.path.realpath(__file__));

dir_output = daPath+"/../../../TSP PK3/graphics/loadout/";
dir_sources = daPath+"/sources/";
bat_makeshot = daPath+"/makeshot.bat";
print(bat_makeshot);

charDefs = [
	{
		"name": "nikki_unmodded",
		"pic": "nikki_unmodded",
		"height": 64,
	},
	{
		"name": "nikki_spitfire",
		"pic": "nikki_spitfire",
		"height": 64,
	},
	{
		"name": "suzu_shotgun",
		"pic": "suzu_shotgun",
		"height": 112,
	},
	{
		"name": "suzu_scope",
		"pic": "suzu_scope",
		"height": 112,
	},
];
	
for doWeapon in charDefs:
	process = subprocess.call([bat_makeshot, str(dir_sources+doWeapon["pic"]+".png"), str(doWeapon["height"]), str(dir_output), doWeapon["name"]]);