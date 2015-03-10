__author__ = 'Ellen Langelaar'

from flask import render_template, request, url_for
import json
import functions as func
from Media_Pi import app
import movies_func
import tv_series_func
import omxplayer
import subtitles


# HOME ######################################################
@app.route('/')
def index():
    return render_template('index.html')
# END #######################################################


# GRID ######################################################
@app.route('/more_items', methods=['POST'])
def more_items():
    if request.form['type'] == 'movie':
        temp = movies_func.get_popular_movies(page=int(request.form['page']))
    else:
        temp = tv_series_func.get_tvshow_all(page=int(request.form['page']))
    return json.dumps([e.serialize() for e in temp])
# END #######################################################


# SEARCH ####################################################
@app.route('/search')
def search():
    return render_template('settings.html', title='Settings')
# END #######################################################


# MOVIES ####################################################
@app.route('/movies')
def movies():
    return render_template('grid.html', title='Movies', page='movie', search=True)


@app.route('/movie/<imdb>')
def movie(imdb):
    data = movies_func.get_movie(imdb_id=imdb)
    return render_template('movie.html', title=data.title, data=data, page='movie')
# END #######################################################


# TV SHOWS ##################################################
@app.route('/shows')
def shows():
    return render_template('grid.html', title='TV Series', page='show', search=True)


@app.route('/show/<imdb>')
def show(imdb):
    data = tv_series_func.get_tvshow_one(imdb)
    return render_template('show.html', title=data.title, data=data)
# END #######################################################


# PLAY ######################################################
@app.route('/play', methods=['POST'])
def play():
    # subtitles.getSubtitle('G:\Horrible.Bosses.2.2014.720p.BluRay.x264.YIFY.mp4')
    func.start_stream('"%s"' % request.form['torrent'])
    return url_for('remote')
# END #######################################################


# REMOTE ####################################################
@app.route('/remote')
def remote():
    return render_template('remote.html', title='remote')


@app.route('/remote_key', methods=['POST'])
def remote_key():
    key = request.form['key']
    if key == 'stop':
        func.stop_stream()
    else:
        omxplayer.send_key(key)
    return key
# END #######################################################


# YouTube ###################################################
@app.route('/youtube')
def youtube():
    return render_template('youtube.html', title='YouTube')
# END #######################################################


# SETTINGS ##################################################
@app.route('/settings')
def settings():
    return render_template('settings.html', title='Settings')
# END #######################################################


