__author__ = 'Ellen Langelaar'

import json

import requests

from models import Tv_show, Episode


base_eztv_url = 'http://eztvapi.re/shows/'
base_eztv_season_url = 'http://eztvapi.re/show/'


def get_tvshow_all(page=1):
    m = json.loads(get_tvshow_by_all(page))
    return get_arr_tv(m)


def get_tvshow_one(imdb):
    m = json.loads(get_tvshow_by_one(imdb))
    return get_one_tv(m)


def get_arr_tv(eztv_json):
    tv_arr = []
    for item in eztv_json:
        imdb = item['imdb_id']
        poster = item['images']['poster']
        poster = poster.replace('original', 'thumb')
        title = item['title']
        num_seasons = item['num_seasons']
        year = item['year']
        tv_arr.append(Tv_show(title, poster, imdb, num_seasons, year))
    return tv_arr


def get_one_tv(eztv_json):
    tv_arr = []
    imdb = eztv_json['imdb_id']
    poster = eztv_json['images']['poster']
    poster = poster.replace('original', 'thumb')
    title = eztv_json['title']
    num_seasons = int(eztv_json['num_seasons'])
    year = eztv_json['year']
    show = Tv_show(title, poster, imdb, num_seasons, year)
    show.banner = eztv_json['images']['banner']

    for item in eztv_json['episodes']:
        season = item['season']
        episode = item['episode']
        title_e = item['title']
        overview = item['overview']
        torrent = item['torrents']['0']['url']

        tv_arr.append(Episode(season, episode, title_e, overview, torrent))
    show.set_episodes(sorted(tv_arr, key=lambda epi: epi.season))
    return show


def get_tvshow_by_all(page=1):
    uri = base_eztv_url + str(page)
    return get_json(url=uri)


def get_tvshow_by_one(imdb):
    uri = base_eztv_season_url + imdb
    return get_json(url=uri)


def get_json(url):
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        else:
            return None


