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
	
::cd comp

FOR /R %%A IN (comp/*.png) DO (
	echo comp/%%~nA
	echo comp/%%~nA
	magick comp/%%~nA.png ^
		-write MPR:orig -alpha off +dither -remap pal3.png ^
		MPR:orig -compose CopyOpacity -composite ^
		-channel A -threshold 50%% +channel ^
		comp/%%~nA.png
)


	
timeout 5