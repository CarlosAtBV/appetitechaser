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
	( rendertest/*.png -trim -append ) ^
	-write MPR:orig -alpha off +dither -remap pal3.png ^
	( MPR:orig -alpha extract -fx round(u) ) ^
	-compose CopyOpacity -composite ^
	-filter point -resize 200%% ^
	preview/preview.png

timeout 5