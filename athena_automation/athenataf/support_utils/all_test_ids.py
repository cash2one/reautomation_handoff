import os

test_class_dict = {}
# path = "G:\\athena_tm\\athena\\athena\\automation\\athena_automation\\athenataf\\tests"
# path = "G:\\athena_tm\\athena\\athena\\automation\\athena_automation\\athenataf\\tests\\configuration\wireless_network"
# path = "G:\\athena_tm\\athena\\athena\\automation\\athena_automation\\athenataf\\tests\\configuration\wireless_network"
# path = "G:\\athena_tm\\athena\\athena\\automation\\athena_automation\\athenataf\\tests\\configuration\wired_network"
# path = "G:\\athena_tm\\athena\\athena\\automation\\athena_automation\\athenataf\\tests\\configuration\wids"
# path = "G:\\athena_tm\\athena\\athena\\automation\\athena_automation\\athenataf\\tests\\configuration\\vpn"
# path = "G:\\athena_tm\\athena\\athena\\automation\\athena_automation\\athenataf\\tests\\configuration\\system"
# path = "G:\\athena_tm\\athena\\athena\\automation\\athena_automation\\athenataf\\tests\\configuration\\services"
# path = "G:\\athena_tm\\athena\\athena\\automation\\athena_automation\\athenataf\\tests\\configuration\\security"
# path = "G:\\athena_tm\\athena\\athena\\automation\\athena_automation\\athenataf\\tests\\configuration\\rf"
# path = "G:\\athena_tm\\athena\\athena\\automation\\athena_automation\\athenataf\\tests\\configuration\\dhcp"
# path = "G:\\athena_tm\\athena\\athena\\automation\\athena_automation\\athenataf\\tests\\configuration\\access_points"
# path = "G:\\athena_tm\\athena\athena\\automation\\athena_automation\\athenataf\\tests\\sanity_test_suite"
path = "G:\\athena_tm\\athena\\athena\\automation\\athena_automation\\athenataf\\tests\\maintenance"


count = 0
for root, dirs, files in os.walk(path):
	for test_class in files:
		if test_class.endswith(".py") and not test_class.startswith("_"):
			test_case_list = []
			test_class_file_object = open(os.path.join(root,test_class), 'r')
			for line in test_class_file_object.xreadlines():
				line = line.strip()
				if line.startswith("def test_ath_"):
					line_parts = line.split('_')
					count = count + 1
					print ('ATH-' + line_parts[2])
			test_class_file_object.close()
print "Tot : %s"%count