from __future__ import division
import os, types
from athenataf.config import fwork
import logging
logger = logging.getLogger('athenataf')
    # ------------------------------------------------------------------------
    # HTML Template
HTML_PREFIX = r"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Athena TAF Test Report</title>
    <meta name="generator" content="%(generator)s"/>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
<style type="text/css" media="screen">
body        { font-family: verdana, arial, helvetica, sans-serif; font-size: 80%; }
table       { font-size: 100%; }
pre         { }

/* -- heading ---------------------------------------------------------------------- */
h1 {
    font-size: 16pt;
    color: gray;
}
.heading {
    margin-top: 0ex;
    margin-bottom: 1ex;
}

.heading .attribute {
    margin-top: 1ex;
    margin-bottom: 0;
}

.heading .description {
    margin-top: 4ex;
    margin-bottom: 6ex;
}

/* -- css div popup ------------------------------------------------------------------------ */
a.popup_link {
}

a.popup_link:hover {
    color: red;
}

.popup_window {
    display: none;
    position: relative;
    left: 0px;
    top: 0px;
    /*border: solid #627173 1px; */
    padding: 10px;
    background-color: #E6E6D6;
    font-family: "Lucida Console", "Courier New", Courier, monospace;
    text-align: left;
    font-size: 8pt;
    width: 500px;
}

}
/* -- report ------------------------------------------------------------------------ */
#show_detail_line {
    margin-top: 3ex;
    margin-bottom: 1ex;
}
#result_table {
    width: 80%;
    border-collapse: collapse;
    border: 1px solid #777;
}
#header_row {
    font-weight: bold;
    color: white;
    background-color: #777;
}

#header_row_summary {
    font-weight: bold;
    color: white;
    background-color: #777;
}

#result_table td {
    border: 1px solid #777;
    padding: 2px;
}

#highlighted_row {
    border: 1px solid #777;
    background-color: #D7EAFF;
}
#footer_row {
    font-weight: bold;
    background-color: #CCFFCC;
}

#passed_row {
    border: 1px solid #777;
    background-color: #D9F0D1;
}

#failed_row {
    border: 1px solid #777;
    background-color: #f4b3b8;
}

#form-iframe {
}
#form-iframe-report {
}
#total_row  { font-weight: bold; }
.passClass  { background-color: #6c6; }
.failClass  { background-color: #c60; }
.errorClass { background-color: #c00; }
.passCase   { color: #6c6; }
.failCase   { color: #c60; font-weight: bold; }
.errorCase  { color: #c00; font-weight: bold; }
.hiddenRow  { display: none; }
.testcase   { margin-left: 2em; }


/* -- ending ---------------------------------------------------------------------- */
#ending {
}

</style>
</head>
<body>
<script language="javascript" type="text/javascript"><!--
output_list = Array();

/* level - 0:Summary; 1:Failed; 2:All */
function showCase(level) {
    trs = document.getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.substr(0,2) == 'ft') {
            if (level < 1) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.substr(0,2) == 'pt') {
            if (level > 1) {
                tr.className = '';
            }
            else {
                tr.className = 'hiddenRow';
            }
        }
    }
}


function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        tid0 = 't' + cid.substr(1) + '.' + (i+1);
        tid = 'f' + tid0;
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'p' + tid0;
            tr = document.getElementById(tid);
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        if (toHide) {
            document.getElementById('div_'+tid).style.display = 'none'
            document.getElementById(tid).className = 'hiddenRow';
        }
        else {
            document.getElementById(tid).className = '';
        }
    }
}


function showTestDetail(div_id){
    var details_div = document.getElementById(div_id)
    var displayState = details_div.style.display
    // alert(displayState)
    if (displayState != 'block' ) {
        displayState = 'block'
        details_div.style.display = 'block'
    }
    else {
        details_div.style.display = 'none'
    }
}


function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}

/* obsoleted by detail in <div>
function showOutput(id, name) {
    var w = window.open("", //url
                    name,
                    "resizable,scrollbars,status,width=800,height=450");
    d = w.document;
    d.write("<pre>");
    d.write(html_escape(output_list[id]));
    d.write("\n");
    d.write("<a href='javascript:window.close()'>close</a>\n");
    d.write("</pre>\n");
    d.close();
}
*/
--></script>
"""

HTML_SUFFIX = "</table></body></html>"

"""
%(heading)s
%(report)s
%(ending)s

</body>
</html>
"""

class TestReporter:
    '''
    Basic HTML report showing the test result .
    Report will include: Test result, Traceback for errors, Associated test method,Test data used & Execution time per test case.
    '''
    
    def __init__(self, config):
        self.config = config
        self._file = open(os.path.join(config.html_frame_dir, "TestReport.html"), "w")
        self._fileTable = open(os.path.join(config.html_frame_dir, "Table.html"), "w")
        self._fileMain = open(os.path.join(config.html_report_dir, "index.html"), "w")
        self.report_headers = [
                                "S_No",
                                "TESTLINK_ID",
                                "TEST_IDEA",
                                "IMPORT_PATH",
                                "TEST_CLASS",
                                "TEST_METHOD",
                                "TEST_DATA",
                                "RESULT",
                                "DURATION",
                                "EXCEPTION",
                                "TRACE",
                                "SCREENSHOT"
                            ]
                            
        self.result_count = {
                                "PASS" : 0,
                                "FAIL" : 0,
                                "ERROR" : 0
                            }
                            
        self.module_result_count = {}
        self.serial_num = 0
        self.total_duration = 0
                            
    def setUp(self):
        self._file.write('''%s<table id='result_table'><colgroup>
<col align='left' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
</colgroup>''' % (HTML_PREFIX))
        self._fileMain.write(HTML_PREFIX)
        self._fileMain.write("<div class='heading'><h1>Athena TAF Test Report</h1></div>")
        self._fileMain.write("<iframe id='form-iframe' src='./htmlFrames/Table.html' style='margin:10; width:1000px; height:100px; border:none; overflow:auto;' scrolling='no' onload='AdjustIframeHeightOnLoad(id)'></iframe>")
        self._fileMain.write("<script type='text/javascript'>function AdjustIframeHeightOnLoad(id) { document.getElementById(id).style.height = document.getElementById(id).contentWindow.document.body.scrollHeight + 32 + 'px'; }function AdjustIframeHeight(i, id) { document.getElementById(id).style.height = parseInt(i) + 'px'; }</script>")
        f = open(os.path.join(fwork.CONFIG_DIR, "global_vars.props"), "r")
        for line in f.xreadlines():
            if line.startswith('url'):
                line = line.strip()
                field,value = line.split(':', 1)
        f.close()
        self._fileMain.write("<p class='url'><strong>URL: </strong>%s</p>"% value)
        if not self.config.options.ignore_device:
            from athenataf.config import devices
            self.device = None
            if not self.config.options.switch:
                self.device = getattr(devices, 'IAP_1')
            else:
                self.device = getattr(devices, 'Switch_1')
            self._fileMain.write("<p class='device'><strong>Device IP: </strong>%s</p>"% self.device.ip)
        self._fileMain.write("<iframe id='form-iframe-report' src='./htmlFrames/TestReport.html' style='margin:10; width:5500px; height:150px; border:none; overflow:auto;' scrolling='no' onload='AdjustIframeHeightOnLoad(id)'></iframe>")
        header_row = []
        for r_entity in self.report_headers:
            header_row.append(r_entity)
        header_row = "<tr id='header_row'>" + "".join(["<td>%s</td>" % s for s in header_row]) + "</tr>"
        self._file.write(header_row)
        
    def report(self, test_result):
        row_color = None
        logger.debug("Writing report for single test")
        logger.debug(str(test_result))
        import_path_parts = test_result["IMPORT_PATH"].split('.')
        # if len(import_path_parts) <= 4:
            # module = import_path_parts[2]
        # else:
            # module = import_path_parts[3]
        if import_path_parts[2] == 'configuration':
            module = import_path_parts[3]
        else:
            module = import_path_parts[2]
        if not self.module_result_count.has_key(module):
            self.module_result_count[module] = {
                                                    "PASS" : 0,
                                                    "FAIL" : 0,
                                                    "ERROR" : 0
                                                }
        result_row = []
        for r_entity in self.report_headers:
            if r_entity == "S_No":
                self.serial_num += 1
                data = self.serial_num
            elif type(test_result[r_entity]) is types.StringType:
                data = test_result[r_entity].replace("<","&lt;").replace(">","&gt;")
            else:
                data = test_result[r_entity]
            if r_entity == "DURATION":
                self.total_duration += float(test_result[r_entity])
            if r_entity == "RESULT":
                if data.find("ERROR") != -1:
                    self.result_count["ERROR"] += 1
                    self.module_result_count[module]["ERROR"] += 1
                else:
                    self.result_count[data] += 1
                    self.module_result_count[module][data] += 1
                if (data.find("ERROR") != -1) or (data.find("FAIL") != -1):
                    row_color = "red"
                else:
                    row_color = "green"
            if r_entity in ["TRACE", "EXCEPTION"]:
                if (data is None) or (data == ""):
                    data = "NA"
            if r_entity == "SCREENSHOT":
                temp = ""
                for i in range(len(data)):
                    temp += "<a href='../../screenshots/%s' target='_blank'>Screenshot# %d</a>" % (data[i],i+1) + "<br/>"
                data = temp
            result_row.append(data)
        logger.debug("Raw Results row: %s" % str(result_row))
        if row_color == "red":
            result = "<tr id='failed_row'>" + "".join(["<td>%s</td>" % s for s in result_row]) + "</tr>"
        elif row_color == "green":
            result = "<tr id='passed_row'>" + "".join(["<td>%s</td>" % s for s in result_row]) + "</tr>"
        logger.debug("Formatted Results row: %s" % result)        
        logger.debug("Writing to report file")            
        self._file.write(result)
        logger.debug("Flushing contents.")            
        self._file.flush()
        
    def tearDown(self):
        self._fileTable.write(HTML_PREFIX)
        self._file.write("</table>")
        self._file.write("<br><br>")
        self._file.write("<div class='heading'><h1>Test Summary</h1>")
        test_duration = self.total_duration/60
        r_types = ["PASS", "FAIL", "ERROR"]
        for r_type in r_types:
            self._file.write("<p class='attribute'><strong>Total %s</strong> %s</p>" % (r_type.title(), self.result_count[r_type]))
        self._file.write("<p class='attribute'><strong>Test Duration </strong> %.2f mins</p>" % test_duration)
        self._file.write("<br></br>")
        self._fileTable.write("<table id='result_table'>")
        self._fileTable.write("<tr id='header_row_summary'><th>MODULE</th><th>PASS</th><th>FAIL</th><th>ERROR</th><th>TOTAL</th><th>PASS %</th></tr>")
        total = self.result_count["PASS"] + self.result_count["FAIL"] + self.result_count["ERROR"]
        try:
            percentage = (self.result_count["PASS"]*100)/total
        except ZeroDivisionError:
            raise Exception("TestReporter : No test case found for the given command.")
        temp = 0
        for key in self.module_result_count.keys():
            module_total = self.module_result_count[key]["PASS"] + self.module_result_count[key]["FAIL"] + self.module_result_count[key]["ERROR"]
            module_percentage = (self.module_result_count[key]["PASS"]*100)/module_total
            temp += 1
            if (temp % 2) == 0:
                self._fileTable.write("<tr id='highlighted_row'><td>%s</td><td>%d</td><td>%d</td><td>%d</td><td>%d</td><td>%.2f</td></tr>" % (key.replace('_',' '), self.module_result_count[key]["PASS"], self.module_result_count[key]["FAIL"], self.module_result_count[key]["ERROR"], module_total, module_percentage))
            else:
                self._fileTable.write("<tr id='result_table td'><td>%s</td><td>%d</td><td>%d</td><td>%d</td><td>%d</td><td>%.2f</td></tr>" % (key.replace('_',' '), self.module_result_count[key]["PASS"], self.module_result_count[key]["FAIL"], self.module_result_count[key]["ERROR"], module_total, module_percentage))
            module_total = 0
        self._fileTable.write("<tr id='footer_row'><td>SUMMARY</td><td>%d</td><td>%d</td><td>%d</td><td>%d</td><td>%.2f</td></tr>" % (self.result_count["PASS"], self.result_count["FAIL"], self.result_count["ERROR"], total, percentage))
        self._fileTable.write("</table>")
        self._fileTable.write("<script type='text/javascript'>parent.AdjustIframeHeight(document.getElementById('result_table').scrollHeight, 'form-iframe');</script>")
        self._file.write("<div>")
        self._file.write("<script type='text/javascript'>parent.AdjustIframeHeight(document.getElementById('header_row').scrollHeight, 'form-iframe-report');</script>")
        self._fileTable.close()
        self._file.close()
        self._fileMain.close()
#        from emailModule import send_mail_via_com
#        send_mail_via_com("TESTREPORT", "Test Report", "rrkrishnan@arubanetworks.com", os.path.join(self.config.html_frame_dir, "TestReport.html"))