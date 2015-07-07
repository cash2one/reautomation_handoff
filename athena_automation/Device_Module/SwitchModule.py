import platform
platForm = platform.platform()
if "Linux" in platForm:
    import pexpect as winpexpect
else:
    import winpexpect 
import datetime
import dataStructure
from errorsModule import *
import const
import os
from athenataf.config import fwork
import logging
log = logging.getLogger("athenataf")

class SwitchSession():
    def __init__(self, deviceObjectRef):
        self.myDevice  = deviceObjectRef
        self.plink_path = os.path.join(fwork.THIRD_PARTY_DIR, "utils", "plink.exe")
        
    def connect(self, protocol='telnet', username="", password=""):
        self.password = password
        self.username = username
        self.protocol       = self.myDevice.get("protocol")
        self.output         = ''
        self.execStartTime  = ''
        self.execEndTime    = ''
        self.configStartTime = ''
        self.configEndTime   = ''
        self.cmdBuffer = ''
        if username == "":
            self.username = self.myDevice.get("username")
        if password == "":
            self.password = self.myDevice.get("password")
        platForm = platform.platform()
        if protocol == 'ssh':
            if "Linux" in platForm:
                cmd = "ssh %s@%s" %(self.myDevice.get('username'), self.myDevice.get('ip'))
            else:
                #cmd = "ssh -l %s " % (self.myDevice.get('username'))
                cmd = "%s -ssh %s -l %s -pw %s" %(self.plink_path, self.myDevice.get('ip'), self.username, self.password)
        else:
            if "Linux" in platForm:
                cmd = "telnet %s %s" %(self.myDevice.get('consoleIp'), self.myDevice.get("port"))
            else:
                cmd = "%s -telnet %s -P %s" % (self.plink_path, self.myDevice.get('consoleIp'), self.myDevice.get("port"))
        
        print('%s\n' %(cmd))
        
        self.cmd                = cmd
        if "Linux" in platForm:
            self.connectId          = winpexpect.spawn(self.cmd)
        else:
            self.connectId          = winpexpect.winspawn(self.cmd)
        self.connectId.logfile_read = dataStructure.myTempFile()
        timestamp = dataStructure.get_timestamp()
        try:
            self.getPrompt()
            self.flush()
        except Exception as err:
            self.logSession(timestamp)
            print('%s' %err)
            raise

    
            
    def disconnect(self): 
        self.connectId.logfile_read.close()
        self.connectId.terminate()
    

    def idleTimerReset(self): 
        self.connectId.logfile_read.timer.reset()
    

    def getIdleTime(self): 
        return self.connectId.logfile_read.timer.getTimerValue()
    

    def getPrompt(self, timeout=-1, idleTimeout=60):

        timeoutAttemptCount  = 1
        notIdleRetryCount = 1
        wrongPasswordCount = 1
        maxNotIdleRetryCount = 15
        out      = ''
        self.idleTimerReset()
        username = self.myDevice.get('username')
        prompt = self.myDevice.get('prompt')
        patList = ['User: $',                           'assword: $',                           '\[confirm\] $',
                   '\[confirm yes/no\]:',               '\[yes/no\]:',                          '\(yes/no\)\?',
                   '\(y/n\)',                           '--More--',                             "\\%s" % (prompt),
                   '\) #',                              winpexpect.TIMEOUT,                     winpexpect.EOF,
                   'Login : $',                         'config\) #',                           '\) >','>>>>>','PoE firmware \[Ok\]','\(y\|n\)\?']
        cpl      = self.connectId.compile_pattern_list(patList)
            
        while True: 
            index = self.connectId.expect(cpl,timeout)
            try:
                out = self.connectId.before + self.connectId.after
            except:
                out = self.connectId.before
            self.output += out
            i = 0
            if index == 0+i:
                ## Login: $
                self.connectId.sendline(self.username)
                try:
                    self.connectId.expect('assword: ',10)
                except winpexpect.TIMEOUT:
                    pass
                else:
                    print "PRINTING HERE"
                    self.connectId.sendline(self.password)
                    out = self.connectId.before + self.connectId.after
                    self.output += out
            elif index == 1+i:
                ## assword: $
                self.connectId.sendline(self.password)
                out = self.connectId.before + self.connectId.after
                self.output += out
            elif index == 2+i:
                ## \[confirm\] $
                self.connectId.sendline()
            elif index == 3+i:
                ## \[confirm yes/no\]:
                self.connectId.sendline('yes')
                out = self.connectId.before + self.connectId.after
                self.output += out
            elif index == 4+i:
                ## \[yes/no\]:
                self.connectId.sendline('yes')
                out = self.connectId.before + self.connectId.after
                self.output += out
            elif index == 5+i:
                ## \(yes/no\)\?
                self.connectId.sendline('yes')
                out = self.connectId.before + self.connectId.after
                self.output += out
            elif index == 6+i:
                ## \[y/n\]:
                self.connectId.sendline('y')
                out = self.connectId.before + self.connectId.after
                self.output += out
            elif index == 7+i:
                ## --More--
                self.connectId.sendline(' ')
                out = self.connectId.before + self.connectId.after
                self.output += out
            elif index == 8+i:
                return const.linuxPrompt
            elif index == 9+i:
                #prompt
                return const.oniePrompt
            elif index == 10+i:
                ## pexpect.TIMEOUT
                idleTimer = self.getIdleTime()
                if idleTimer < idleTimeout:
                    self.connectId.before = ''
                    self.connectId.after = ''
#                    log.debug('idle timer %s' %idleTimer, level=const.LEVEL4)
                    if notIdleRetryCount > maxNotIdleRetryCount:
                        raise winpexpect.TIMEOUT('connection timed out')
                    notIdleRetryCount += 1
                else:
                    if timeoutAttemptCount < 2:
                        self.connectId.sendline("")
                        timeoutAttemptCount += 1
                    else:
                        raise winpexpect.TIMEOUT('connection timed out')
            elif index == 11+i:
                ## pexpect.EOF
                raise winpexpect.EOF('connection terminated')
            elif index == 12+i:
                self.connectId.sendline(self.myDevice.get("consoleUsername"))
                try:
                    self.connectId.expect('assword :', 10)
                except winpexpect.TIMEOUT:
                    pass
                else:
                    self.connectId.sendline(self.myDevice.get('consolePassword'))
                    self.connectId.sendline("\r")
                    self.connectId.sendline("%s\r" %self.username)
                    #self.connectId.sendline("test123")
                    self.connectId.sendline("%s\r" %self.password)
                    #if self.connectId.expect("User:"):
                    #self.connectId.sendline("%s\r" % self.username)
                    # self.connectId.sendline("test123")
                    #self.connectId.sendline("admin\r")
                    out = self.connectId.before + self.connectId.after
                    self.output += out
            elif index == 13+i:
                self.connectId.sendline("end")
            elif index == 14 + i:
                self.connectId.sendline("enable")
                try:
                    self.connectId.expect('assword: ', 10)
                except winpexpect.TIMEOUT:
                    pass
                else:
                    self.connectId.sendline(self.myDevice.get('enable'))
                    print "INSIDE EXCEPT BLOCK"
                    out = self.connectId.before + self.connectId.after
                    self.output += out

    def transmit(self, cmd): 
        self.connectId.write("%s\n" %cmd)
    
    def receive(self, pattern, timeout=-1):
        timestamp = dataStructure.get_timestamp()
        self.output = ""
        cpl = self.connectId.compile_pattern_list(pattern)
        try:
            self.connectId.expect(cpl,timeout)
            try:
                out = self.connectId.before + self.connectId.after
                self.output += out
                self.logSession(timestamp)
                return self.output
            except:
                out = self.connectId.before
                self.output += out
                self.logSession(timestamp)
                return self.output
        except winpexpect.EOF as err:
            try:
                out = self.connectId.before 
                self.output += out
                self.logSession(timestamp)
                raise
            except:
                self.logSession(timestamp)
                raise
        except winpexpect.TIMEOUT as err:
            try:
                out = self.connectId.before
                self.output += out
                self.logSession(timestamp)
                return self.output
            except:
                self.logSession(timestamp)
                return self.output

    def flush(self): 
        """ This will flush any data in expect buffer"""
        self.receive('.*',1)
        self.output = ''


    def execute(self,cmd,timeout=-1):
        self.output = ""
        self.execStartTime = datetime.datetime.now().time()
        self.flush()
        self.connectId.sendline("")
        try:
            self.getPrompt(timeout)
            pass
        except Exception as err:
            self.execEndTime = datetime.datetime.now().time()
            print('%s' %err)
            raise

        for line in cmd.splitlines():
            try:
                self.connectId.sendline(line)
                self.getPrompt(timeout)
            except Exception as err:
                self.execEndTime = datetime.datetime.now().time()
                print('%s %s \n%s' %(err[0], err[1], getTraceback(err[2])))
                raise
        self.execEndTime = datetime.datetime.now().time()

    def flushCmdBuffer(self): 
        cmd = self.cmdBuffer
        if cmd:
            self.configure(cmd)
        self.cmdBuffer = ''
    
    def logSession(self, timestamp):
        self.connectId.logfile_read.seek(0)
        temp = self.connectId.logfile_read.read()
        #print(temp,also_console=False,timestamp=timestamp)
        #print temp
        log.info(temp)
        self.connectId.logfile_read.seek(0)
        self.connectId.logfile_read.truncate()    

