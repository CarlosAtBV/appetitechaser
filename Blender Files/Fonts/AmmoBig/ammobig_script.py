import subprocess, math, os

basePath = os.path.dirname(os.path.realpath(__file__))+"/";
restingPlace = basePath+"../../../TSP PK3/fonts/tsp_ammo_big/";
restingPlaceTwo = basePath+"../../../TSP PK3/fonts/tsp_ammo_small/";

cmd_drawText = '-font "'+basePath+'sfquartzite.ttf" -pointsize 18 label:0123456789 ^';
cmd_pointSize = str(18+10);
cmd_warpOffset = 10;
cmd_perspective = "-distort Perspective \"0,0 "+str(cmd_warpOffset)+",0  0,18 0,18  48,18 48,18  48,0 "+str(48+cmd_warpOffset)+",0\" -extent +1+0 -trim";

minRange = 48;
maxRange = 57;

for i in range(minRange, maxRange+1):
	getCode = format(i, 'x');
	frameName = format(getCode, "0>4");
	
	commandToDo = ('magick convert -background "#000000" -fill "#FFFFFF" ^'
		+'-font "'+basePath+'sfquartzite.ttf" -pointsize '+cmd_pointSize+' label:'+str(chr(i))+' ^'
		+'-trim -extent 48x18-1-0 '+cmd_perspective+' ^'
		+'"'+basePath+frameName+'.png"')
	subprocess.call(commandToDo, shell=True);
	
	commandToDo = ('magick convert "'+basePath+frameName+'.png" "'+basePath+frameName+'.png" ^'
		+'-alpha Off -compose CopyOpacity -composite ^'
		+'"'+restingPlace+frameName+'.png"')
	subprocess.call(commandToDo, shell=True);
	
	commandToDo = ('magick convert "'+restingPlace+frameName+'.png" -resize 50% ^'
		+'"'+restingPlaceTwo+frameName+'.png"')
	subprocess.call(commandToDo, shell=True);
	
	maxI = i - minRange;
	maxOffset = maxRange - minRange;
	print("..."+str(math.floor((maxI/maxOffset)*100))+"%");