#!/usr/bin/python

desc = \
"""
Tool for creating game-on-demand containers for extracted xbox 360 games.
"""

import argparse
import sys

# set up argument parser
parser = argparse.ArgumentParser(
    description=desc)

# parse arguments
parser.parse_args(sys.argv[1:])

