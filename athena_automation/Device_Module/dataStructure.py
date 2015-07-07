import sys
import tempfile
import time
import datetime

class nestedDict(dict):
    def __init__(self, dictionary=None):
        if dictionary is None:
            super(nestedDict, self).__init__()
        else:
            #print 'inside else'
            for key in dictionary.keys():
                val = dictionary[key]
                try:
                    dictionary[key].keys()
                    self[key] = nestedDict(val)
                except:
                    self[key] = val

    def __getitem__(self, key):
        if key in self: return self.get(key)
        return self.setdefault(key, nestedDict())
    def __str__(self,indentationLevel=0,indentationString='    ', out=''):
        if indentationLevel == 0:
            out = '--------------- dict out ----------------\n'
        for key in self.keys():
            val = self[key]
            prntSpace = indentationString * indentationLevel
            width = max([len(str(x)) for x in self.keys()])
            try:
                self[key].keys()
                out += prntSpace + str(key) + '\n'
                out = val.__str__(indentationLevel+1,indentationString, out)
            except:
                sCount = width - len(str(key)) + 15
                out += prntSpace + str(key) + ' ' * sCount + '= ' + str(val) + '\n'
        if indentationLevel == 0:
            out += '------------------------------------------\n'
            return out
        else:
            return out

class Timer(object):
    def __init__(self):
        self.startTime = time.time()
    def reset(self):
        self.startTime = time.time()
    def getTimerValue(self):
        currentTime = time.time()
        delta = currentTime - self.startTime
        return delta

class myTempFile(file):
    def __init__(self):
        self.tempFile = tempfile.TemporaryFile()
        self.timer = Timer()
    def write(self, *args, **kwargs):
        self.tempFile.write(*args, **kwargs)
        sys.__stdout__.write(*args, **kwargs)
        sys.__stdout__.flush()
        self.tempFile.flush()
        self.timer.reset()
    def writelines(self, *args, **kwargs):
        self.tempFile.writelines(*args, **kwargs)
        sys.__stdout__.writelines(*args, **kwargs)
    def close(self, *args, **kwargs):
        self.tempFile.close(*args, **kwargs)
    def fileno(self, *args, **kwargs):
        return self.tempFile.fileno(*args, **kwargs)
    def flush(self, *args, **kwargs):
        self.tempFile.flush(*args, **kwargs)
    def isatty(self, *args, **kwargs):
        return self.tempFile.isatty(*args, **kwargs)
    def newlines(self, *args, **kwargs):
        self.tempFile.newlines(*args, **kwargs)
    def next(self, *args, **kwargs):
        self.tempFile.next(*args, **kwargs)
    def read(self, *args, **kwargs):
        return self.tempFile.read(*args, **kwargs)
    def readinto(self, *args, **kwargs):
        return self.tempFile.readinto(*args, **kwargs)
    def readline(self, *args, **kwargs):
        return self.tempFile.readline(*args, **kwargs)
    def readlines(self, *args, **kwargs):
        return self.tempFile.readlines(*args, **kwargs)
    def seek(self, *args, **kwargs):
        self.tempFile.seek(*args, **kwargs)
    def tell(self, *args, **kwargs):
        return self.tempFile.tell(*args, **kwargs)
    def truncate(self, *args, **kwargs):
        self.tempFile.truncate(*args, **kwargs)
    def xreadlines(self, *args, **kwargs):
        return self.tempFile.xreadlines(*args, **kwargs)


def get_timestamp():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return st
