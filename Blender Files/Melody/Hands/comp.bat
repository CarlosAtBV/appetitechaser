::magick preview.png preview2.png -trim -append ^
::	-write MPR:orig -alpha off +dither -remap pal.png ^
::	( MPR:orig -alpha extract -fx round(u) ) ^
::	-compose CopyOpacity -composite ^
::	preview3.png
	
magick -background none ^
	( -gravity West render/melee_idle-1.png -extent 416x400 -extent 800x400 ) ^
	( -gravity East render/melee_idle-1.png -extent 396x400 -extent 800x400 ) ^
	comp/melee_idle-1.png
	
magick -background none ^
	( -gravity West render/melee_idle-2.png -extent 416x400 -extent 800x400 ) ^
	( -gravity East render/melee_idle-2.png -extent 396x400 -extent 800x400 ) ^
	comp/melee_idle-2.png
	
magick -background none ^
	( -gravity West render/melee_idle-3.png -extent 416x400 -extent 800x400 ) ^
	( -gravity East render/melee_idle-3.png -extent 396x400 -extent 800x400 ) ^
	comp/melee_idle-3.png
	
timeout 5