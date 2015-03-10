__author__ = 'e11en'

import subprocess
import shlex
import time


def start(torrent_url):
    cmd = 'peerflix "%s" -q -p 8888 -r' % torrent_url
    proc = subprocess.Popen(shlex.split(cmd), stdin=subprocess.PIPE,
                                              stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE,
                                              shell=False)
    # Wait until it's running
    while proc.poll() != None:
        time.sleep(0.1)

    print 'peerflix started'
    return proc


# CLEAN UP PEERFLIX TMP FILES
def cleanup():
    cmd = 'rm -r /tmp/torrent-stream/*'
    subprocess.call(shlex.split(cmd))