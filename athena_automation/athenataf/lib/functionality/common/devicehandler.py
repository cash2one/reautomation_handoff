import os
from athenataf.config.device_command_map import CommandMap

class DeviceHandler:
    '''
    This class will establish connection to the IAP connected to the Athena Instance under test and will trigger the respective command.
    Gets the device details from the devices.py .
    '''


    def __init__(self, device_name):
        from athenataf.config import devices
        from athenataf.config import fwork
        self.device = None
        self.count = 1
        self.plink_path = os.path.join(fwork.THIRD_PARTY_DIR, "utils", "plink.exe")
        self.tcl_script_path = os.path.join(fwork.THIRD_PARTY_DIR, "utils", "ssh_tcl.tcl")
        self.device = getattr(devices, device_name)


    def handleTelnetConnection(self):
        import telnetlib
        t = telnetlib.Telnet()
        t.open(self.device.ip, self.device.port)
        t.write("\r")
        # t.set_debuglevel(1)
        import time
        current_time  = time.time()
        while 1:
            if abs(int(current_time-time.time())) >25:
                self.count = self.count + 1
                if self.count  == 2:
                    self.count = 1
                    return 0

            output = t.read_eager()
            # print "First time : ",output.split("\n")
            # raw_input("Check first output")
            if len(output)==0:
                output = t.read_eager()
            if output.lower().find("more")!=-1:
                t.write("q\r")
                continue
            elif output.lower().find("nobody")!=-1:
                t.write("\r")
                continue
            elif output.lower().find("user")>1:
                t.write("%s\r"%self.device.username)
                continue
            elif output.lower().find("password:")>1:
                t.write("%s\r"%self.device.password)
                continue
            if output.lower().find("aruba")!=-1:
                if output[len(output)-1] in [">"]:
                    t.write("enable\r")
                    time.sleep(1)
                    t.write("enable\r")
                    continue
                elif output[len(output)-1] in ["#"]:
                    print t.read_eager()
                    break
                else:
                    continue
            # print "Not macthed for any condition"

            # print output
            # raw_input("asd")
        return 1

    def run(self,command):
            '''
            SSH connectivity via PLINK
            OS Check : Os version will be checked and decision is made to choose direct plink or via TCL .
            Param : Command : Command to run .
            type  : String
            '''

            import subprocess
            import platform
            windows_version = platform.platform()
            windows_version = windows_version.split('-')
            if windows_version[0] == 'Windows' and ('2008' in windows_version[1]) or windows_version[0] == "Linux" and self.device.type == "SWITCH":
                print self.device.type
                # This block is for ssh connectivity in windows8

                #proc = subprocess.Popen([self.plink_path, "-ssh", self.device.ip, "-l", self.device.username, "-P", "22", "-pw", self.device.password], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
                #import time
                #time.sleep(10)
                #proc.stdin.write("y\n")
                #proc.stdin.write("\n%s\n" % command)
                #time.sleep(1)
                #stdout, stderr = proc.communicate(input="\n%s\n" % command)
                import MODULES.LinuxModule
                import MODULES.LinuxDevicesModule
                role = type("_IAP", (MODULES.LinuxDevicesModule.LinuxDevice,), {})
                setattr(role, 'username', self.device.username)
                setattr(role, 'password', self.device.password)
                setattr(role, 'serverIp', self.device.ip)
                setattr(role, 'exePath', self.plink_path)
                if self.device.type == "SWITCH":
                    setattr(role, 'prompt', '\) #')
                else:
                    setattr(role, 'prompt', '#')
                proc = role()
                proc.connect()
                #proc.execute("")
                if self.device.type == "SWITCH":
                    proc.receive('\) #')
                else:
                    proc.receive('#')

                proc.transmit(command)
                print "PRINTING COMMAND HERE : %s" %command
                if self.device.type == "SWITCH":
                    stdout = proc.receive('\) #')
                else:
                    stdout = proc.receive('#')

                if stdout != 0:
                    setattr(proc, 'returncode', 1)
                else:
                    setattr(proc, 'returncode', 0)
                #stdout = devObj.output
                stderr = ""
                #devObj.disconnect()
                print "@@@@@@@@@@@@@@@@@@@@@@@INSIDE RUN@@@@@@@@@@@@@@@@@@@@@@@"
                print stdout
                print command
                print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                proc.disconnect()
            else:
                # This block is for all os version except windows8
                i = 2
                if self.device.protocol == "telnet":
                    return_value = self.handleTelnetConnection()
                    if  return_value == 0:
                        self.handleTelnetConnection()
                while i!=0:
                    print "PRINTINF BEFORE TCL SCRIPT"
                    proc = subprocess.Popen(["tclsh", self.tcl_script_path,self.device.ip,self.device.username,self.device.password,command,self.device.protocol,self.device.port],shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = proc.communicate()

                    # print "proc completed"
                    if len(stdout.split("\n"))>40:
                        # print "Got the status proceeding further"
                        break
                    else:
                        # print "Try for one more time"
                        # print stdout
                        i = i -1
            if stdout.lower().find("more")!=-1:
                print "Find the more"
                print len(stdout.split("\n"))
                # raw_input("Check the length")
                stdout.replace("-More-- (q) quit (u) pageup (/) search (n) repeat","")
                stdout.replace("--More-- (q) quit (u) pageup (/) search (n) repeat\r--------------\r\r","")
            print "@@@@@@@@@@@@@@RUN@@@@@@@@@@@@@@@@@@"
            print proc.returncode
            print stdout
            print "#####################################"
            print stderr
            print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

            return proc.returncode, stdout, stderr


    # def run(self,command):
    # 	'''
    # 	SSH connectivity via PLINK
    # 	OS Check : Os version will be checked and decision is made to choose direct plink or via TCL .
    # 	Param : Command : Command to run .
    # 	type  : String
    # 	'''
    #
    # 	import subprocess
    # 	import platform
    # 	windows_version = platform.platform()
    # 	windows_version = windows_version.split('-')
    # 	if windows_version[0] == 'Windows' and ('2008' in windows_version[1]):
    # 		# This block is for ssh connectivity in windows8
    #
    # 		proc = subprocess.Popen([self.plink_path, "-ssh", self.device.ip, "-l", self.device.username, "-P", "22", "-pw", self.device.password], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
    # 		import time
    # 		time.sleep(10)
    # 		proc.stdin.write("\n%s\n" % command)
    # 		stdout, stderr = proc.communicate()
    # 	else:
    # 		# This block is for all os version except windows8
    # 		i = 2
    # 		if self.device.protocol == "telnet":
    # 			return_value = self.handleTelnetConnection()
    # 			if  return_value == 0:
    # 				self.handleTelnetConnection()
    # 		while i!=0:
    # 			proc = subprocess.Popen(["tclsh", self.tcl_script_path,self.device.ip,self.device.username,self.device.password,command,self.device.protocol,self.device.port],shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # 			stdout, stderr = proc.communicate()
    # 			# print "proc completed"
    # 			if len(stdout.split("\n"))>40:
    # 				# print "Got the status proceeding further"
    # 				break
    # 			else:
    # 				# print "Try for one more time"
    # 				# print stdout
    # 				i = i -1
    # 	if stdout.lower().find("more")!=-1:
    # 		print "Find the more"
    # 		print len(stdout.split("\n"))
    # 		# raw_input("Check the length")
    # 		stdout.replace("-More-- (q) quit (u) pageup (/) search (n) repeat","")
    # 		stdout.replace("--More-- (q) quit (u) pageup (/) search (n) repeat\r--------------\r\r","")
    # 	print stdout
    # 	return proc.returncode, stdout, stderr


    def get_running_config(self, extra_command = None):
        '''
        Run "Show running-config" command.
        Search for command in device_command_map .
        If command not present in device version map , pull command line from common map .
        '''
        # command_key = "GET_RUN_CONFIG"
        if not extra_command:
            #command_key = "NO_PAGE"
            command_key = "GET_RUN_CONFIG"
        else:
            print "In to Extra Command loopd"
            command_key = extra_command
        version_specific_map = CommandMap.__dict__[self.device.type]
        common_map = CommandMap.__dict__[self.device.type + "_COMMON"]
        command_line = None
        versions = version_specific_map.keys()
        if versions.count(self.device.version) != 0:
            for version in versions[versions.index(self.device.version):]:
                command_line = version_specific_map[version].get(command_key, None)
                if command_line is not None: break
        if command_line is None:
            command_line = common_map.get(command_key, None)
        if command_key is None:
            raise Exception("Check your command map. Command not available for the mentione device and version.")
        else:
            return self.run(command_line)

    def get_device_status(self):
        '''
        Checks device status by running "show ap debug athena" command .
        '''
        command_key = "GET_DEVICE_STATUS"
        version_specific_map = CommandMap.__dict__[self.device.type]
        common_map = CommandMap.__dict__[self.device.type + "_COMMON"]
        command_line = None
        versions = version_specific_map.keys()
        if versions.count(self.device.version) != 0:
            for version in versions[versions.index(self.device.version):]:
                command_line = version_specific_map[version].get(command_key, None)
                if command_line is not None: break
        if command_line is None:
            command_line = common_map.get(command_key, None)
        if command_key is None:
            raise Exception("Check your command map. Command not available for the mentione device and version.")
        else:
            return self.run(command_line)

    def connect_device_to_server(self):
        '''
        connects the device to the athena server by running "debug-athena-server" command
        '''
        command_key = "PULL_DEVICE_UP"
        version_specific_map = CommandMap.__dict__[self.device.type]
        common_map = CommandMap.__dict__[self.device.type + "_COMMON"]
        command_line = None
        versions = version_specific_map.keys()
        if versions.count(self.device.version) != 0:
            for version in versions[versions.index(self.device.version):]:
                command_line = version_specific_map[version].get(command_key, None)
                if command_line is not None: break
        if command_line is None:
            command_line = common_map.get(command_key, None)
        if command_key is None:
            raise Exception("Check your command map. Command not available for the mentione device and version.")
        else:
            return self.run(command_line + self.device.server)