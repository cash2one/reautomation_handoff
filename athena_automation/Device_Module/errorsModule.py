import traceback
import sys
def getTraceback(tbObj):
    tb = 'Traceback (most recent call last):\n'
    tbList = traceback.extract_tb(tbObj)
    for file, line, func, caller in iter(tbList):
        tb += 'File %s, line %s, in %s\n %s\n' %(file, line, func, caller)
    sys.__stdout__.write(tb)
    return tb

class configFailed(Exception):
    pass

class reloadFailed(Exception):
    pass

class noDeviceObjAvailable(Exception):
    pass

class noSuchClass(Exception):
    pass

class devObjExists(Exception):
    pass
