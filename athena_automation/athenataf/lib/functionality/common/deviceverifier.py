import os
import re
import time
from athenataf.config import fwork
#from athenataf.lib.functionality.common.devicehandler import DeviceHandler
from Device_Module import ObjectModule as Device
from athenataf.lib.util.textdiffer import TextDiffer
from athenataf.config import devices
import logging
logger = logging.getLogger('athenataf')
import os

class DeviceVerifier:
    def __init__(self, config, test, device=os.environ['device']):
        self.config = config
        try:
            self.get_config = Device.Device.getDeviceObject(os.environ['device'])
        except Exception as err:
            print err
            raise
            pass
        self.differ = TextDiffer()
        self.test = test
        self.s1 = {}
        self.s2 = {}
        self.s3 = {}
        self.device_results_test_dir = None

    def _log_snapshot(self, name, snapshot):
        self.device_results_test_dir = os.path.join(self.config.device_verification_dir, self.test.current_test_id)
        if not os.path.isdir(self.device_results_test_dir): os.makedirs(self.device_results_test_dir)
        if os.environ['device'] != 'IAP_1' and os.environ['device'] != 'Switch_1':
            f = open(os.path.join(self.device_results_test_dir, "%s_%s.txt" % (name, os.environ['device'])), "w")
        else:
            f = open(os.path.join(self.device_results_test_dir, "%s.txt" % name), "w")
        f.write(snapshot)
        f.close()
        
    def _take_snapshot(self, type, extra_command = None):
        #config = self.get_config.get_running_config(extra_command)
        config = Device.Device.getDeviceObject(os.environ['device']).get_running_config(extra_command)
        config_string = config
        lines = config_string.split('\n')
        pseudo_snapshot = []
        for line in lines:
            if not(line.startswith(" index ") or line.startswith(" wpa-passphrase") or line.startswith("version ") or line.lower().find("more")!=-1):
                words = line.split(" ")
                for word in words:
                    result1 = re.match("[^-_:]{32}", word)
                    if not result1 == None:
                        line = line.replace(word, "")
                    result2 = re.match("(([A-Z][0-9]|[A-Z][A-Z]|[0-9][A-Z]|[0-9][0-9]):){2,6}", word, re.I)
                    if not result2 == None:
                        line = line.replace(word, "")
                if (line.startswith("name ") and ('Instant-' in line)):
                    name_parts = line.split('-')
                    name_parts[1] = ""
                    line = "".join(name_parts)
                pseudo_snapshot.append(line)
        snapshot = '\n'.join(pseudo_snapshot)
        self._log_snapshot(type, snapshot)
        return snapshot
        
    def take_s1_snapshot(self, extra_command = None):
        if not self.config.options.ignore_device:
            self.clear(os.environ['device'])
            if not self.config.options.switch:
                time.sleep(devices.CONFIG_CHANGE_WAIT_TIME)
            # setattr(self, "s1_%s" %os.environ["device"], self._take_snapshot("s1",  extra_command))
            self.s1[os.environ['device']] = self._take_snapshot("s1", extra_command)
            # self.s1 = self._take_snapshot("s1",  extra_command)
        
    def take_s2_snapshot(self, extra_command = None):
        if not self.config.options.ignore_device:
            if not  self.config.options.switch:
                time.sleep(devices.CONFIG_CHANGE_WAIT_TIME)
            # setattr(self, "s2_%s" %os.environ["device"], self._take_snapshot("s2",  extra_command))
            self.s2[os.environ['device']] = self._take_snapshot("s2", extra_command)
            # self.s2 = self._take_snapshot("s2",  extra_command)
        
    def take_s3_snapshot(self, extra_command = None):
        if not self.config.options.ignore_device:
            if not  self.config.options.switch:        
                time.sleep(devices.CONFIG_CHANGE_WAIT_TIME)    
            # setattr(self, "s3_%s" %os.environ["device"], self._take_snapshot("s3",  extra_command))
            self.s3[os.environ['device']] = self._take_snapshot("s3", extra_command)
            # self.s3 = self._take_snapshot("s3",  extra_command)
        
    def _get_test_diff(self, num_of_context_lines):
        expected_config_diff = None
        import os
        print os.environ['device']
        device = os.environ['device']
        # raw_input('device')
        version = None
        exec("version = devices.%s.version"%device)
        print version
        # raw_input('version')
        if self.config.options.switch:
            diff_file_path = os.path.join(fwork.DEVICE_VERIFICATION_DIR+"\%s"%self.get_config.get('type') , "%s_s1_s2_diff.txt") % self.test.current_test_id
        else:
            diff_file_path = os.path.join(fwork.DEVICE_VERIFICATION_DIR+"\%s"%self.get_config.get('type') +"\%s"%version, "%s_s1_s2_diff.txt") % self.test.current_test_id
        print diff_file_path
        # raw_input('path')
        if os.path.isfile(diff_file_path):
            diff_handle = open(diff_file_path, "r")
            expected_config_diff_list = diff_handle.readlines()
            expected_config_diff = ''.join(expected_config_diff_list)
            diff_handle.close()
        else:
            # To be used during script development only
            try:
                left_file = os.path.join(fwork.DEVICE_VERIFICATION_DIR, "%s_base.txt") % self.test.current_test_id
                right_file = os.path.join(fwork.DEVICE_VERIFICATION_DIR, "%s_final.txt") % self.test.current_test_id
                if os.path.isfile(left_file) and os.path.isfile(right_file): 
                    expected_config_diff = self.differ.get_difference(left_file, right_file, num_of_context_lines)
                else:
                    raise Exception("'%s_s1_s2_diff.txt' file not found in dir '%s'" % (self.test.current_test_id, fwork.DEVICE_VERIFICATION_DIR))
            except Exception as e:
                logger.debug("deviceverifier: caught exception:: %s" % str(e))
                raise
        expected_config_diff = expected_config_diff % self.test.get_all_config_dict()
        f = open(os.path.join(self.device_results_test_dir, "s1_s2_expected_diff.txt"), "w")
        f.write(expected_config_diff)
        f.close()        
        return expected_config_diff

    def _check_diff_equality(self, left_diff, right_diff):
        if self.differ.get_difference(left_diff, right_diff, 0) != "":
            return False
        else:
            return True
        #return left_diff == right_diff
    
    def _get_snapshot_diff(self, type, left_snapshot, right_snapshot, num_of_context_lines):
        import os
        actual_config_diff = self.differ.get_difference(left_snapshot, right_snapshot, num_of_context_lines)
        print "The device used for Snapshot"
        print os.environ['device']
        f = open(os.path.join(self.device_results_test_dir, "%s_%s_actual_diff.txt" % (type,os.environ['device'])), "w")
        f.write(actual_config_diff)
        f.close()        
        return actual_config_diff
        
    def check_s1_s2_diff(self , num_of_context_lines):
        if not self.config.options.ignore_device:
            print "The snapshot key is:", os.environ['device']
            print self.s1[os.environ['device']]
            print self.s1[os.environ['device']]
            print self.s2[os.environ['device']]
            calculated_diff = self._get_snapshot_diff("s1_s2",self.s1[os.environ['device']], self.s2[os.environ['device']], num_of_context_lines)
            test_reference_diff = self._get_test_diff(num_of_context_lines)
            return self._check_diff_equality(calculated_diff, test_reference_diff)
        else:
            return True
        
    def check_s1_s3_diff(self):
        if not self.config.options.ignore_device:
            calculated_diff = self._get_snapshot_diff("s1_s3", self.s1[os.environ['device']], self.s3[os.environ['device']], None)
            return self._check_diff_equality(calculated_diff, "")
        else:
            return True
        
    def clear(self, device):
        if not self.config.options.ignore_device:
            #self.s1.clear()
            self.s1[device] = ""
            #self.s2.clear()
            self.s2[device] = ""
            self.s3[device] = ""
            #self.s3.clear()

    def get_device_current_status(self,device=None):
        if self.config.options.switch:
            logger.debug("Switch Device status")
            device ='switch'
        else:
            device = 'ap'
        if not self.config.options.ignore_device:
            return self.get_config.get_device_status()

    def connect_device(self):
        if not self.config.options.ignore_device:
            time.sleep(devices.CONNECTION_WAIT_TIME)
            self.get_config.connect_device_to_server()
            time.sleep(devices.CONFIG_CHANGE_WAIT_TIME)
            time.sleep(devices.CONFIG_CHANGE_WAIT_TIME)
            if not self.get_device_current_status():
                logger.info("*** DEVICE IS NOT UP. ABORTING TEST EXECUTION. ***")
                import sys
                sys.exit(1)