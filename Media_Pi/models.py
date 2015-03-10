__author__ = 'e11en'
import threading
import subprocess


# MOVIES ###
class Movie:
    def __init__(self, title, year, poster, imdb, tmdb_id, genre=None, quality=None, overview='', torrent='', runtime=''):
        self.title = title
        self.year = year
        self.poster = poster
        self.imdb = imdb
        self.tmdb_id = tmdb_id
        self.genre = genre
        self.quality = quality
        self.overview = overview
        self.torrent = torrent
        self.runtime = runtime

    def serialize(self):
        return {
            'title': self.title,
            'year': self.year,
            'poster': self.poster,
            'imdb': self.imdb,
            'tmdb_id': self.tmdb_id
        }
# MOVIES END ###


# TV SHOWS ###
class Tv_show:
    def __init__(self, title, poster, imdb, num_seasons, year):
        self.title = title
        self.poster = poster
        self.imdb = imdb
        self.num_seasons = num_seasons
        self.year = year
        self.episodes = []
        self.banner = ''

    def serialize(self):
        return {
            'title': self.title,
            'poster': self.poster,
            'imdb': self.imdb,
            'num_seasons': self.num_seasons,
            'year': self.year
        }

    def set_episodes(self, epi_arr):
        self.episodes = epi_arr


class Episode:
    def __init__(self, season, episode, title, overview, torrent):
        self.season = season
        self.episode = episode
        self.title = title
        self.overview = overview
        self.torrent = torrent

    def serialize(self):
        return {
            'season': self.season,
            'episode': self.episode,
            'title': self.title,
            'overview': self.overview,
            'torrent': self.torrent
        }
# TV SHOWS END ###


# PROCESSES ###
class Peerflix(threading.Thread):
    def __init__(self, torrent_url):
        self.stdout = None
        self.stderr = None
        self.torrent_url = torrent_url
        self.stream_url = ''
        threading.Thread.__init__(self)

    def run(self):
        cmd = 'peerflix %s --quiet' % self.torrent_url
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     shell=False)
        self.stdout, self.stderr = proc.communicate()
        # self.stream_url = proc.stdout.readline().split(' ')[4]


class Vlc(threading.Thread):
    def __init__(self, stream_url):
        self.stdout = None
        self.stderr = None
        self.stream_url = stream_url
        threading.Thread.__init__(self)

    def run(self):
        cmd = 'cvlc %s -I rc' % self.stream_url
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     shell=False)
        self.stdout, self.stderr = proc.communicate()
# PROCESSES END ###