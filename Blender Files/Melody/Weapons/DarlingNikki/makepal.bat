::magick preview.png preview2.png -trim -append ^
::	-write MPR:orig -alpha off +dither -remap pal.png ^
::	( MPR:orig -alpha extract -fx round(u) ) ^
::	-compose CopyOpacity -composite ^
::	preview3.png

magick ( -size 1x1 xc:#130B17 xc:#21233E xc:#2A3457 xc:#7F9AB5 xc:#FFFFFF +append -resize 32x1^! ) ^
	( -size 1x1 xc:#141818 xc:#354041 xc:#727675 xc:#FFFFFF +append -resize 24x1^! ) ^
	( -size 1x1 xc:#180705 xc:#522B17 xc:#FFAA89 +append -resize 24x1^! ) ^
	( -size 1x1 xc:#06060E xc:#393945 xc:#CCCDCE +append -resize 24x1^! ) ^
	+append ^
	pal.png

magick -background none -gravity center ^
	render_spit/0001.png ^
	-write MPR:orig -alpha off +dither -remap pal.png ^
	( MPR:orig -alpha extract -fx round(u) ) ^
	-compose CopyOpacity -composite ^
	paltester.png
	
timeout 4