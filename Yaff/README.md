###Yaff Yet Another Feed fingy
## Works on Py2.7 < and Py3.4 < , requires 
## requests
## bs4
## validators

#### Example
# Yaff will try to find AND check for feeds (rss and atom even non-compliant) 

```python
from Yaff import get_feeds
guardian = get_feeds("https://www.theguardian.com")
#the result is dictionary of lists
for url,feeds in guardian.items():
    print(url, feeds[0].title,feeds[0].feedtype)
#the list contains namedtuples of title and feedtype 
#to get all feeds that have the same url
for url,feeds in guardian.items():
    print(url)
    for feed in feeds:
        print(feed.title,feed.feedtype)
```
