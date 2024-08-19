::magick preview.png preview2.png -trim -append ^
::	-write MPR:orig -alpha off +dither -remap pal.png ^
::	( MPR:orig -alpha extract -fx round(u) ) ^
::	-compose CopyOpacity -composite ^
::	preview3.png

magick pal_base.png ^
	( -size 1x1 xc:#493437 xc:#854F3C xc:#FEE5C3 xc:#FFEEDA +append -resize 64x1^! ) ^
	( -size 1x1 xc:#0A010A xc:#13050B xc:#353030 xc:#4E413F xc:#705445 +append -resize 24x1^! ) ^
	+append ^
	pal3.png
	
magick -background none -gravity center ^
	( rendertest/0001.png rendertest/0002.png rendertest/0003.png rendertest/0004.png -gravity center -extent 320x240 -trim -extent 120%% -append ) ^
	-write MPR:orig -alpha off +dither -remap pal3.png ^
	( MPR:orig -alpha extract -fx round(u) ) ^
	-compose CopyOpacity -composite ^
	-filter point -resize 200%%x240%%^! ^
	preview/paltester.png
	
timeout 10
exit /B 0

magick -background none -gravity center ^
	( rendertest/*.png -trim -append ) ^
	-write MPR:orig -alpha off +dither -remap pal3.png ^
	( MPR:orig -alpha extract -fx round(u) ) ^
	-compose CopyOpacity -composite ^
	-filter point -resize 200%% ^
	preview/preview.png
	
exit /B 0

magick -background none -dispose background ^
	rendertest/*.png -reverse rendertest/*.png ^
	-filter point -resize 200%%x240%% ^
	test.gif

timeout 5