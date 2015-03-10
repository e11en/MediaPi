__author__ = 'Ellen Langelaar'

from subfinder import subtitle
from subfinder import movie


def getSubtitle(fileName, lang = "eng"):
    #  TODO: CHECK SUB TAAL IN SETTINGS
    #  TODO: LANGUAGE SELECT
    try:
        s = subtitle.OSService()
        print "Getting subtitles:"
        m = movie.MovieFile(fileName)
        s.get(m, language=lang)
    except Exception, e:
        print "Error getting subtitles: %s" % e

