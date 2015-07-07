import sys
import tempfile
import time


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


