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

class IAPSession():
    def __init__(self, deviceObjectRef):
        self.myDevice  = deviceObjectRef
        
    def connect(self, protocol='ssh'):
        self.protocol       = self.myDevice.get("protocol")
        self.output         = ''
        self.execStartTime  = ''
        self.execEndTime    = ''
        self.configStartTime = ''
        self.configEndTime   = ''
        self.cmdBuffer = ''

        if protocol == 'ssh':
            import platform
            platForm = platform.platform()

            if "Linux" in platForm:
                cmd = "ssh %s@%s" %(self.myDevice.get('username'), self.myDevice.get('serverIp'))
            else:
                #cmd = "ssh -l %s " % (self.myDevice.get('username'))
                if self.myDevice.get('exePath') != 0:
                    cmd = "%s -ssh %s -l %s -pw %s" %(self.myDevice.get('exePath'), self.myDevice.get('serverIp'), self.myDevice.get("username"), self.myDevice.get("password"))
                else:
                    cmd = "plink.exe -ssh %s -l %s -pw %s" % (self.myDevice.get('serverIp'), self.myDevice.get("username"), self.myDevice.get("password"))
        else:
            cmd = "telnet "
            cmd = cmd + self.myDevice.get('serverIp')
        
        print('%s\n' %(cmd))
        
        self.cmd                = cmd
        if "Linux" in platForm:
            self.connectId          = winpexpect.spawn(self.cmd)
        else:
            self.connectId          = winpexpect.winspawn(self.cmd)
        self.connectId.logfile_read = dataStructure.myTempFile()
        try:
            self.getPrompt()
            self.flush()
        except Exception as err:
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
        patList = ['User: $',                           'assword: $',                        '\[confirm\] $',
                                 '\[confirm yes/no\]:',                '\[yes/no\]:',                       '\(yes/no\)\?',
                                 '\(y/n\)',                           '--More--',                          prompt,
                                 ':~\$',                           winpexpect.TIMEOUT,                      winpexpect.EOF]
        cpl      = self.connectId.compile_pattern_list(patList)
            
        while True: 
            index = self.connectId.expect(cpl,timeout)
            try:
                out = self.connectId.before + self.connectId.after
            except:
                out = self.connectId.before
            self.output += out
            print self.output
            i = 0

            if index == 0+i: 
                ## Login: $
                self.connectId.sendline(self.myDevice.get('username'))
                out = self.connectId.before + self.connectId.after
                self.output += out
                try:
                    self.connectId.expect('assword:',10)
                except winpexpect.TIMEOUT:
                    pass
                else:
                    self.connectId.sendline(self.myDevice.get('password'))
                    out = self.connectId.before + self.connectId.after
                    self.output += out
            elif index == 1+i:
                ## assword: $
                self.connectId.sendline(self.myDevice.get('password'))
                out = self.connectId.before + self.connectId.after
                self.output += out
                try:
                    self.connectId.expect('assword:', 10)
                except winpexpect.TIMEOUT:
                    pass
                else:
                    self.connectId.sendline(self.myDevice.get('password'))
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

    def transmit(self, cmd): 
        self.connectId.write("%s\n" %cmd)
    
    def receive(self, pattern, timeout=-1): 
        cpl = self.connectId.compile_pattern_list(pattern)
        try:
            self.connectId.expect(cpl,timeout)
            try:
                out = self.connectId.before + self.connectId.after
                self.output += out
                return self.output
            except:
                out = self.connectId.before
                self.output += out
                return 0
        except winpexpect.EOF as err:
            try:
                out = self.connectId.before 
                self.output += out
                raise
            except:
                raise
        except winpexpect.TIMEOUT as err:
            try:
                out = self.connectId.before
                self.output += out
                return 0
            except:
                return 0

    def flush(self): 
        """ This will flush any data in expect buffer"""
        self.receive('.*',1)
        self.output = ''
    

    def execute(self,cmd,timeout=-1): 
        self.execStartTime = datetime.datetime.now().time()
        self.flush()
        self.connectId.sendline("")
        try:
            self.getPrompt(timeout)
        except Exception as err:
            self.execEndTime = datetime.datetime.now().time()
            print('%s' %err)
            raise

        for line in cmd.splitlines():
            try:
                self.connectId.send("%s\r" %line)
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
    
    def logSession(self,timestamp): 
        self.connectId.logfile_read.seek(0)
        temp = self.connectId.logfile_read.read()
        #print(temp,also_console=False,timestamp=timestamp)
        print temp
        self.connectId.logfile_read.seek(0)
        self.connectId.logfile_read.truncate()    

