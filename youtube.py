#!/usr/bin/python2
# file: youtube.py
#
#--play youtube with omxplayer from myplaylist.url
#=============================================================
import os
import subprocess

def run_command(command):
    # run command (can be an array (for parameters))
    p = subprocess.Popen \
        (command, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    # capture output and error
    (output, err) = p.communicate()
    # wait for command to end
    # TODO: really long running?
    status = p.wait()

    # decode output from byte string
    if output is not None:
        output = output.decode('utf-8')
    if err is not None:
        err = err.decode('utf-8')
    # return stdout, stderr, status code
    return (output, err, status)

#0--init xfilename
xfilename = "myplaylist.url"

print '\n>> Play youtube with omxplayer' 
print '>> -----------------------------------------------------'
print '\n>> file: %s' % xfilename

#1a--xfilename --> xlist
xfile = open(xfilename, "r+")
xlist = xfile.readline().splitlines()
xfile.close()

#1b--xlist --> xhttp
xhttp = []
for xl in xlist:
	if (xl[0] <>'#') and (xl[0]<>'\n'):
		xhttp = xhttp + [xl]

#1c--show xhttp
xi=1
for xurl in xhttp:
	print '     %i) %s' % (xi,xurl),
	xi+=1 

#2--get xsel
xin = input('\n>> select url [1-%i]: ' % (xi-1))
xsel = xin-1
print '>> playing %i) %s   ...'% (xsel+1, xhttp[xsel])

#4--omxplayer
'''
#================================================
#!/bin/bash
#youtube.sh
echo "enter youtube clip url:"
read url
ymp4=$(youtube-dl -g $url)
#wget $ymp4
omxplayer -o local --win 0,50,800,500 $ymp4 
#================================================
'''
xcmd = 'youtube-dl -g %s' % xhttp[xsel]
print '\n>>xcmd= %s' % xcmd



#----------
xrtn = run_command(xcmd)
xh = ['output:','error:','status:']
i=0
for xr in xrtn:
	print '>>%s %s' % (xh[i],xr)
	i+=1
	

#xcmd = 'omxplayer -o local --win 0,50,800,500 %s' % xrtn[0]
xcmd = 'wget %s' % xrtn[0]
print '\n>>xcmd= %s' % xcmd
print "...."
os.system(xcmd)
#xrtn2 = run_command(xcmd)
