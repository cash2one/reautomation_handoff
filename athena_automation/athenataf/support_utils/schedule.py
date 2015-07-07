import optparse
f = open("C:\Users\ASET\Desktop\scheduler.bat",'w')
usage = """Usage: %prog [options]"""
parser = optparse.OptionParser(usage=usage)	
# parser.add_option('-m', "--modules", dest='modules',
			  # default=[],
			  # help='Enter the modules')
parser.add_option('-m',  "--modules", dest='modules',action='store_true',
			  default=False,
			  help='Takes the Modules')
parser.add_option('-b', "--browser", dest='browser',
			  default="firefox",
			  help='browser type by default firefox')		
parser.add_option('-i', "--ignore", dest='ignore',action='store_true',
			  default=False,
			  help='ignore device -default (OFF)')	
cmd, args = parser.parse_args()
f.write(r"cd C:\aruba\athena\athena\automation\athena_automation")
f.write("\n")
lis=[]
if cmd.modules:
	import os 
	lis = os.listdir(r"C:\Users\ASET\Desktop\execution_module")
	lis = [i.split(".")[0] for  i in lis ]
for i in lis:
	f.write("python run.py -i %s %s %s\n"%(i,"-b "+cmd.browser if cmd.browser!="firefox" else "-b firefox","--ignore_device" if cmd.ignore else ""))
f.close()