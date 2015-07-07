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
            if not self.config.options.ignore_device:
                self.get_config = Device.Device.getDeviceObject(device)
        except Exception as err:
            print err
            raise
            pass
        self.differ = TextDiffer()
        self.test = test
        self.s1 = None
        self.s2 = None
        self.s3 = None
        self.device_results_test_dir = None

    def _log_snapshot(self, name, snapshot):
        self.device_results_test_dir = os.path.join(self.config.device_verification_dir, self.test.current_test_id)
        if not os.path.isdir(self.device_results_test_dir): os.makedirs(self.device_results_test_dir)
        f = open(os.path.join(self.device_results_test_dir, "%s.txt" % name), "w")
        f.write(snapshot)
        f.close()
        
    def _take_snapshot(self, type, extra_command = None):
        config = self.get_config.get_running_config(extra_command)
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
            self.clear()
            if not self.config.options.switch:
                time.sleep(devices.CONFIG_CHANGE_WAIT_TIME)
            self.s1 = self._take_snapshot("s1",  extra_command)
        
    def take_s2_snapshot(self, extra_command = None):
        if not self.config.options.ignore_device:
            if not  self.config.options.switch:
                time.sleep(devices.CONFIG_CHANGE_WAIT_TIME)    
            self.s2 = self._take_snapshot("s2",  extra_command)
        
    def take_s3_snapshot(self, extra_command = None):
        if not self.config.options.ignore_device:
            if not  self.config.options.switch:        
                time.sleep(devices.CONFIG_CHANGE_WAIT_TIME)    
            self.s3 = self._take_snapshot("s3",  extra_command)        
        
    def _get_test_diff(self, num_of_context_lines):
        expected_config_diff = None
        if self.config.options.switch:
            diff_file_path = os.path.join(fwork.DEVICE_VERIFICATION_DIR+"\%s"%self.get_config.get('type') , "%s_s1_s2_diff.txt") % self.test.current_test_id
        else:
            diff_file_path = os.path.join(fwork.DEVICE_VERIFICATION_DIR+"/%s"%self.get_config.get('type') +"/%s"%self.get_config.get('version') , "%s_s1_s2_diff.txt") % self.test.current_test_id
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
        actual_config_diff = self.differ.get_difference(left_snapshot, right_snapshot, num_of_context_lines)
        f = open(os.path.join(self.device_results_test_dir, "%s_actual_diff.txt" % type), "w")
        f.write(actual_config_diff)
        f.close()        
        return actual_config_diff
        
    def check_s1_s2_diff(self , num_of_context_lines):
        if not self.config.options.ignore_device:
            calculated_diff = self._get_snapshot_diff("s1_s2",self.s1, self.s2, num_of_context_lines)
            test_reference_diff = self._get_test_diff(num_of_context_lines)
            return self._check_diff_equality(calculated_diff, test_reference_diff)
        else:
            return True
        
    def check_s1_s3_diff(self):
        if not self.config.options.ignore_device:
            calculated_diff = self._get_snapshot_diff("s1_s3", self.s1, self.s3, None)
            return self._check_diff_equality(calculated_diff, "")
        else:
            return True
        
    def clear(self):
        if not self.config.options.ignore_device:
            self.s1 = None
            self.s2 = None
            self.s3 = None
    
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