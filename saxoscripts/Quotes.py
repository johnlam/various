import requests
from BeautifulSoup import BeautifulSoup
from random import choice
import saxo

class Quotes(object):
    RANDOM_SUBJECTS=['programming','computers','developer']
    
    def __init__(self,subject):
        if subject:
            self.getquote(subject)
        else:
            self.getquote(choice(RANDOM_SUBJECTS))

    def __str__(self):
        return self.quote
        
    def getquote(self,subject):
        req = requests.get('http://www.goodreads.com/quotes/tag/' + subject)
        soup = BeautifulSoup(req.text)
        quotes = soup.findAll('div',attrs={'class':'quoteText'})
        if len(quotes) == 0:
            self.quote = 'No quotes' 
        else:
            self.quote = choice(quotes).text[:250]

@saxo.pipe
def quotes(arg):
    return str(Quotes(arg))
