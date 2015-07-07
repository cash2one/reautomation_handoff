import xlwt
#path of file containing all testid's
file = open(r"C:\Users\ASET\Desktop\failed_test_cases.txt")
file_contents  = file.readlines()
file_contents = [i for i in file_contents if i!='\n']
print "The total no of test cases",len(file_contents)
#No of xls files to be generated.
files = 3
div_count = int(len(file_contents)/files)
print "the test distribution count",div_count
import os
os.chdir(r"C:\Users\ASET\Desktop\resulted_excel_files")
for i in range(0,files):
	workbook = xlwt.Workbook()
	file1 = workbook.add_sheet("test")
	file1.write(0,0,"TESTLINK_ID")
	file1.write(0,1,"TEST_IDEA")
	file1.write(0,2,"LAST_MODIFIED")
	row = 1
	k=0 
	if i+1==files:
		for j in file_contents[div_count*i:]:
			file1.write(row,k,j.replace("\n",""))
			row = row + 1
	elif i>0:
		for j in file_contents[div_count*i:(div_count*i)+div_count]:
			file1.write(row,k,j.replace("\n",""))
			row = row + 1
			
	elif i==0:
		for j in file_contents[i+div_count*i:div_count]:
			file1.write(row,k,j.replace("\n",""))
			row = row + 1
	workbook.save(r"wireless_%s.xls"%str(i+1))