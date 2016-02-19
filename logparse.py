from dateutil import parser
from ParserHelper import ParserHelper as phelp
from IRCNicks import IRCNicks

STDDATE = 16

def start(logfile):
    ''' An Xchat log parser that stores
    nicknames as keys and quotes as a list of strings"

    f = open(logfile,"r")
    ircnicks = IRCNicks()

    for line in f.readlines():
        if line[0] == '*' or len(line) < 20:
            continue
        if line[16:22] == 'Python' or line[16:19] == 'Tcl':
            continue
        if line[0] != 'T' and line[STDDATE] != '*':
            #dtime = parser.parse(line[0:15])
            nick = phelp.getnick(line)
            text = phelp.gettext(line)
            ircnicks.addquote(nick,text)
            #print dtime , nick , text
        elif line[0] == 'T' and line[STDDATE] != '*':
            nick = phelp.getnick(line,2,True)
            text = phelp.gettext(line)
            ircnicks.addquote(nick,text)
            
    f.close()
    return ircnicks

