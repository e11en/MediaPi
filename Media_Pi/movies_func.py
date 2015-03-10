__author__ = 'Ellen Langelaar'

import json

import requests
import tmdbsimple as tmdb

from models import Movie


tmdb.API_KEY = '9a5d3d7ffc482b8739b64c021725f6b8'
base_url_yify = 'https://yts.re/api/'
base_url_tmdb_img = 'http://image.tmdb.org/t/p/w154'
base_url_tmdb_img_large = 'http://image.tmdb.org/t/p/w342'


def get_movies(imdb_id=None, keywords=None, page=1):
    if imdb_id is not None:
        return get_movie(imdb_id)
    elif keywords is not None:
        try:
            m = json.loads(get_movie_by_keyword(keywords=keywords, page=page))['MovieList']
        except KeyError:
            return []
    else:
        return None

    return get_arr_movie(m)


def get_movie(imdb_id=None):
    if imdb_id is not None:
        try:
            m = json.loads(get_movie_by_imdb(imdb_id))['MovieList']
        except KeyError:
            return []
    else:
        return None

    return get_one_movie(m)


def get_popular_movies(limit=10, page=1):
    try:
        m = json.loads(get_movie_by_all(limit, page))['MovieList']
    except KeyError:
        return []

    return get_arr_movie(m)


def get_arr_movie(yify_json):
    movie_arr = []
    imdb_arr = []
    for item in yify_json:
        imdb = item['ImdbCode']

        if imdb not in imdb_arr:
            imdb_arr.append(imdb)
        else:
            continue

        try:
            title = item['MovieTitleClean']
        except KeyError:
            title = item['MovieTitle']

        tmdb_id = item['MovieID']
        year = item['MovieYear']
        poster = get_poster(imdb)
        movie_arr.append(Movie(title=title, year=year, poster=poster, imdb=imdb, tmdb_id=tmdb_id))

    return movie_arr


def get_one_movie(yify_json):
    quality_arr = []
    imdb = yify_json[0]['ImdbCode']
    tmdb_id = yify_json[0]['MovieID']
    m2 = get_movie_info(imdb)
    title = yify_json[0]['MovieTitleClean']
    year = yify_json[0]['MovieYear']
    poster = get_poster(imdb, True)
    overview = m2['overview']
    genre = yify_json[0]['Genre']
    torrent = yify_json[0]['TorrentMagnetUrl']
    runtime = m2['runtime']

    for item in yify_json:
        quality_arr.append(item['Quality'])

    return Movie(title=title, year=year, poster=poster, imdb=imdb, tmdb_id=tmdb_id,
                 genre=genre, quality=quality_arr, overview=overview, torrent=torrent, runtime=runtime)


def get_movie_by_keyword(keywords, limit=10, page=1):
    uri = base_url_yify + 'list.json?keywords=' + keywords + '&limit=' + str(limit) + '&set=' + str(page)
    return get_json(url=uri)


def get_movie_by_imdb(id, limit=10, page=1):
    uri = base_url_yify + 'listimdb.json?imdb_id=' + id + '&limit=' + str(limit) + '&set=' + str(page)
    return get_json(url=uri)


def get_movie_by_all(limit=10, page=1):
    uri = base_url_yify + 'list.json?limit=' + str(limit) + '&set=' + str(page)
    return get_json(url=uri)


def get_json(url):
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        else:
            return None


def get_poster(imdb, large=False):
    base_url = 'http://api.themoviedb.org/3/find/'
    ext_url = '?api_key=9a5d3d7ffc482b8739b64c021725f6b8&external_source=imdb_id'
    r_json = get_json(url=base_url + imdb + ext_url)
    response = json.loads(r_json)['movie_results'][0]['poster_path']
    if large:
        return base_url_tmdb_img_large + response
    else:
        return base_url_tmdb_img + response


def get_movie_info(imdb_id):
    find = tmdb.Find(imdb_id)
    m_id = find.info(external_source='imdb_id')['movie_results'][0]['id']
    movie = tmdb.Movies(m_id)
    return movie.info()