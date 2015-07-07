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
import os
import dataStructure
from errorsModule import *
from athenataf.config import fwork

class ClientSession():
    def __init__(self, deviceObjectRef):
        self.myDevice  = deviceObjectRef
        self.plink_path = os.path.join(fwork.THIRD_PARTY_DIR, "utils", "plink.exe")

    def connect(self, protocol='ssh', type='ip'):
        self.protocol = self.myDevice.get("protocol")
        self.output = ''
        self.execStartTime = ''
        self.execEndTime = ''
        self.configStartTime = ''
        self.configEndTime = ''
        self.cmdBuffer = ''

        if protocol == 'ssh':
            import platform

            platForm = platform.platform()

            if "Linux" in platForm:
                cmd = "ssh %s@%s" % (self.myDevice.get('username'), self.myDevice.get('eth_ip'))
            else:
                # cmd = "ssh -l %s " % (self.myDevice.get('username'))
                cmd = "%s -ssh %s -l %s -pw %s" % (self.plink_path, self.myDevice.get('eth_ip'), self.myDevice.get("username"),self.myDevice.get("password"))
        else:
            cmd = "telnet "
            cmd = cmd + self.myDevice.get('serverIp')

        print('%s\n' % (cmd))

        self.cmd = cmd
        if "Linux" in platForm:
            self.connectId = winpexpect.spawn(self.cmd)
        else:
            self.connectId = winpexpect.winspawn(self.cmd)
        self.connectId.logfile_read = dataStructure.myTempFile()
        try:
            self.getPrompt()
            self.connectId.sendline("netsh interface set interface name='Wi-Fi' admin=ENABLED")
            self.flush()
        except Exception as err:
            print('%s' % err)
            raise


    def disconnect(self):
        self.connectId.logfile_read.close()
        self.connectId.terminate()

    def idleTimerReset(self):
        self.connectId.logfile_read.timer.reset()

    def getIdleTime(self):
        return self.connectId.logfile_read.timer.getTimerValue()

    def getPrompt(self, prompt="#", timeout=-1, idleTimeout=60):
        timeoutAttemptCount  = 1
        notIdleRetryCount = 1
        wrongPasswordCount = 1
        maxNotIdleRetryCount = 15
        out      = ''
        self.idleTimerReset()
        username = self.myDevice.get('username')
        userPatList = self.myDevice.userDialogueResponse.keys()
        patList = [ "login as:",                    "assword:",         username + ">",
                    winpexpect.TIMEOUT,                      winpexpect.EOF]

        cpl      = self.connectId.compile_pattern_list(patList)

        while True:
            index = self.connectId.expect(cpl,timeout)

            out = self.connectId.before
            self.output += out
            for i in range(len(userPatList)):
                if index == i:
                    self.connectId.sendline(self.myDevice.userDialogueResponse[userPatList[i]])
            i = len(userPatList)

            if index == 0+i:
                ## Login: $
                self.connectId.sendline(self.myDevice.get('username'))
                out = self.connectId.after
                self.output += out
                try:
                    self.connectId.expect('assword:',10)
                except winpexpect.TIMEOUT:
                    pass
                else:
                    self.connectId.sendline(self.myDevice.get('password'))
                    out = self.connectId.after
                    self.output += out
            elif index == 1+i:
                ## assword: $
                self.connectId.sendline(self.myDevice.get('password'))
                out = self.connectId.after
                self.output += out
            elif index == 2+i:
                ## > prompt
                self.connectId.sendline()
                return 1
            elif index == 18+i:
                ## winpexpect.TIMEOUT
                idleTimer = self.getIdleTime()
                if idleTimer < idleTimeout:
                    self.connectId.before = ''
                    self.connectId.after = ''
                    log.debug('idle timer %s' %idleTimer)
                    if notIdleRetryCount > maxNotIdleRetryCount:
                        raise winpexpect.TIMEOUT('connection timed out')
                    notIdleRetryCount += 1
                else:
                    if timeoutAttemptCount < 2:
                        self.connectId.sendline()
                        timeoutAttemptCount += 1
                    else:
                        raise winpexpect.TIMEOUT('connection timed out')
            elif index == 19+i:
                ## winpexpect.EOF
                raise winpexpect.EOF('connection terminated')


    def transmit(self, cmd):
        self.connectId.write("%s\n" %cmd)


    def receive(self, pattern, timeout=-1):
        cpl = self.connectId.compile_pattern_list(pattern)
        try:
            self.connectId.expect(cpl,timeout)
            try:
                out = self.connectId.before + self.connectId.after
                self.output += out
                self.logSession()
                return self.output
            except:
                out = self.connectId.before
                self.output += out
                self.logSession()
                return 0
        except winpexpect.EOF as err:
            try:
                out = self.connectId.before
                self.output += out
                self.logSession()
                raise
            except:
                self.logSession()
                raise
        except winpexpect.TIMEOUT as err:
            try:
                out = self.connectId.before
                self.output += out
                self.logSession()
                return 0
            except:
                self.logSession()
                return 0



    def flush(self):
        """ This will flush any data in expect buffer"""
        self.receive('.*',1)
        self.output = ''


    def execute(self,cmd,timeout=-1):
        self.execStartTime = datetime.datetime.now().time()
        self.flush()
        self.connectId.sendline()

        try:
            self.getPrompt('exec',timeout)
        except Exception as err:
            self.execEndTime = datetime.datetime.now().time()
            self.logSession()
            raise sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]

        for line in cmd.splitlines():
            try:
                self.connectId.sendline(line)
                self.getPrompt('exec',timeout)
            except:
                self.execEndTime = datetime.datetime.now().time()
                self.logSession()
                raise sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]

        self.execEndTime = datetime.datetime.now().time()
        self.logSession()

    def flushCmdBuffer(self):
        cmd = self.cmdBuffer
        if cmd:
            self.configure(cmd)
        self.cmdBuffer = ''

    def logSession(self):
        self.connectId.logfile_read.seek(0)
        temp = self.connectId.logfile_read.read()
        log.info(temp)
        self.connectId.logfile_read.seek(0)
        self.connectId.logfile_read.truncate()



