import winpexpect
from robot.running import TestSuite
import subprocess
import sys
import re
import os
from robot import utils
from robot.reporting import ResultWriter
import dataStructure
import tempfile
import postProcess
import signal

import yaml

class testInfo(object):
    def __init__(self, scriptName):
        self.scriptName = scriptName
        self.tcInfo = dataStructure.nestedDict()
        self.currentTcid = 'suite_setup'
        self.variableFile = variableFile()
        self.scriptResult = 'FAIL'
    def appendLog(self, msg, timestamp, tcid=None):
        if tcid is None:
            tcid = self.currentTcid
        if 'msgList' not in self.tcInfo[tcid]:
            self.tcInfo[tcid]['msgList'] = []
            self.tcInfo[tcid]['timestamps'] = []
            self.variableFile.initTcInfo(tcid)
        self.tcInfo[tcid]['msgList'].append(msg)
        self.tcInfo[tcid]['timestamps'].append(timestamp)
        self.variableFile.appendLog(tcid, msg, timestamp)
    def setScriptResult(self, status):
        self.scriptResult = status
    def setResult(self, status, tcid=None):
        if tcid is None:
            tcid = self.currentTcid
        self.tcInfo[tcid]['result'] = status
        self.variableFile.setResult(tcid, status)
    def setTcid(self, id):
        self.currentTcid = id
    def setLogFile(self, fileName):
        self.logFileName = fileName
    def flush(self):
        self.variableFile.flush()
    
class variableFile(object):
    def __init__(self):
        #self.file = tempfile.NamedTemporaryFile(dir=None, delete=True, suffix='.py')
        self.file = open("tempFile.py", "w+")
        self.name = self.file.name
        print self.name
        self.file.write('# coding=utf-8\n')
        self.file.write('import dataStructure\n')
        self.file.write('testcaseInfo = dataStructure.nestedDict()\n')
        self.file.write('setupLog = dataStructure.nestedDict()\n')
        self.file.write('cleanupLog = dataStructure.nestedDict()\n')
    def initTcInfo(self, tcid):
        if tcid is 'suite_setup':
            self.file.write('setupLog["msgList"] = []\n')
            self.file.write('setupLog["timestamps"] = []\n')
        elif tcid is 'suite_cleanup':
            self.file.write('cleanupLog["msgList"] = []\n')
            self.file.write('cleanupLog["timestamps"] = []\n')
        else:
            self.file.write('testcaseInfo["%s"]["msgList"] = []\n' %tcid)
            self.file.write('testcaseInfo["%s"]["timestamps"] = []\n' %tcid)
    def appendLog(self, tcid, msg, timestamp):
        if tcid is 'suite_setup':
            self.file.write('setupLog["msgList"].append("%s")\n' %msg)
            self.file.write('setupLog["timestamps"].append("%s")\n' %timestamp)
        elif tcid is 'suite_cleanup':
            self.file.write('cleanupLog["msgList"].append("%s")\n' %msg)
            self.file.write('cleanupLog["timestamps"].append("%s")\n' %timestamp)
        else:
            self.file.write('testcaseInfo["%s"]["msgList"].append("%s")\n' %(tcid, msg))
            self.file.write('testcaseInfo["%s"]["timestamps"].append("%s")\n' %(tcid, timestamp))
    def setResult(self, tcid, status):
        if tcid is 'suite_setup':
            self.file.write('setupLog["result"] = "%s"\n' %status)
        elif tcid is 'suite_cleanup':
            self.file.write('cleanupLog["result"] = "%s"\n' %status)
        else:
            self.file.write('testcaseInfo["%s"]["result"] = "%s"\n' %(tcid, status))
    def flush(self):
        self.file.flush()
    def close(self):
        self.file.close()
        # This will remove the .pyc file created for the variable file
        if os.path.isfile(self.name+'c'):
            os.remove(self.name+'c')


def createRobotSuite(testcaseInfo):
    suite = TestSuite(os.path.basename(testcaseInfo.scriptName))
    suite.imports.library('logModule')
    suite.imports.variables(testcaseInfo.variableFile.name)
    tcList = [val for val in testcaseInfo.tcInfo.keys() if val not in ['suite_setup', 'suite_cleanup']]
    if tcList:
        ## This suite has f10 testcases defined
        ## suite_setup should precede suite_cleanup. Otherwise, both will be set as None.
        if 'suite_setup' in testcaseInfo.tcInfo.keys():
            suite.keywords.create('setup_log', args=['${setupLog}'], type='setup')
        if 'suite_cleanup' in testcaseInfo.tcInfo.keys():
            suite.keywords.create('cleanup_log', args=['${cleanupLog}'], type='teardown')
    else:
        ## This suite has no f10 testcases defined in the script. Entire script should be treated as one testcase
        if 'suite_cleanup' in testcaseInfo.tcInfo.keys():
            suite.keywords.create('cleanup_log', args=['${cleanupLog}'], type='teardown')
        test = suite.tests.create(testcaseInfo.scriptName, tags=None)
        test.keywords.create('testcase_log', args=['${setupLog}', 'result=%s' %testcaseInfo.scriptResult])
        
    for tcid in testcaseInfo.tcInfo.keys():
        if tcid in ['suite_setup', 'suite_cleanup']:
            pass
        else:
            test = suite.tests.create(tcid, tags=None)
            print testcaseInfo
            test.keywords.create('testcase_log', args=['${testcaseInfo}', 'tcid=%s' %tcid])
    return suite


def scriptExecutionMonitor(output):
    global testcaseInfo
    global testcaseInfoList
    global bufferLine
    global yamlCont
    
    if 'bufferLine' not in globals():
        bufferLine = ''

    tempOut = bufferLine + output
    for line in tempOut.split('\n')[0:-1]:
        try:
            scriptStart = re.search(yamlCont["scriptStart"], line)
            if scriptStart:
                scriptName = scriptStart.group(1)
                print
                testcaseInfo = testInfo(scriptName)
                testcaseInfoList.append(testcaseInfo)
        except:
            pass
    
        try:
            scriptCleanup = re.search(yamlCont["scriptCleanup"], line)
            if scriptCleanup:
                testcaseInfo.setTcid('suite_cleanup')
        except:
            pass
                
        try:
            scriptCleanup = re.search(yamlCont["scriptStartup"], line)
            if scriptCleanup:
               testcaseInfo.setTcid('suite_startup')
        except:
            pass
                                                                                                    

        try:
            testcaseStart = re.search(yamlCont["testcaseStart"], line)
            if testcaseStart:
                testcaseInfo.setTcid("%s" %(testcaseStart.group(1)))
        except:
            pass
        try:
           testcaseResult = re.search(yamlCont["testcaseResult"], line)
           if testcaseResult:
               testcaseInfo.setResult(testcaseResult.group(1).upper())
        except:
            pass
        
        try:
            scriptResult = re.search(yamlCont["scriptResult"], line)
            if scriptResult:
                testcaseInfo.setScriptResult(scriptResult.group(1).upper())
        except:
            pass
                                                            
        line = line.strip('\r')
        line = line.replace("\"", "\\\"")
        timestamp = utils.get_timestamp()
     ## only if testcaseInfo is initialized, test logs can be added.
        if 'testcaseInfo' in globals():
            testcaseInfo.appendLog(msg=line, timestamp=timestamp)
    bufferLine = tempOut.split('\n')[-1]
    return output

def executeScript(inputScript, scriptOptionalArgs, inputFile=None):
    global testcaseInfoList
    global testcaseInfo
    global yamlCont
    testcaseInfoList = []
    yamlCont = {}
    if inputFile != None:
        fil = open(inputFile, "r")
        yamlCont = yaml.load(fil)
#        inputFileType = re.search('(.*).yaml', inputFile).group(1)

    inputFileType = 'unknown'
    if inputFile != None:
        inputFileType = re.search('(.*).yaml', inputFile).group(1)
    cmd = "%s %s" %(inputScript, ' '.join(scriptOptionalArgs))
    #inputFileType = 'unknown'
    print "@@@@@@@@@@@@@@@"
    print cmd
    print "@@@@@@@@@@@@@@@"
    ps = winpexpect.winspawn(cmd)
    ps.logfile_read = sys.stdout

    ## Initialize testcaseInfo if the script is not a flist.
    if inputFileType in ['unknown']:
        scriptName = inputScript
        testcaseInfo = testInfo(scriptName)
        testcaseInfoList.append(testcaseInfo)

    timeout = -1
    ps.interact(output_filter=scriptExecutionMonitor)

    if inputFileType is 'unknown':
        ## creates a nested suite
        suiteList = []
        for testcaseInfo in testcaseInfoList:
            testcaseInfo.flush()
            suite = createRobotSuite(testcaseInfo)
            suiteList.append(suite)
        suite = TestSuite(inputScript)
        suite.suites = suiteList
        result = suite.run(output='output.xml', loglevel='debug')
        for testcaseInfo in testcaseInfoList:
            testcaseInfo.variableFile.close()
    else:
        ## creates a single suite
        for testcaseInfo in testcaseInfoList:
            testcaseInfo.flush()
            print testcaseInfo
            suite = createRobotSuite(testcaseInfo)
            result = suite.run(output='output.xml', loglevel='debug')
            testcaseInfo.variableFile.close()

    # Generating log files requires processing the earlier generated output XML.
    ResultWriter('output.xml').write_results()
    pp = postProcess.postProcess(suiteFile=testcaseInfo.scriptName)
    pp.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print 'usage : %s <inputScript> <script optional args>' %sys.argv[0]
        sys.exit()
    if re.search(".yaml", sys.argv[1]):
        inputFile = sys.argv[1]
        inputScript = sys.argv[2]
        scriptOptionalArgs = sys.argv[3:]
        print scriptOptionalArgs
        executeScript(inputScript, scriptOptionalArgs, inputFile)
    else:
        inputScript = sys.argv[1]
        scriptOptionalArgs = sys.argv[2:]
        executeScript(inputScript, scriptOptionalArgs)

