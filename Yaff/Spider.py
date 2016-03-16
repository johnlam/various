import requests
from URLHandling import URLHandler


class Spider(object):
    def __init__(self, url, **reqargs):
        self.is_valid = URLHandler.is_valid(url)
        self.reqargs = reqargs
        if self.is_valid:
            self.request = requests.get(url, **self.reqargs)
            self.contenttype = self.request.headers['content-type']
        else:
            raise ValueError(url + ' is not valid. Check for missing scheme (i.e. http(s))')

    def make_request(self, url):
        self.is_valid = URLHandler.is_valid(url)
        if self.is_valid:
            self.request = requests.get(url, **self.reqargs)
            self.contenttype = self.request.headers['content-type']
        else:
            raise ValueError(url + ' is not valid. Check for missing scheme (i.e. http(s))')
