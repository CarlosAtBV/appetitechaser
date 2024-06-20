::magick preview.png preview2.png -trim -append ^
::	-write MPR:orig -alpha off +dither -remap pal.png ^
::	( MPR:orig -alpha extract -fx round(u) ) ^
::	-compose CopyOpacity -composite ^
::	preview3.png

magick ^
	( preview/twohands.png preview/twohands2.png -trim -append ) ^
	-write MPR:orig -alpha off +dither -remap pal2.png ^
	( MPR:orig -alpha extract -fx round(u) ) ^
	-compose CopyOpacity -composite ^
	-filter point -resize 200%% ^
	preview/preview.png

timeout 5