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

# constants
data_dir_name = os.path.join("data", "quickboot")

# set up argument parser
parser = argparse.ArgumentParser(description=desc)

# parse arguments
parser.parse_args(sys.argv[1:])

game_name = raw_input("Name of game: ")
game_loc = raw_input("Location of game: ")

dir_name = game_name
print game_name + " " + game_loc

# create directory structure
print "Creating files...",
os.mkdir(dir_name)

# copy in default.xex
xex_name = os.path.join(dir_name, "default.xex")
to_be_copied = os.path.join(data_dir_name, "default.xex")
shutil.copy(to_be_copied, xex_name)

# create config file
config_name = os.path.join(dir_name, "config.ini")
config_file = open(config_name, "w")
config_file.write(game_loc+"\n")
config_file.close()

print "Done"

# create LIVE container for directory structure
print "Creating container...",
container = containers.LiveContainer()

print "Done"

# clean up
print "Cleaning up...",
os.remove(config_name)
os.remove(xex_name)
os.rmdir(dir_name)
print "Done"
