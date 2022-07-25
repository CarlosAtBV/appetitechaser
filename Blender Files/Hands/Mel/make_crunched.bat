cd render_melhands

magick mogrify -channel A -fx round(u) -path ../render_melcrunch *.png

timeout 35