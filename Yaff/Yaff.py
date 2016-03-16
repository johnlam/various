from __future__ import print_function
from collections import namedtuple, defaultdict
from bs4 import BeautifulSoup
from Spider import Spider
from URLHandling import URLHandler

__version__ = "0.0.1"
Result = namedtuple('Result', 'title feedtype')


class Yaff(object):
    def __init__(self, url, **kwargs):
        self.results = defaultdict(list)
        self.maxdepth = 2
        self.URLHandler = URLHandler()
        self.candidates = set()
        self.url = url
        self.baseurl = self.URLHandler.get_provider(self.url)
        self.spider = Spider(self.url, **kwargs)
        self.mysoup = BeautifulSoup(self.spider.request.text)

    def getnormalfeeds(self):
        tags = self.mysoup.findAll(['link', 'a'],
                                   {"type": ['application/rss+xml', 'application/atom+xml',
                                             "application/x.atom+xml",
                                             "text/xml", "application/xhtml+xml"]})
        for tag in tags:
            url = URLHandler.get_full_urls(self.baseurl, tag['href'])
            self.results[url].append(Result(title=tag.get('title', ''),
                                            feedtype=tag.get('type', '')))
        return self

    def gethiddenfeeds(self):
        for i in range(self.maxdepth):
            self._getcandidatetags()
            for candidate in self.candidates:
                try:
                    self.spider.make_request(candidate)
                    self.mysoup = BeautifulSoup(self.spider.request.text)
                except ValueError as e:
                    print(e)
                    continue
                if self.isfeed():
                    self.results[self.spider.request.url].append(Result(
                        title=self.mysoup.find('title').text,
                        feedtype=self.spider.contenttype))

                self.getnormalfeeds()
        return self

    def getrootrss(self):
        self.spider.make_request(self.url + '/rss')
        if self.isfeed():
            self.mysoup = BeautifulSoup(self.spider.request.text)
            url = URLHandler.get_full_urls(self.baseurl, self.url + '/rss')
            self.results[url].append(Result(
                title=self.mysoup.find('title').text,
                feedtype=self.spider.contenttype))
        return self

    def _getcandidatetags(self):
        tags = self.mysoup.findAll('a')
        feedstrings = ['feed', 'rss', 'atom', 'xml']
        for tag in tags:
            try:
                if any(fstring in tag['href'] for fstring in feedstrings):
                    self.candidates.add(URLHandler.get_full_urls(self.baseurl, tag['href']))
            except:
                continue

    def isfeed(self):
        if 'xml' in self.spider.contenttype or 'atom' in self.spider.contenttype:
            return True
        return False


def get_feeds(url, **kwargs):
    mfeeds = Yaff(url, **kwargs)
    mfeeds.getnormalfeeds() \
        .gethiddenfeeds() \
        .getrootrss()

    return mfeeds.results
