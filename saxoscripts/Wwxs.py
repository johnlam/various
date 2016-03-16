#!/usr/bin/env python
import markovify
import json

class Wwxs(object):

    def __init__(self,nick):
        p = json.load(open("model.json","r"))
        if nick not in p["_users"]:
            self.sentence = 'No data for '+ nick
        else:
            hmmodels = markovify.Text(" ".join(p["_users"][nick]))
            self.sentence = hmmodels.make_sentence()
            if self.sentence is None:
                self.sentence = hmmodels.make_short_sentence(50)
            print type(self.sentence)
            print len(self.sentence), type(self.sentence)

    def __str__(self):
        return self.sentence

print(Wwxs("saml"))
