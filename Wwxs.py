import cPickle as pickle
import markovify
import saxo

class Wwxs(object):
    def __init__(self,nick):
        p = pickle.load(open("mymodel.p"))
        if nick not in p:
            self.sentence = 'No data for ' + nick
        else:
            hmmodels = markovify.Text(" ".join(seq[nick]))
            self.sentence = hmmodels.make_sentence()

    def __str__(self):
        return self.sentence

@saxo.pipe
def wwxs(arg):
    if not arg:
        return "Example: .wwxs 'nickname'"
    return str(Wwxs(arg))