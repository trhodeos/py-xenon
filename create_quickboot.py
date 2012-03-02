#!/usr/bin/python

import argparse
import os
import shutil
import sys
from xenon import containers

desc = \
"""
Tool for creating game-on-demand containers for extracted xbox 360 games.
"""

# quickboot constants
data_dir_name = os.path.join("data", "quickboot")

# set up argument parser
parser = argparse.ArgumentParser(description=desc)

# parse arguments
parser.parse_args(sys.argv[1:])

# get game information
game_name = raw_input("Name of game (eg Skyrim): ")
game_loc = raw_input("Location of executable (eg \Game\Skyrim\default.xex): ")

# set up output info
dir_name = game_name
output_dir_name = os.path.join("Content", "0000000000000000", "DEADBEEF", "00007000")
output_name = os.path.join(output_dir_name, game_name)

# quickboot xex/config info
xex_name = os.path.join(dir_name, "default.xex")
to_be_copied = os.path.join(data_dir_name, "default.xex")

config_name = os.path.join(dir_name, "config.ini")

print "Creating files...",
# create directory structure
os.mkdir(dir_name)
os.makedirs(output_dir_name)

# copy in default.xex
shutil.copy(to_be_copied, xex_name)

# create config file
config_file = open(config_name, "w")
config_file.write(game_loc + "\n")
config_file.close()
print "Done"

# create LIVE container for directory structure
print "Creating container...",
container = containers.LiveContainer()
container.set_title(game_name)
container.write(output_name)
print "Done"

# clean up
print "Cleaning up...",
os.remove(config_name)
os.remove(xex_name)
os.rmdir(dir_name)
print "Done"
