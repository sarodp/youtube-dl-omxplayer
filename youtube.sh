#!/bin/bash
#youtube.sh
echo "enter youtube clip url:"
read url
ymp4=$(youtube-dl -g $url)
#wget $ymp4
omxplayer -o local --win 0,50,800,500 $ymp4 
