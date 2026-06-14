magick -size 64x64 xc:white -fx ((i+j-64)/64) -alpha off ^
	( +clone -flip ) -append ( +clone -flop ) +append diamond.png

timeout 5