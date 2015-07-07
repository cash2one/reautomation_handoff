'''
Created on 03-Jul-2014

@author: Shrividhya
@description:
- Connects to Testlink MySQL DB & fetches all test case id's & Last modified date for automated cases 
- Parses the testdata folder in automation framework and fetches all the testcase id's from the automatiom framework
- Compares the Testlink data & automation data
- Sends an email notification if there are any difference

@prerequisite: 
Install https://pypi.python.org/pypi/google-appengine
Install MySQLdb, xlrd, pyExcelerator
'''
from pyExcelerator import Workbook
import sys
import MySQLdb
import xlrd
from config import TESTLINK_HOST_NAME,TESTLINK_USER_NAME,TESTLINK_PWD,TESTLINK_DB_NAME,SELECT_QUERY,TESTLINK_XLS_PATH,TESTLINK_XLS_NAME,FRAMEWORK_XLS_NAME
global testlink_dict,automated_dict,testlink_xls_path,automated_xls_path
import smtplib

def fetch_data_from_db_write_into_xls():
    #Connect to Testlink DB and fetch all automated cases
    conn = MySQLdb.connect(host=TESTLINK_HOST_NAME,user=TESTLINK_USER_NAME,passwd=TESTLINK_PWD,db=TESTLINK_DB_NAME) 
    cu_select=conn.cursor(MySQLdb.cursors.DictCursor)
    testlink_xls_path = TESTLINK_XLS_PATH;
    try:
        cu_select.execute(SELECT_QUERY)
    except MySQLdb.Error:
        errInsertSql = "Insert Sql ERROR!! sql is==>%s" %(SELECT_QUERY)
        sys.exit(errInsertSql)
    
    testlink_dict = cu_select.fetchall()
    #Create an excel from the fetched data
    wb = Workbook()
    ws0 = wb.add_sheet('0')
    row_number=1
    for row in testlink_dict:
        i=0
        for item in row:
    
            
            val=str(row[item])
            if i==0:
                val="ATH-"+val
            
            if row_number==1:
                ws0.write(0,i,'')
                ws0.write(0,i,item)
                ws0.write(row_number,i,val)
                i=i+1
            else:
                ws0.write(row_number,i,val)
                i=i+1
        row_number=row_number+1
            
    #Save the file 
    wb.save('%s.xls'%testlink_xls_path)

def send_email(strMailContent):
    import smtplib
    import base64
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText

    with open("strMailContent.txt","w") as outfile:
        outfile.write(strMailContent)

    recipient = "sponnuswamy@arubanetworks.com"
    msg = MIMEMultipart()
    msg['Subject'] = "Testlink Polling Script Output"
    msg['From'] = 'sponnuswamy@arubanetworks.com'
    msg['To'] = recipient

    filename = "strMailContent.txt"
    f = file(filename)
    attachment = MIMEText(f.read())
    attachment.add_header('Content-Disposition', 'attachment', filename=filename)           
    msg.attach(attachment)

    try:
        smtpObj = smtplib.SMTP('mail.arubanetworks.com')
        smtpObj.sendmail(msg['From'], msg['To'], msg.as_string())
        print "Successfully sent email"
    except SMTPException:
        print "Error: unable to send email"
    finally:
        smtpObj.quit()

def get_dict_from_xls(filename):
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_index(0)
    row_dict = {}
    for row_index in range(sheet.nrows):
        if row_index != 0:
            row_dict[sheet.cell(row_index, 0).value] = sheet.cell(row_index, 1).value
    return row_dict

def get_set_testids(setname):
    strtestids = ""
    for item in setname:
        if item!="":
            strtestids = strtestids + item + "\n"
    if strtestids=="":
        strtestids = "None"
    return strtestids
 
def compare_dicts_and_frame_notification_mail_content(a,b):
    keya=set(a.keys())
    keyb=set(b.keys())
    a_xclusive = keya - keyb
    b_xclusive = keyb - keya
    _common = keya & keyb
    common_eq = set(k for k in _common if a[k] == b[k])
    common_neq = _common - common_eq
    modifiedTestCases_in_Testlink= get_set_testids(common_neq)
    newTestCases_in_Testlink = get_set_testids(a_xclusive)
    newTestCases_in_Framework = get_set_testids(b_xclusive)
    strMailContent= "\nMODIFIED IN TESTLINK:\n" + modifiedTestCases_in_Testlink + "\n"
    strMailContent= strMailContent + "\nAUTOMATED BUT NOT IN TESTLINK: \n" + newTestCases_in_Framework + "\n"
    strMailContent= strMailContent + "IN TESTLINK BUT NOT AUTOMATED \n" + newTestCases_in_Testlink + "\n"
    print strMailContent
    return strMailContent
        
if __name__ == '__main__':
    #Get data from testlink db and write into xls
    fetch_data_from_db_write_into_xls()
    
    #Compare the testlink & automation framework data
    testlink_data_dict = get_dict_from_xls(TESTLINK_XLS_NAME)
    automation_data_dict = get_dict_from_xls(FRAMEWORK_XLS_NAME)
    strMailContent = compare_dicts_and_frame_notification_mail_content(testlink_data_dict, automation_data_dict)

    #Send notification mail to Automation DL
    send_email(strMailContent)