magick preview.png preview2.png -trim -append ^
	-write MPR:orig -alpha off +dither -remap pal.png ^
	( MPR:orig -alpha extract -fx round(u) ) ^
	-compose CopyOpacity -composite ^
	preview3.png

timeout 5