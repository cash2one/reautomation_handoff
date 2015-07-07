__author__ = 'rrkrishnan'
import os
from athenataf.config.device_command_map import CommandMap
import time
from Device_Module.ObjectModule import Device

'''
This class will establish connection to the IAP connected to the Athena Instance under test and will trigger the respective command.
Gets the device details from the devices.py .
'''

def connect_device_to_server(device):
    myDevice = Device.getDeviceObject(device)
    try:
        myDevice.connect_device_to_server()
    except:
        myDevice.disconnect()
        time.sleep(100)
        myDevice.connect()
        myDevice.connect_device_to_server()
    i = 1
    while i < 4:
        if myDevice.get_device_status():
            break
        else:
            time.sleep(10)
        i = i + 1
    if not myDevice.get_device_status():
        raise AssertionError("Device is not attached to Athena Yet")

def disconnect_device_from_server(device):
    myDevice = Device.getDeviceObject(device)
    try:
        myDevice.connect_device_to_server("1.1.1.1")
    except:
        myDevice.disconnect()
        time.sleep(100)
        myDevice.connect()
        myDevice.connect_device_to_server("1.1.1.1")
    time.sleep(10)
    i = 1
    while i < 10:
        if not myDevice.get_device_status():
            break
        else:
            time.sleep(5)
        i = i + 1
    if myDevice.get_device_status():
        raise AssertionError("Device is attached to Athena Yet")


def disconnect_client_from_ap(device):
    myDevice = Device.getDeviceObject(device)
    try:
        myDevice.disconnect_client_from_ap()
    except:
        myDevice.connect()
        myDevice.disconnect_client_from_ap()


def connect_client_to_ap(device, SSID=None):
    myDevice = Device.getDeviceObject(device)
    try:
        myDevice.connect_client_to_ap(SSID=SSID)
    except:
        myDevice.connect()
        time.sleep(5)
        myDevice.connect_client_to_ap(SSID=SSID)

def write_erase_all(device):
    myDevice = Device.getDeviceObject(device)
    myDevice.receive("#")
    myDevice.transmit("write erase all")
    myDevice.receive("\(y\/n\):")
    myDevice.transmit("y")
    output = myDevice.receive("#")

def reload(device):
    myDevice = Device.getDeviceObject(device)
    myDevice.receive("#")
    myDevice.transmit("reload")
    time.sleep(300)
    reconnect(device)

def reconnect(device):
    myDevice = Device.getDeviceObject(device)
    myDevice.reconnect()
    myDevice.setUsername("admin")
    myDevice.setPassword("test123")
    for i in range(0, 10):
        myDevice.transmit("show version")
        if "User" in myDevice.receive("User:"):
            break
        else:
            time.sleep(50)
    myDevice.getPrompt()

def getPrompt(device):
    myDevice = Device.getDeviceObject(device)
    try:
        myDevice.getPrompt()
    except:
        myDevice.transmit("\r")
        myDevice.getPrompt()
        
def factoryReset(device):
    '''
    Factory reset the IAP 
    '''
    if "IAP" in device :
        myDevice = Device.getDeviceObject(device)
        myDevice.receive("#")
        write_erase_all(device)
        myDevice.transmit("reload")
        myDevice.receive("Hit <Enter> to stop autoboot:  2")
        myDevice.transmit("\n")
        time.sleep(30)
        myDevice.transmit("factory_reset")
        time.sleep(30)
        myDevice.receive("apboot>")
        time.sleep(15)
        myDevice.transmit("setenv ipaddr %s" %myDevice.get("ip"))
        time.sleep(8)
        myDevice.receive("apboot>")
        myDevice.transmit("setenv netmask %s"%myDevice.get("netmask"))
        time.sleep(8)
        myDevice.receive("apboot>")
        myDevice.transmit("setenv gatewayip %s"%myDevice.get("gatewayip"))
        time.sleep(8)
        myDevice.receive("apboot>")
        myDevice.transmit("setenv standalone_mode 1") 
        time.sleep(8)
        myDevice.receive("apboot>")
        myDevice.transmit("setenv dnsip 8.8.8.8") # Hard coding dns , since dnsip will be same for all the devices 
        time.sleep(8)
        myDevice.receive("apboot>")
        myDevice.transmit("saveenv")
        time.sleep(8)
        myDevice.receive("apboot>")
        myDevice.transmit("print")
        time.sleep(8)
        myDevice.receive("apboot>")
        myDevice.transmit("boot")
        time.sleep(2)
        myDevice.receive("        <<<<<       Welcome to the Access Point     >>>>>")
        time.sleep(50)
        myDevice.receive("i am master now")
        myDevice.receive(" !!! Init ---> Master")
        myDevice.receive("ethernet_device_event: dev eth1 is up")
        myDevice.transmit("\n")
        myDevice.receive("User:")
        myDevice.transmit("admin")
        myDevice.receive("Password:")
        myDevice.transmit("admin")
        myDevice.receive("#")
        myDevice.transmit("show ap-env")
    else:
        myDevice = Device.getDeviceObject(device)
        myDevice.receive("\) #")
        myDevice.transmit("write erase all")
        myDevice.receive("to proceed :")
        myDevice.transmit("y")
        myDevice.transmit("restore factory_default stacking")
        myDevice.receive("\[y\/n\]:")
        myDevice.transmit("y")
        time.sleep(100)
        myDevice.receive("Loading factory initial configuration.")
        myDevice.receive("Starting Console Session")
        myDevice.receive("Retrieving Configuration ...")
        time.sleep(100)
        myDevice.receive("User:")
        myDevice.transmit("admin")
        time.sleep(8)
        myDevice.receive("assword:")
        myDevice.transmit("admin123")
        time.sleep(8)
        myDevice.receive("\) >")
        myDevice.transmit("enable")
        myDevice.receive("assword:")
        myDevice.transmit("enable")     
        myDevice.receive("\(y\|n\)\?")
        myDevice.transmit("n")
        time.sleep(8)
        myDevice.receive("\) #")
        myDevice.transmit("show ip interface brief")
        time.sleep(8)
        myDevice.receive("\) #")
        myDevice.transmit("configure t")
        myDevice.receive("\) #")
        time.sleep(8)
        myDevice.transmit("interface vlan 1")
        myDevice.receive("\) #")
        time.sleep(8)
        myDevice.transmit("no ip address")
        myDevice.receive("\) #")
        time.sleep(8)
        myDevice.transmit("ip address dhcp-client")
        myDevice.receive("\) #")
        time.sleep(8)       
        myDevice.transmit("ip-profile")
        myDevice.receive("\) #")
        time.sleep(8)
        myDevice.transmit("default-gateway import dhcp")
        myDevice.receive("\) #")
        time.sleep(8)
        myDevice.transmit("end")
        myDevice.receive("\) #")
        time.sleep(8)
        myDevice.transmit("show ip interface brief")
        myDevice.receive("\) #")
        time.sleep(8)
        
# def reload_connect_to_switch(self, serverIp=None):
    # import pdb
    # pdb.set_trace()
    # myDevice = Device.getDeviceObject("Switch_1")
    # myDevice.receive("\) #")
    # myDevice.transmit("\r")
    # myDevice.transmit("\r")
    # myDevice.transmit("\r")
    # myDevice.transmit("\r")
    # time.sleep(8)
    # myDevice.transmit("support")
    # time.sleep(8)
    # myDevice.receive("Password:")
    # time.sleep(4)
    # myDevice.transmit("Ph03n1X")
    # time.sleep(8)
    # myDevice.receive("\) #")    
    # time.sleep(8)
    # myDevice.transmit("debug aruba-central connection ip 1.1.1.1")
    # time.sleep(8)
    # myDevice.receive("\) #")    

# def create_dhcp_pool(device):
    # myDevice = Device.getDeviceObject("device")
        myDevice.receive("\) #")
        myDevice.transmit("\r")
        myDevice.transmit("\r")
        myDevice.transmit("configure terminal")
        myDevice.receive("\) #")
        time.sleep(8)
        myDevice.transmit("ip dhcp pool PRETEST")
        myDevice.receive("\) #")
        time.sleep(8)
        myDevice.transmit("network 3.3.3.3 255.255.0.0")
        myDevice.receive("\) #")
        time.sleep(8)
        myDevice.transmit("end")
        myDevice.receive("\) #")
        time.sleep(8)
        myDevice.transmit("show ip dhcp database")
        myDevice.receive("\) #")
        time.sleep(8)
        
def assert_backend(device,command=None,expected=None):
    '''
    Device : IAP or switch to used for backend validation.
    command : cli command
    expected : expected result in cli o/partition
    '''
    myDevice = Device.getDeviceObject(device)
    if "IAP" in device:
        myDevice.receive("#")
        myDevice.transmit("%s"%command)
        output = myDevice.receive("#")
        if not expected in output:
            raise AssertionError("%s not found in config." %expected)
    else:
        myDevice.receive("\) #")
        myDevice.transmit("%s"%command)
        output = myDevice.receive("\) #")
        if not expected in output:
            raise AssertionError("%s not found in config." %expected)

def configure_deny_inter_user_bridging_and_deny_local_routing(ap):
    import time
    myDevice = Device.getDeviceObject(ap)
    myDevice.receive("#")
    myDevice.transmit("show ap debug cloud-server")
    myDevice.transmit("configure terminal")
    # myDevice.receive("(config) #")
    time.sleep(8)
    myDevice.receive("#")
    myDevice.transmit("wlan ssid-profile em1")
    time.sleep(8)
    myDevice.receive("#")
    myDevice.transmit("deny-inter-user-bridging")
    time.sleep(8)
    myDevice.receive("#")
    myDevice.transmit("deny-local-routing")
    time.sleep(8)
    myDevice.receive("#")
    myDevice.transmit("end")
    time.sleep(8)
    myDevice.receive("#")
    myDevice.transmit("commit apply")
    time.sleep(8)
    myDevice.receive("#")
    myDevice.transmit("sh ru | inc deny")
    time.sleep(8)
    myDevice.receive("#")
    
    # myDevice.connect_device_to_server()
	
	
def configureWirelessNetwork(device):
	'''
	Configures a wireless Network 
	'''
	myDevice = Device.getDeviceObject(device)
	myDevice.receive("#")
	myDevice.transmit("config t")
	time.sleep(8)
	myDevice.receive("#")
	myDevice.transmit("wlan ssid-profile test2") 
	time.sleep(8)
	myDevice.receive("#")
	myDevice.transmit("enable")
	time.sleep(8)
	myDevice.receive("#")
	myDevice.transmit("index 1")
	time.sleep(8)
	myDevice.receive("#")
	myDevice.transmit("type employee") 
	time.sleep(8)
	myDevice.receive("#")
	myDevice.transmit("essid test2")
	time.sleep(8)
	myDevice.receive("#")
	myDevice.transmit("wpa-passphrase b61c83b4823d792cc8ce229d23c8c07c2a9eaa92208e5f2d")
	time.sleep(8)
	myDevice.receive("#")
	myDevice.transmit("opmode wpa2-psk-aes")
	time.sleep(8)
	myDevice.receive("#")
	myDevice.transmit("auth-server InternalServer") 
	time.sleep(8)
	myDevice.receive("#")
	myDevice.transmit("set-role AP-Group contains test default_wired_port_profile")
	time.sleep(8)
	myDevice.receive("#")
	myDevice.transmit("rf-band all")
	time.sleep(8)
	myDevice.receive("#")
	myDevice.transmit("captive-portal disable") 
	time.sleep(8)
	myDevice.receive("#")
	myDevice.transmit("dtim-period 1")
	time.sleep(8)
	myDevice.receive("#")
	myDevice.transmit("inactivity-timeout 1000")
	time.sleep(8)
	myDevice.receive("#")
	myDevice.transmit("broadcast-filter none") 
	time.sleep(8)
	myDevice.receive("#")
	myDevice.transmit("dmo-channel-utilization-threshold 90")
	time.sleep(8)
	myDevice.receive("#")
	myDevice.transmit("local-probe-req-thresh 0")
	time.sleep(8)
	myDevice.receive("#")
	myDevice.transmit("max-clients-threshold 64")
	time.sleep(8)
	myDevice.receive("#")
	myDevice.transmit("end")
	time.sleep(8)
	myDevice.receive("#")
	myDevice.transmit("commit apply")
	time.sleep(8)
	myDevice.receive("#")
	
	myDevice.connect_device_to_server()
        