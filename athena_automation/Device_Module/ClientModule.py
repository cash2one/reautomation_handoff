__author__ = 'rrkrishnan'
import platform
platForm = platform.platform()
if "Linux" in platForm:
    import pexpect as winpexpect
else:
    import winpexpect
import logging
log = logging.getLogger('athenataf')
import datetime
import sys
import os
import subprocess
import dataStructure
import tempfile
import time
from errorsModule import *
from athenataf.config import fwork
import const
import subprocess
import paramiko

class ClientSession():
    def __init__(self, deviceObjectRef):
        self.myDevice  = deviceObjectRef
        self.plink_path = os.path.join(fwork.THIRD_PARTY_DIR, "utils", "plink.exe")

    def connect(self, protocol='ssh', type='eth_ip'):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if type == "ip":
            self.ssh.connect(self.myDevice.get("ip"), username=self.myDevice.get("username"), password=self.myDevice.get("password"), timeout=999999)
            self.execute("netsh interface set interface name=\"Wi-Fi\" admin=ENABLED")
        else:
            self.ssh.connect(self.myDevice.get("eth_ip"), username=self.myDevice.get("username"), password=self.myDevice.get("password"), timeout=999999)
            self.execute("netsh interface set interface name=\"Wi-Fi\" admin=ENABLED")

    def execute(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        log.info(stderr.read())
        self.output = stdout.read()
        log.info(self.output)
        return 1

    def disconnect(self):
        #self.execute("netsh interface set interface name=\"Wi-Fi\" admin=DISABLED")
        self.ssh.close()


    