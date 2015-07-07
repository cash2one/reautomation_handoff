__author__ = 'rrkrishnan'

import ObjectModule
import ClientModule
import const
import logging
log = logging.getLogger('athenataf')

class ClientDevice(ObjectModule.Device):
    def __init__(self, varName = None):
        #-----------------------------------------------------------------------
        # Choose the platform depends on Map File information.
        #-----------------------------------------------------------------------
        self.userDialogueResponse = {}

        ObjectModule.Device.__init__(self,"ARUBA", varName)
        if varName is None:
            self.name = self.__class__.__name__
        else:
            self.name = varName
        self.session = ClientModule.ClientSession(deviceObjectRef=self)

    def connect(self, protocol='ssh', type='eth_ip'):
        self.session.connect(protocol, type)

   # def getPrompt(self, prompt):
   #     return self.session.getPrompt(prompt)

    #def reconnect(self):
    #    self.session.connect(protocol=self.session.protocol, type=self.session.type)

    def disconnect(self):
        self.session.disconnect()

    #def transmit(self, transCommands):
    #    self.session.transmit(transCommands)

#    def receive(self,pattern,timeout=-1):
#        return self.session.receive(pattern,timeout)

    def execute(self, execCommands,timeout=-1):
        self.session.execute(execCommands,timeout)
        return self.session.output

    #def flushCmdBuffer(self):
    #    self.session.flushCmdBuffer()

    def get(self,var):
        if hasattr(self, var) :
            return getattr(self,var)
        else :
            return const.FALSE

    def disconnect_client_from_ap(self):
        return self.session.execute("netsh interface set interface name=\"Wi-Fi\" admin=DISABLED")

    def connect_client_to_ap(self, SSID=None):
        self.session.execute("netsh interface set interface name=\"Wi-Fi\" admin=ENABLED")
        import time
        time.sleep(10)
        if SSID is None:
            self.session.execute("netsh wlan connect name=TEST_Monitoring")
        else:
            self.session.execute("netsh wlan connect name=%s" %SSID)
        if not "success" in self.session.output:
            log.error("Not connected")
            return False

