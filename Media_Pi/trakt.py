__author__ = 'Ellen Langelaar'

_base_url = 'https://api.trakt.tv/'
_api_key = 'd4161a7a106424551add171e5470112e4afdaf2438e6ef2fe0548edc75924868'

# TODO: implement trakt
# @app.route('/trakt')
# def trakt():
#    if func.chk_storage_item('trakt-username'):
#        return render_template('trakt.html', title='Trakt', username=func.get_storage_item('trakt-username'))
#    else:
#        return render_template('trakt.html', title='Trakt')


# @app.route('/trakt', methods=['POST'])
# def trakt_login():
#    username = request.form['username']
#    password = request.form['password']
#    if account.test(username, password):
#       func.set_storage_item('trakt-username', username)
#       func.set_storage_item('trakt-password', password)
#       return render_template('trakt.html', username=request.form['username'])
#    else:
#       return render_template('trakt.html', error=username)
# END #######################################################