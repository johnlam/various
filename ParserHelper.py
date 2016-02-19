

class ParserHelper(object):
	
    @staticmethod
    def getnick(line,offset=1,weird=False):
        start = line.find('<') + offset
        end = line.find('>')
        if weird:
            end = end - 1
        return line[start:end].rstrip()


    @staticmethod
    def scrollback(line):
        if line[0] == '[' and line[9] == ']':
            return line.replace(line[0:10],'')
        return line


    @staticmethod
    def gettext(line,offset=1):
        start = line.find('\t') + offset
        end = line.find('\n')
        return ParserHelper.scrollback(line[start:end])
