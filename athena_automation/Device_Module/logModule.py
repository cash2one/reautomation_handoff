import robot.api.logger 
from robot.output import Message
from robot.output.logger import LOGGER
import threading
from robot.running.timeouts import timeoutthread
import sys
from dataStructure import nestedDict
import const

LOGGING_THREADS = ('MainThread', timeoutthread.TIMEOUT_THREAD_NAME)

threadDict = nestedDict()
logThreadLock = threading.Lock()
debugLogLevel = 0
def info(msg, html=False, also_console=True,timestamp=None):
    currentThread = threading.currentThread()
    if currentThread.getName() in LOGGING_THREADS:
        logMsg = Message(msg, 'INFO', html, timestamp=timestamp)
        LOGGER.log_message(logMsg)
        if also_console:
            sys.__stdout__.write('\n %s' %(msg))
    else:
        if also_console:
             sys.__stdout__.write("\n%s" %(msg))
        logMsg = Message(msg,'INFO',html,timestamp=timestamp)
        if currentThread in threadDict:
            threadDict[currentThread]['msgList'].append(logMsg)
        else:
            threadDict[currentThread]['msgList'] = []
            threadDict[currentThread]['msgList'].append(logMsg)

def step(msg, html=True, also_console=True, timestamp=None):
    strLen = len(msg)
    fontTag = '<font size = 3 color="blue" style="background: #ADD8E6;"> '
    fontEndTag = '</font>'
    info("%s %s %s" %(fontTag, msg, fontEndTag), html, also_console=False,timestamp=timestamp)
    if also_console:
        sys.__stdout__.write("\nSTEP : %s" %(msg))

def error(msg, html=True, also_console=False,timestamp=None):
    fontTag = '<font color=\"red\"><b> ERROR: '
    fontEndTag = '</b></font>'
    info("%s %s %s" %(fontTag, msg, fontEndTag), html, also_console=False,timestamp=timestamp)
    if also_console:
        sys.__stdout__.write('\nERROR: %s' %(msg))

def fail(msg, html=True, also_console=True,timestamp=None):
    fontTag = '<font color=\"red\"><b> FAIL:'
    fontEndTag = '</b>,</font>'
    info("%s %s %s" %(fontTag, msg, fontEndTag), html, also_console=False,timestamp=timestamp)
    if also_console:
        sys.__stdout__.write('\nFAIL: %s' %(msg))

def success(msg, html=True, also_console=True,timestamp=None):
    fontTag = '<font color=\"green\"><b> PASS:'
    fontEndTag = '</b></font>'
    info("%s %s %s" %(fontTag, msg, fontEndTag), html, also_console=False,timestamp=timestamp)
    if also_console:
        sys.__stdout__.write('\nPASS: %s' %(msg))

def debug(msg, html=True, timestamp=None, level=0):
    currentThread = threading.currentThread()
    if currentThread.getName() in LOGGING_THREADS:
        if level <= debugLogLevel:
            logMsg = Message(msg, 'DEBUG', html, timestamp=timestamp)
            LOGGER.log_message(logMsg)
    else:
        if level <= debugLogLevel:
            logMsg = Message(msg,'DEBUG',html,timestamp=timestamp)
            if currentThread in threadDict:
                threadDict[currentThread]['msgList'].append(logMsg)
            else:
                threadDict[currentThread]['msgList'] = []
                threadDict[currentThread]['msgList'].append(logMsg)

    
def flushThreadLog(threadList):
    #global threadDict
    #global logThreadLock
    currentThread = threading.currentThread()
    for thread in threadList:
        if thread == currentThread:
            continue
        elif currentThread.getName() not in LOGGING_THREADS:
            for msg in threadDict[thread]['msgList']:
                logThreadLock.acquire()
                debug('flushThreadLog - lock acquired by thread %s' %thread.threadId, level=const.LEVEL4)
                try:
                    threadDict[currentThread]['msgList'].append(msg)
                except:
                    sys.__stdout__.write(sys.exc_info())
                    logThreadLock.release()
                    debug('flushThreadLog - lock released by thread %s' %thread.threadId, level=const.LEVEL4)
                logThreadLock.release()
                debug('flushThreadLog - lock released by thread %s' %thread.threadId, level=const.LEVEL4)
            threadDict.pop(thread, None)
        else:
            for msg in threadDict[thread]['msgList']:
                LOGGER.log_message(msg)
            threadDict.pop(thread, None)

def testcase_log(f10TcInfo, tcid=None, result='PASS'):
    if tcid is None:
        msgList = f10TcInfo['msgList']
        timestampList = f10TcInfo['timestamps']
        if f10TcInfo['result']:
            result = f10TcInfo['result']
    else:
        msgList = f10TcInfo[tcid]['msgList']
        timestampList = f10TcInfo[tcid]['timestamps']
        if f10TcInfo[tcid]['result']:
            result = f10TcInfo[tcid]['result']
    for msg,timestamp in zip(msgList, timestampList) :
        info(msg,timestamp=timestamp,also_console=False)
    if result == 'FAIL' or result == 'Terminated':
        assert False, "Test failed"


def setup_log(setupLog):
    msgList = setupLog["msgList"]
    timestampList = setupLog["timestamps"]
    for msg, timestamp in zip(msgList, timestampList):
        info(msg, timestamp=timestamp, also_console=False)

def cleanup_log(cleanupLog):
    msgList = cleanupLog["msgList"]
    timestampList = cleanupLog["timestamps"]
    for msg, timestamp in zip(msgList, timestampList):
        info(msg, timestamp=timestamp, also_console=False)

