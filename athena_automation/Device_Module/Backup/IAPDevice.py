import ObjectModule
import os
import IAPModule
import sys
import re
import const
import time
from errorsModule import configFailed, reloadFailed

class IAPDevice(ObjectModule.Device):
    def __init__(self, varName = None):
        #-----------------------------------------------------------------------
        # Choose the platform depends on Map File information.
        #-----------------------------------------------------------------------
        self.userDialogueResponse = {}

        ObjectModule.Device.__init__(self,"SERVER", varName)
        if varName is None:
            self.name = self.__class__.__name__
        else:
            self.name = varName
        self.session = IAPModule.IAPSession(deviceObjectRef=self)

    def connect(self, protocol='ssh'):
        self.session.connect(protocol)
    
    def getPrompt(self):
        self.transmit('\n')
        return self.session.getPrompt()
        
    def disconnect(self):
        self.session.disconnect()

    def transmit(self, transCommands):
        self.session.transmit(transCommands)

    def receive(self,pattern,timeout=-1):
        return self.session.receive(pattern,timeout)

    def execute(self, execCommands,timeout=-1):
        self.session.execute(execCommands,timeout)
        return self.session.output
        
    def get(self,var):
        if hasattr(self, var) :
            return getattr(self,var)
        else :
            return const.FALSE 
