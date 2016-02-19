from collections import defaultdict


class IRCNicks(object):
    def __init__(self):
        self._users = defaultdict(list)

    def addquote(self,nick,quote):
        self._users[nick].append(quote)

    def getquotes(self,nick):
        return self._users[nick]

    def __len__(self):
        return len(self._users.keys())
    
    def __getitem__(self, nick):
        return self._users[nick]

    def __setitem__(self, nick, quote):
        self._users[nick].append(quote)

    def __delitem__(self, nick):
        del self._users[nick]

    def __iter__(self):
        return iter(self._users.items())