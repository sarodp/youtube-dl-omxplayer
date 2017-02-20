# youtube-dl-omxplayer
download youtube and play with omxplayer

$ sudo apt-get update

$ sudo apt-get upgrade

$ sudo apt-get install youtube-dl

...

$ sudo apt-get install omxplayer

$ nano youtube.sh
 #!/bin/bash
 #youtube.sh
 echo "enter youtube clip url:"
 read url
 ymp4=$(youtube-dl -g $url)
 omxplayer -o local --win 0,50,800,500 $ymp4 

$ chmod +x youtube.sh

$ youtube.sh

enter youtube clip url: https://www.youtube.com/watch?v=3FygIKsnkCw&list=RD3FygIKsnkCw

...
