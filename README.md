###Some of my silly [saxo](https://github.com/sbp/saxo) scripts and an xchat logparser

#### For the logparser
```python
import logparser
channel = logparser.start("##mychannel.txt")
print channel['nick'][0]
```
