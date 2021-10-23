magick convert -background none ^
	( %1 ) ^
	-write MPR:orig ^
	( MPR:orig -channel a %2 -compose multiply -composite ) ^
	-compose copyalpha -composite ^
	%3.png