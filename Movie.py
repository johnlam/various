import json
import requests
from BeautifulSoup import BeautifulSoup
from urllib import urlencode
from datetime import datetime
from math import log10,modf
from dateutil import parser
from dateutil.relativedelta import relativedelta
from random import choice
import saxo

class Movie(object):

    def __init__(self,movie):
        
        self.rating = float(0)
        self.reldate = datetime.utcnow()
        self.quotes = []
        if movie.startswith('tt') and len(movie) == 9:
            self.movieid = movie
        else:
            self.title = movie
            self.movieid = self.getid()

        self.getinfo()

    def __str__(self):
        if self.quotes:
            return self.title + self.whentospoil() + choice(self.quotes)[:100]
        return self.title + self.whentospoil()

    def getinfo(self):
        req = requests.get('http://www.imdb.com/title/'+self.movieid + '/')
        soup = BeautifulSoup(req.text)
        ratetag = soup.find('div',attrs={"class":"ratingValue"})
        self.rating = float(ratetag.find('span',attrs={'itemprop':'ratingValue'}).text)
        self.reldate = parser.parse(soup.find('meta',attrs={'itemprop':'datePublished'})['content'])
        if not self.title:
            title = soup.find('h1',attrs={'itemprop':'name'})
            self.title = title.text.split('&')[0]

        
    def getid(self):
        moviequery = urlencode({"q":self.title})
        req = requests.get('http://www.imdb.com/xml/find?json=1&nr=1&tt=on&' + moviequery)
        imdbdata = json.loads(req.text)
        if 'title_popular' in imdbdata:
            movieid = imdbdata['title_popular'][0]['id']
        elif 'title_substring' in imdbdata:
            movieid = imdbdata['title_substring'][0]['id']
        return movieid

    def whentospoil(self):
        spoildate = self._calcspoiler()
        if spoildate > datetime.utcnow():
            return spoildate.strftime('. Can be spoilt from %d, %b %Y. ')
        else:
            self.getquotes()
            return spoildate.strftime('. Can be spoilt since %d, %b %Y. ') 

    def _calcspoiler(self):
        years = self._MUF()
        frac,whole = modf(years)
        return self.reldate + relativedelta(years=int(whole),months=int((frac/100) * 12))
    
    def _MUF(self):
        """ Calculate years relative to rating.
        Assume that a movie with a rating of 10/10 should be spoiled
        10 years after its release.
        """
        return log10(self.rating**self.rating)


    def getquotes(self):
        req = requests.get('http://www.imdb.com/title/'+self.movieid + '/quotes')
        soup = BeautifulSoup(req.text)
        quotes = soup.findAll("div",attrs={"class":"sodatext"})
        for quote in quotes:
            self.quotes.append(quote.text.replace('\n',''))

@saxo.pipe
def spoil(arg):
    if not arg:
        return "Example: .spoil The Matrix or .spoil tt0133093 "
    return str(Movie(arg))
