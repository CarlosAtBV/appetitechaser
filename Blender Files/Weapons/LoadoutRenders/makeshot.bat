if not exist %3 mkdir %3

magick convert -background none ^
	( %1 -filter box -resize 100%%x120%% -gravity center -resize x%2 -trim ) ^
	%3/%4.png