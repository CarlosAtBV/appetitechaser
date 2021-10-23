set NAME=bv-tsp-dev

tools\7za a -tzip %NAME%.pk3 ".\TSP PK3\*" -xr@pack_exclude.txt

timeout 5
