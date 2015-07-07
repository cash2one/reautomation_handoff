import re
import sys
import const
import threading
from errorsModule import devObjExists, noSuchClass, noDeviceObjAvailable

class Device(object):
    device = {}
    allInstances = {}
    lock = threading.Lock()
    def __init__(self, p_Product="IAP",varName=None):
        self.productType = p_Product
        self.updateDeviceDict(varName)
        self.updateAllInstances()

    def updateDeviceDict(self, varName):
        self.lock.acquire()
        try:
            print('updateDeviceDict - lock acquired by class %s' %(self.__class__.__name__))
            if varName is None:
                self.device[self.__class__.__name__] = self
            else:
                self.device[varName] = self
            print('updateDeviceDict - lock released by class %s' %(self.__class__.__name__))
        except:
            print(sys.exc_info())
        self.lock.release()
        

    def updateAllInstances(self):
        self.lock.acquire()
        print('updateAllInstances - lock acquired by class %s' %(self.__class__.__name__))
        if self.__class__.__name__ not in self.allInstances:
            self.allInstances[self.__class__.__name__] = []
        self.allInstances[self.__class__.__name__].append(self)
        print('updateAllInstances - lock released by class %s' %(self.__class__.__name__))
        self.lock.release()
            
    def getAllInstances(self):
        self.lock.acquire()
        print('getAllInstances - lock acquired by class %s' %self.__class__.__name__)
        if self.__class__.__name__ in self.allInstances:
            objList = self.allInstances[self.__class__.__name__]
        else:
            objList = []
        print('getAllInstances - lock released by class %s' %self.__class__.__name__)
        self.lock.release()
        return objList

    @classmethod
    def getDeviceClassRef(cls, devObjString):
        try:
            devObj = cls.getDeviceObject(devObjString)
            return devObj.__class__
        except:
            raise noSuchClass('no such class for string %s' %devObjString)

    @classmethod
    def getDeviceObject(cls, devObjString):
        cls.lock.acquire()
        print('getDeviceObject - lock acquired by string %s' %(devObjString))
        if devObjString in cls.device:
            obj = cls.device[devObjString]
            print('getDeviceObject - device keys %s' %(cls.device.keys()))
            cls.lock.release()
            print('getDeviceObject - lock released by string %s' %(devObjString))
            return obj
        else:
            cls.lock.release()
            print('getDeviceObject - lock released by string %s' %(devObjString))
            raise noDeviceObjAvailable('no device object created with string %s' %devObjString)
            
    @classmethod
    def createDeviceObject(cls, classNameString, devObjString):
        try:
            cls.getDeviceObject(devObjString)
        except:
            classRef = cls.getDeviceClassRef(classNameString)
            devObj = classRef(devObjString)
            return devObj
        else:
            raise devObjExists('device with string %s already exists' %devObjString)

##class Device --Definition Over
