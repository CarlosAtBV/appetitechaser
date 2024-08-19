magick -background "none" -delay %%[fx:100*(1/35)] -dispose background animtest/*.png ^
	-filter point -resize 200%%x240%% ^
	animtest.gif