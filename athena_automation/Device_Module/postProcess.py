from time import gmtime, strftime
import os
import shutil
#import emailModule
from robot.result import ExecutionResult
import socket
import getpass
import datetime
from robot.libraries.BuiltIn import BuiltIn
import spur
import scp
import paramiko

gmt = gmtime()
dts = strftime("%d_%b_%Y_%H_%M_%S", gmt)
dfolder = strftime("%d_%m_%y", gmt)
class postProcess(object):
    ROBOT_LISTENER_API_VERSION = 2
    def __init__(self, logDir='D:\\', suiteFile='suite.txt', reportFile='report.html', logFile='log.html', outputFile = 'output.xml'):
        self.logDir = logDir
        self.sFile = str(os.path.basename(suiteFile))
        self.rFile = reportFile
        self.lFile = logFile
        self.oFile = outputFile
        self.sPath = str(os.path.dirname(os.path.abspath(suiteFile)))

    def start_suite(self, suite, attr):
        self.sFile = str(os.path.basename(BuiltIn().get_variable_value("${SUITE_SOURCE}")))
        self.rFile = str(BuiltIn().get_variable_value('${REPORT_FILE}'))
        self.lFile = str(BuiltIn().get_variable_value('${LOG_FILE}'))
        self.oFile = str(BuiltIn().get_variable_value('${OUTPUT_FILE}'))
        self.sPath = str(os.path.dirname(os.path.abspath(BuiltIn().get_variable_value("${SUITE_SOURCE}"))))

    def close(self):

        self.passCount = 0
        self.failCount = 0
        #logDir = self.logDir + dfolder
        logDir = self.sPath + '\\LOG\\' + dfolder
        logDir += '\\' + os.path.splitext(self.sFile)[0] + '_' + dts
        try:
            os.makedirs(logDir)
        except OSError:
            if not os.path.isdir(logDir):
                raise

        #shell = spur.SshShell(hostname=server, username=username, password = password)
        #result = shell.run(['mkdir', '-p', logDir])
        newReportFile = logDir + '\\' + os.path.basename(self.rFile)
        newLogFile = logDir + '\\' + os.path.basename(self.lFile)
        #logLink += '/' + os.path.basename(self.lFile)
        logLink = newLogFile
        newOutputFile = logDir + '\\' + os.path.basename(self.oFile)
        #client = paramiko.SSHClient()
        #client.load_system_host_keys()
        #client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #client.connect(server, username=username, password=password)
        #scpClient = scp.SCPClient(client.get_transport())
        #files = [self.rFile, self.lFile, self.oFile]
        #scpClient.put(files, logDir)
        for sourceFile in [self.rFile, self.lFile, self.oFile]:
            shutil.copy(sourceFile, logDir)
        result = ExecutionResult(self.oFile)
        server = socket.gethostname()
        user = getpass.getuser()
        suiteName = result.suite
        testSuiteList = result.suite.suites
        testCount = result.suite.test_count
        suiteStartTime = datetime.datetime.strptime(result.suite.starttime.partition('.')[0], '%Y%m%d %H:%M:%S')
        suiteEndTime = datetime.datetime.strptime(result.suite.endtime.partition('.')[0], '%Y%m%d %H:%M:%S')
        suiteTimeElapsed = datetime.timedelta(milliseconds=result.suite.elapsedtime)
        testInfoTable = self._createTestReport(result.suite, logLink)
        subject = "%s executed. Total testcase - %s; Pass : %s; Fail %s;" %(suiteName, testCount, self.passCount, self.failCount)
        report = "Content-Type: text/html\n"
        report += "MIME-Version: 1.0\n"
        report += "<html>\n"
        report += """<style>\n
                         table {
                            align: left;
                            clear: left;
                            margin-bottom: 30px;
                         }
                         table,th,td {
                            border:1px solid black;
                            border-collapse:collapse;
                        }
                        th,td {padding:5px;}
                        th {text-align:left;}
                        td {font-family: courier; font-size: 10pt;}
                     </style>"""
        report += "<body>\n"
        report += "<pre>\n"
        report += "<font face=courier size=3>\n"
        report += "<b>\t\t<u>Summary result\n\n</u></b>"
        report += "Suite name           : %s\n" %(suiteName)
        report += "Execution server     : %s\n" %(server)
        report += "Username             : %s\n" %(user)
        report += "Suite start time     : %s\n" %(suiteStartTime)
        report += "Suite end time       : %s\n" %(suiteEndTime)
        report += "Suite run time       : %s\n" %(suiteTimeElapsed)
        report += "Total TCs executed   : %s\n" %(testCount)
        report += "Total TCs passed     : %s\n" %(self.passCount)
        report += "Total TCs failed     : %s\n" %(self.failCount)
        report += "\n"
        report += "Log                  : <a href=\"%s\"> %s </a>\n" %(logLink, newLogFile)
        report += "\n"
        report += testInfoTable
        report += "\n"
        report += "</font></pre></body></html>\n"
        #emailModule.sendmail2(subject=subject, body=report)
    def _createTestReport(self, testSuite, logLink, suiteIndex=1):
        report = ""
        testList = testSuite.tests
        if testList:
            report += "<table border=\"1\" style=\"width:300px\" align=\"left\" clear=\"left\" margin-bottom=\"30px\">\n"
            report += "<tr><th bgcolor=\"ooffff\">%s</th></tr>\n" %testSuite
            report += "<tr><th bgcolor=\"00ffff\">Testcase</th><th bgcolor=\"00ffff\">Description</th><th bgcolor=\"00ffff\">Result</th>\n"
    
        testIndex = 0
        for test in testList:
            testIndex += 1
            report += "<tr><td><a href = \"%s#s%s-t%s\">%s</a></td><td>%s</td><td>%s</td></tr>\n"%(logLink, suiteIndex, testIndex, test, test.doc, test.status)
            if test.status in 'PASS':
                self.passCount += 1
            else:
                self.failCount += 1

        report += "</table>"
        testSuiteList = testSuite.suites
        if testSuiteList:
            index = 0
            for testSuite in testSuiteList:
                index += 1
                report += self._createTestReport(testSuite, logLink, index)
        return report
