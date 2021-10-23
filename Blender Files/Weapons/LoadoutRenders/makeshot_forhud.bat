if not exist %2 mkdir %2

magick convert -background none ^
	( %1 -filter box -resize 100%%x120%% -gravity center -trim -resize x72 ) ^
	-gravity northwest -gravity center -rotate 45 ^
	-gravity northwest -extent 128x128 ^
	%2%3.png