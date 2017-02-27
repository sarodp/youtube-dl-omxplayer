#!/usr/bin/python2
# file: testomxwrap.py

from omxplayer import OMXPlayer
from time import sleep

file_path_or_url = raw_input('file or url: ')

# This will start an `omxplayer` process, this might
# fail the first time you run it, currently in the
# process of fixing this though.
player = OMXPlayer(file_path_or_url)

# The player will initially be paused

player.play()
sleep(5)
player.pause()

# Kill the `omxplayer` process gracefully.
player.quit()
