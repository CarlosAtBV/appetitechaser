FOR /R %%A IN (render_spit/*.png) DO (
	echo comp/%%~nA
	echo comp/%%~nA
	magick render_spit/%%~nA.png ^
		-write MPR:orig -alpha off +dither -remap pal.png ^
		MPR:orig -compose CopyOpacity -composite ^
		-channel A -threshold 50%% +channel ^
		comp/%%~nA.png
)


	
timeout 5