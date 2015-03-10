__author__ = 'e11en'

import subprocess
import shlex
import time


def start(stream_url):
    time.sleep(10)
    cmd = 'omxplayer -o hdmi -r -b %s' % stream_url
    proc = subprocess.Popen(shlex.split(cmd), shell=False)
    # Wait until it's running
    while proc.poll() != None:
        time.sleep(0.1)
    print 'omxplayer started'

def send_cmd(key):
    cmd = '/usr/local/bin/dbuscontrol.sh %s' % key
    subprocess.call(shlex.split(cmd))
    print 'omxplayer key: %s' % key


def stop():
    send_cmd('stop')


def seek(position):
    # POSITION IN MICORSECONDS
    send_cmd('setposition %s' % position)


def send_key(key):
    if key == 'play-pause':
        send_cmd('pause')
