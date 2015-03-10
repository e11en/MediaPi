__author__ = 'Ellen Langelaar'

import shelve
import omxplayer, peerflix

proc_peerflix = None

# GET AN ITEM IN STORAGE #
def get_storage_item(key):
    storage = shelve.open('storage.dat')
    temp = storage[key]
    storage.close()
    return temp


# SET AN ITEM IN STORAGE
def set_storage_item(key, value):
    storage = shelve.open('storage.dat')
    storage[key] = value
    storage.close()


# CHECK IF A KEY IS IN STORAGE
def chk_storage_item(key):
    storage = shelve.open('storage.dat')
    temp = key in storage
    storage.close()
    return temp


# START VIDEO STREAM
def start_stream(torrent_url):
    global proc_peerflix
    proc_peerflix = peerflix.start(torrent_url)
    stream_url = proc_peerflix.stdout.readline().split(' ')[4]
    omxplayer.start(stream_url)


def stop_stream():
    global proc_peerflix
    proc_peerflix.kill()
    omxplayer.stop()
    peerflix.cleanup()