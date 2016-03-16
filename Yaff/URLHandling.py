
try:
    from urlparse import urlparse,urljoin
except ImportError:
    from urllib.parse import urlparse,urljoin

import validators


class URLHandler(object):
    @staticmethod
    def is_valid(url):
        return validators.url(url)

    @staticmethod
    def get_full_urls(base, url):
        if not URLHandler.is_valid(base):
            raise ValueError('URL is not valid. Check for missing scheme (i.e. http(s))')
        if URLHandler.is_absolute(url):
            return url
        return urljoin(base, url)

    @staticmethod
    def is_absolute(url):
        return bool(urlparse(url).netloc)

    @staticmethod
    def get_provider(url, scheme=True):
        if scheme:
            return URLHandler.get_base_with_scheme(urlparse(url).netloc)
        return urlparse(url).netloc

    @staticmethod
    def get_base_with_scheme(url):
        if url.startswith('https://') or url.startswith('http://'):
            return url
        else:
            return 'http://' + url

    @staticmethod
    def is_root(url):
        ups = urlparse(url)
        if (ups.path == '/' or ups.path == '') and ups.query == '':
            return True
        return False
