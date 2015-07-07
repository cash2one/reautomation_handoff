f1 = open(r"C:\Users\ASET\Desktop\file1.txt")
f2 = open(r"C:\Users\ASET\Desktop\file2.txt")
f3 = open(r"C:\Users\ASET\Desktop\modules\ap_automated.csv",'w')
f4 = open(r"C:\Users\ASET\Desktop\modules\ap_not_automated.csv",'w')
l1 = f1.readlines()
l2 = f2.readlines()
# get the common testcases.
final  = list(set(l1)&set(l2))
for i in final: f3.write(i)
f3.close()
# get the testcases which are not automated. 
non_automated = [i for i in list(set(final)^set(l2)) if i!='\n']
for i in non_automated: f4.write(i)
f4.close()
print "The no of testcases automated  		:	%d"%len(final)
print "The no of testcases not automated 	:	%d"%len(non_automated)
