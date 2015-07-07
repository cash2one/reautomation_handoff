'''
Created on 09-Jul-2014

@author: sponnuswamy
'''
import os
from xlwt import Workbook
import xlrd
from config import FRAMEWORK_TESTDATA_PATH


test_data_path = FRAMEWORK_TESTDATA_PATH
book = Workbook()
sheet = book.add_sheet("Sheet 1")
col1_name = 'TestcaseID'
col2_name = 'LastUpdatedDate'
sheet.write(0, 0, col1_name)
sheet.write(0, 1, col2_name)
row_num_write = 0

for file in os.listdir(test_data_path):
    row_dict = {}
    row_num_read = 0
    flag = True
    wb = xlrd.open_workbook(os.path.join(test_data_path, file))
    wb.sheet_names()
    sh = wb.sheet_by_index(0)
    headers = sh.row_values(0)
    while(flag == True):
        try:
            row_num_read += 1
            row_dict = dict(zip(headers, sh.row_values(row_num_read)))
        except IndexError,e:
            flag = False
        else:
            row_num_write += 1
            sheet.write(row_num_write, 1, row_dict['TESTLINK_ID'])
            sheet.write(row_num_write, 2, row_dict['LAST_MODIFIED'])
book.save('Test_ids.xls')