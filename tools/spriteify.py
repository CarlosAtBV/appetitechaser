import sys, os, subprocess, shutil
import numpy as np
path_base = (os.path.dirname(os.path.realpath(__file__)))
path_file = (os.path.dirname(os.path.realpath(sys.argv[1])))
path_game = f"{path_base}/../TSP PK3"

from wand.image import Image
from wand.display import display
from wand.color import Color
from wand.drawing import Drawing
from wand.api import library

import json

commands = []

with open(sys.argv[1], "r") as file:
	commands = file.read().split("\n")
	
cur_image = None

for command in commands:
	command = command+" "
	command_words = []
	lastWord = ""
	while True:
		if len(command) == 0:
			break
			
		ltr = command[0]
		command = command[1:]
		
		if ltr == " ":
			if len(lastWord) > 0:
				command_words.append(lastWord)
				lastWord = ""
			continue
			
		lastWord = lastWord + ltr
		
	# now do
	
	print(command_words)
	
	if len(command_words) == 0:
		continue
	
	if command_words[0] == "load":
		cur_image = Image(filename=f"{path_file}/{command_words[1].replace('"', '')}")
	
	if command_words[0] == "save":
		path_out = f"{path_game}/{command_words[1].replace('"', '')}"
		# 20
		# 41
		x_off = (cur_image.width/2)-160
		y_off = ((cur_image.height/2)-120) + 61
		path_dest = (os.path.dirname(os.path.realpath(path_out)))
		os.makedirs(path_dest, exist_ok=True)
		cur_image.save(filename=path_out)
		#subprocess.Popen(['D:/Projects/RenderPipeline/grabpng.exe', '-grab', str(0), str(61), path_out])
		subprocess.Popen(['D:/Projects/RenderPipeline/grabpng.exe', '-grab', str(x_off), str(y_off), path_out])
	#print(command)