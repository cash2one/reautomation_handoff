import ObjectModule
import os
import IAPModule
import sys
import re
import const
import time
from errorsModule import configFailed, reloadFailed
from athenataf.config.device_command_map import CommandMap
import logging
log = logging.getLogger('athenataf')

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

    def connect(self, protocol='telnet'):
        try:
            self.session.connect(protocol)
            #self.connect_device_to_server()
        except Exception as err:
            log.info("PRINTING ERROR IN CONNECT : %s" %err)
            #self.session.connect(protocol)
            self.reconnect()

    def setUsername(self, username):
        setattr(self.session, "username", username)

    def setPassword(self, password):
        setattr(self.session, "password", password)

    def reload(self):
        self.session.receive("#")
        self.session.transmit("reload")
        time.sleep(200)
        self.reconnect()


    def reconnect(self, username='admin', password='admin'):
        try:
            self.session.disconnect()
        except:
            pass
        self.session.connect(username=username, password=password)
        self.connect_device_to_server()
    
    def getPrompt(self):
        #self.transmit('\n')
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

    def get_running_config(self, extra_command=None):
        '''
        Run "Show running-config" command.
        Search for command in device_command_map .
        If command not present in device version map , pull command line from common map .
        '''
        # command_key = "GET_RUN_CONFIG"
        if not extra_command:
            command_key = "GET_RUN_CONFIG"
        else:
            command_key = extra_command
        version_specific_map = CommandMap.__dict__[self.get("type")]
        common_map = CommandMap.__dict__[self.get("type") + "_COMMON"]
        command_line = None
        versions = version_specific_map.keys()
        if versions.count(self.get("version")) != 0:
            for version in versions[versions.index(self.get("version")):]:
                command_line = version_specific_map[version].get(command_key, None)
                if command_line is not None: break
        if command_line is None:
            command_line = common_map.get(command_key, None)
        print command_key
        if command_key is None:
            raise Exception("Check your command map. Command not available for the mentioned device and version.")
        else:
            try:
                self.receive("#")
                self.transmit(command_line)
                output = self.receive("#")
            except Exception as err:
                log.error(err)
            return output

    def get_device_status(self, strict=False):
        '''
        Checks device status by running "show ap debug athena" command .
        '''
        command_key = "GET_DEVICE_STATUS"
        print self.get("type")
        version_specific_map = CommandMap.__dict__[self.get("type")]
        common_map = CommandMap.__dict__[self.get("type") + "_COMMON"]
        command_line = None
        versions = version_specific_map.keys()
        log.info(versions)
        if versions.count(self.get("version")) != 0:
            for version in versions[versions.index(self.get("version")):]:
                command_line = version_specific_map[version].get(command_key, None)
                if command_line is not None: break
        if command_line is None:
            command_line = common_map.get(command_key, None)
        if command_key is None:
            raise Exception("Check your command map. Command not available for the mentioned device and version.")
        else:
            try:
                self.receive("#")
                self.transmit(command_line)
                output = self.receive("#")
                log.info("PRINTING THE OUTPUT HERE ...........................")
                log.info(output)
                log.info("#" * 80)
                current_status_list = output.split()
            except Exception as err:
               log.error(err)
            print "STATUS OF DEVICE : %s" %(':success' in current_status_list)
            if strict:
                if not (':success' in current_status_list):
                    self.connect_device_to_server()
                    time.sleep(40)
                    self.get_device_status()
                else:
                    return True
            else:
                return (':success' in current_status_list)

    def connect_device_to_server(self, serverIp=None):
        '''
        connects the device to the athena server by running "debug-athena-server" command
        '''
        import re

        command_key = "PULL_DEVICE_UP"
        version_specific_map = CommandMap.__dict__[self.get("type")]
        common_map = CommandMap.__dict__[self.get("type") + "_COMMON"]
        command_line = None
        versions = version_specific_map.keys()
        if versions.count(self.get("version")) != 0:
            for version in versions[versions.index(self.get("version")):]:
                command_line = version_specific_map[version].get(command_key, None)
                if command_line is not None: break
        if command_line is None:
            command_line = common_map.get(command_key, None)
        if command_key is None:
            raise Exception("Check your command map. Command not available for the mentioned device and version.")
        else:
            try:
                self.receive("#")
                if serverIp is None:
                    self.transmit(command_line + self.server)
                else:
                    self.transmit(command_line + serverIp)
                output = self.receive("#")
            except Exception as err:
                log.error(err)
            return output
