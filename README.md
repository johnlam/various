###Some of my silly saxo scripts and an xchat logparser

#### For the logparser
``` import logparser
    channel = logparser.start("##mychannel.txt")
    print channel['nick'][0]
```
