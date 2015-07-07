import os

from athenataf.config import fwork
from athenataf.config import devices
from athenataf.lib.util.ConfigReader import ConfigReader
from athenataf.lib.util.ExcelReader import ExcelReader
from athenataf.lib.test.TestReporter import TestReporter
#from athenataf.lib.functionality.common.deviceverifier import DeviceVerifier

import logging
logger = logging.getLogger('athenataf')
import pprint
import time

class TestRunner:
    '''
        Base runner Class for all Test Cases
        Add tests to run from Excel data file thus 
        providing Data Driven Support to the frame work
    '''
    def __init__(self, config):
        '''
            Base runner Class Initiator Sets Data files from where Data need
            to be retrieved and to be used for Building Tests.
        '''
        logger.info("Initializing TestRunner")
        # The keys are test link ids and the values are import information.
        self.__test_map = {}
        if not os.path.isdir(fwork.RESULTS_DIR):
            os.makedirs(fwork.RESULTS_DIR)
        self.reporter = TestReporter(config)
        self.config = config
        if not 'device' in os.environ:
            if not self.config.options.switch:
                os.environ['device'] = "IAP_1"
            else:
                os.environ['device'] = "Switch_1"
        self.config.global_vars = ConfigReader("global_vars")
        self.config.config_vars = ConfigReader("config_vars")
        self._test_discover_count = 0
        self.filter_input_files = False
        self.filter_testlink_ids = False
        self.filter_test_classes = False
        self.filter_test_methods = False
        self.filtered_test_id_list = []
        if self.config.options.input_files != "ALL":
            self.filter_input_files = True
            self.config.input_files = [i.strip().upper() for i in self.config.options.input_files.split(",")]
        if self.config.options.testlink_ids != "ALL":
            self.filter_testlink_ids = True
            self.config.testlink_ids = [i.strip().upper() for i in self.config.options.testlink_ids.split(",")]
        if self.config.options.test_classes != "ALL":
            self.filter_test_classes = True
            self.config.test_classes = [i.strip().upper() for i in self.config.options.test_classes.split(",")]
        if self.config.options.test_methods != "ALL":
            self.filter_test_methods = True
            self.config.test_methods = [i.strip().upper() for i in self.config.options.test_methods.split(",")]

        import re
        self.aClassRef = {}
        self.aObjectRef = {}
        if not self.config.options.ignore_device:
            from inspect import isclass
            from Device_Module import IAPDevice
            # from Device_Module import ClientDevice
            from Device_Module import SwitchDevice
            classes = [x for x in dir(devices) if isclass(getattr(devices, x))]
            print classes
            for clas in classes:
                if getattr(devices, clas).type == "IAP":
                    self.aClassRef[clas] = type(clas, (IAPDevice.IAPDevice,), {})
                # elif getattr(devices, clas).type == "CLIENT":
                    # self.aClassRef[clas] = type(clas, (ClientDevice.ClientDevice,), {})
                elif getattr(devices, clas).type == "SWITCH":
                   self.aClassRef[clas] = type(clas, (SwitchDevice.SwitchDevice,), {})
                self.aObjectRef[clas] = self.aClassRef[clas]()
                print self.aObjectRef.values()
                val = self.aClassRef[clas]
                print clas
                print val
                for att in dir(getattr(devices, clas)):
                    if att != "__doc__" and att != "__module__":
                        setattr(val, att, getattr(getattr(devices, clas), att))
        self.error_type = None

    def _include_input_file(self, dd_file):
        logger.debug("Executing Input File Filter.")    
        if not dd_file.endswith(".xls"):    
            return False
        if self.filter_input_files:
            logger.debug("Check %s in %s" % (dd_file, self.config.input_files))    
            file_name = dd_file.split(".")[0]
            if file_name.upper() in self.config.input_files:
                return True
            else:
                return False
        else:
            return True

    def _include_test_id_based_on_column_filter(self, test_info):
        filter = test_info.record.get("FILTER?", None)
        if (filter is None) or (filter == u''):
            return True
        filter = filter.upper().strip()
        if self.config.options.exclude_filter:
            if filter == "Y":
                return False
            else:
                return True
        else:
            if filter == "Y":
                return True
            else:
                return False            

                            
    def _include_test_id(self, test_info):
        include = False
        if self.filter_testlink_ids:
            logger.debug("Check filter: %s in %s" % (test_info.id.upper(), self.config.testlink_ids))
            if test_info.id.upper() in self.config.testlink_ids:
                include = self._include_test_id_based_on_column_filter(test_info)
            else:
                include = False
        else:
            include = self._include_test_id_based_on_column_filter(test_info)

        
        return include

        
    def _include_test_class(self, class_name):
        if self.filter_test_classes:
            if class_name.upper() in self.config.test_classes:
                return True
            else:
                return False
        else:
            return True    

    def _include_test_method(self, method_name):
        if self.filter_test_methods:
            if method_name.upper() in self.config.test_methods:
                return True
            else:
                return False
        else:
            return True            

    def _add_test(self, test_module_meta):
        '''
            Adds Test meta data and forms Test_Queue from data files
        '''
        Test = None
        exec ("from %s import %s as Test" % (test_module_meta[0], test_module_meta[1]))
        test = Test(self.config)
        method_tuples = []
        logger.debug("Disovering Test Methods for Test Class: %s" % test.__class__.__name__)
        for m in test.__class__.__dict__.keys():
            if m.startswith("test"):
                test_id = "-".join([i.upper() for i in m.split("_")[1:3]])            
                if not self._include_test_method(m):
                    self.filtered_test_id_list.append(test_id)
                    continue
                self._test_discover_count += 1
                logger.debug(m)
                self.__test_map[test_id] = {
                                                "PARENT" : test,
                                                "PARENT_IMPORT_PATH" : test_module_meta[0],
                                                "METHOD_NAME" : m,
                                            }
        
    def discover(self, tests_filter=None):
        test_queue = []
        counter = 1
        for root, dirs, files in os.walk(self.config.options.tests_dir):
            index = root.find(self.config.options.tests_dir)
            import_path_prefix = ".".join(["athenataf", "tests", root[index + len(self.config.options.tests_dir) + 1:].replace("\\",".").replace("/", "."), ""])
            for test_module in files:
                if test_module.endswith(".py") and not test_module.startswith("_"):
                    test_module_name = test_module.split(".")[0]
                    if not self._include_test_class(test_module_name):
                        continue
                    test_module_import = import_path_prefix + test_module_name
                    include = True
                    if tests_filter is not None:
                        if test_module_name not in tests_filter:
                            include = False
                    if include:
                        test_queue.append([test_module_import, test_module_name])

        for test_module_meta in test_queue:
            self._add_test(test_module_meta)

            
        logger.info("TOTAL TESTS DISCOVERED IN CODE: %d" % self._test_discover_count)
        logger.debug("Test ID Keys:")    
        keys = self.__test_map.keys()
        keys.sort()
        for key in keys:
            logger.debug(key)

            
    def prepare(self):
        pass

        
    def setUp(self):
        self.reporter.setUp()
        if not self.config.options.ignore_device:
            retries = 0
            print(self.aObjectRef.values())
            for dev in self.aObjectRef.values():
                dev.connect()
            # while retries < 5:
                # dev = self.aObjectRef[os.environ['device']]
                # if dev.get_device_status():
                    # break
                # retries = retries + 1
            # if retries == 5:
                # logger.info("*** DEVICE IS NOT UP. ABORTING TEST EXECUTION. ***")
                # for dev in self.aObjectRef.values():
                    # dev.disconnect()
                # import sys
                # sys.exit(1)

        
    def _get_test_result_map(self, test_info):
        test_idea = test_info.record.get("TEST_IDEA", None)
        if (test_idea == u"") or (test_idea is None):
            test_idea = "Not Provided"
        test_result = {
                    "TESTLINK_ID" : test_info.record["TESTLINK_ID"],
                    "TEST_IDEA" : test_idea,                                    
                    "IMPORT_PATH" : test_info.ipath,
                    "TEST_CLASS" : test_info.klass,
                    "TEST_METHOD"    : test_info.method,
                    "TEST_DATA" : str(test_info.record),
                    "RESULT" : "NOT_SET",
                    "DURATION" : "",
                    "EXCEPTION" : "",
                    "TRACE"    : ""

        }
        return test_result

    def _execute_fixture(self, test_obj, method_name, test_result):
        try:
            if not method_name.startswith("test"):
                if not self.config.options.ignore_device:
                    retries = 0
                    # while retries < 3:
                        # dev = self.aObjectRef[os.environ['device']]
                        # if dev.get_device_status():
                            # break
                        # retries = retries + 1
                    # if retries == 3:
                        # logger.info("*** DEVICE IS NOT UP. ABORTING TEST EXECUTION. ***")
                        # for dev in self.aObjectRef.values():
                            # dev.disconnect()
                        # import sys
                        # sys.exit(1)
                logger.info("**** Device is UP *****")
                logger.info("Executing test.%s" % method_name)
            if not self.config.options.fake_run:
                apply(getattr(test_obj, method_name))
        except AssertionError, e:
            if 'actual and expected running config' in str(e):
                self.error_type = 'EE'
            elif 'Post clean-up the device did not' in str(e):
                self.error_type = 'EP'
            else:
                self.error_type = 'UKN'
            test_result["RESULT"] = "FAIL"
            import traceback
            test_result["EXCEPTION"] = "AssertionError in Test %s: %s" % (method_name, str(e))
            test_result["TRACE"] = traceback.format_exc(e)
            test_obj.on_fail()
            return None            
        except Exception, e:
            self.error_type = 'UKN'
            test_result["RESULT"] = "ERROR"            
            import traceback
            test_result["EXCEPTION"] = "Exception in Test %s: %s" % (method_name, str(e))
            test_result["TRACE"] = traceback.format_exc(e)    
            test_obj.on_error()            
            return None
        else:
            if method_name in ["setUp","tearDown"]:
                return "%s_SUCCESS" % method_name.upper()
            else:
                return "TESTMETHOD_SUCCESS"

            
    def _execute_test(self, test_info, test_result):
        try:
            setup_result = self._execute_fixture(test_info.parent, "setUp", test_result)
            run_result = None
            teardown_result = None
            if setup_result is not None:
                test_info.parent.record = test_info.record                

                run_result = self._execute_fixture(test_info.parent, test_info.method, test_result)
            teardown_result = self._execute_fixture(test_info.parent, "tearDown", test_result)
            if not ((setup_result is None) or (run_result is None) or (teardown_result is None)):
                test_result["RESULT"] = "PASS"
                method_parts = test_info.method.split('_')
                test_method_id = method_parts[1] + '-' + method_parts[2]
                f = open(os.path.join(self.config.results_dir, "passed_test_cases.txt"), "a")
                f.write(test_method_id + '\n')
                f.close()
                logger.info("TEST CASE RESULT : PASS")
            else:
                method_parts = test_info.method.split('_')
                test_method_id = method_parts[1] + '-' + method_parts[2]
                f = open(os.path.join(self.config.results_dir, "failed_test_cases.txt"), "a")
                f.write(test_method_id + ' - ' + self.error_type + '\n')
                f.close()
                logger.info("TEST CASE RESULT : FAIL")
                self.error_type = None
        except Exception, e:
            msg = "Exception in TestRunner while executing test: %s::%s" % (test_info.klass, test_info.method)
            logger.error(msg)
            test_result["RESULT"] = "ERROR_IN_TESTRUNNER"
            import traceback
            test_result["EXCEPTION"] = msg + str(e)
            test_result["TRACE"] = traceback.format_exc()

    def _execute_teardown_testclass(self):
        try:
            # Execute the Class Tear Down
            if ExecutionContext.current_class is not None:
                logger.info("%s:Tear Down Test Class" % ExecutionContext.current_class.split(".")[-1])
            else:
                logger.debug("[None]:Tear Down Test Class")
            if not self.config.options.fake_run:            
                ExecutionContext.current_test_obj.tearDownTestClass()
            logger.info("*" * 30)
        except Exception, e:
            msg = "Error in tearDownTestClass for %s" % ExecutionContext.current_class
            logger.error(msg)
            import traceback
            logger.debug(traceback.format_exc())
            if ExecutionContext.current_test_obj is not None:
                ExecutionContext.current_test_obj.on_error()
                ExecutionContext.current_test_obj.stop_browser()
            else:
                logger.debug("Current Test Object is None.")                
            
    def _execute_setup_testclass(self, test_info, test_result):
        # Execute the Class Set Up                    
        logger.info("*" * 30)                        
        logger.info("%s:Set Up Test Class" % test_info.klass)
        ExecutionContext.current_class = test_info.ipath
        ExecutionContext.current_test_obj =  test_info.parent        
        try:
            if not self.config.options.fake_run:
                test_info.parent.setUpTestClass()
        except Exception, e:
            msg = "Error in setUpTestClass for %s" % test_info.klass
            logger.error(msg)
            test_result["RESULT"] = "ERROR_IN_SETUP_TESTCLASS"
            import traceback
            test_result["EXCEPTION"] = msg + str(e)
            test_result["TRACE"] = traceback.format_exc()
            ExecutionContext.last_setup_class_failure = True
            test_info.parent.on_error()            
            return None
        else:
            # Only the absence of exception, the current variables are reset to new class
            ExecutionContext.last_setup_class_failure = False
            return "SUCCESS"
            
    def _log_testid_info(self, test_info):
        logger.info("-" * 30)                    
        logger.info("%s%s" % ("TESTLINK ID:".ljust(15),test_info.id))
        logger.info("%s%s" % ("IMPORT PATH:".ljust(15),test_info.ipath))
        logger.info("%s%s" % ("TEST METHOD:".ljust(15),test_info.method))                    
        logger.info("-" * 30)

    def _get_test_info(self, tests_reader, counter):
        try:
            record = tests_reader.get_next_record()
            logger.debug(str(record))
        except Exception, e:
            msg = "Error in reading records from Excel file: %s" % tests_reader.file_path
            logger.error(msg)
            logger.error(str(e))
            import traceback
            logger.error(traceback.print_exc())                        
            raise Exception(msg)                
        if record is None:
            raise Exception("Records finished")
            
        test_id = record.get("TESTLINK_ID", None)
        if (test_id is None) or (test_id == u''):
            logger.error("TESTLINK_ID not mentioned in %s, Record# %d" % (tests_reader.file_path, counter))
            return None
        test_method_meta = self.__test_map.get(test_id, None)
        if test_method_meta is None:
            if not test_id in self.filtered_test_id_list:
                logger.error("No automated test found for the TESTLINK_ID=%s" % (test_id))
            else:
                logger.error("Was added to excluded list post filtering: TESTLINK_ID=%s" % (test_id))
            return None    
        test_info = TestInfo()
        test_info.id = test_id
        test_info.record = record
        test_info.parent = test_method_meta["PARENT"]
        test_info.ipath = test_method_meta["PARENT_IMPORT_PATH"]
        test_info.klass = test_info.parent.__class__.__name__
        test_info.method = test_method_meta["METHOD_NAME"]
        return test_info
            
    def _get_tests_reader(self, file_name, dir_name):
        try:
            tests_dir_path = os.path.join(self.config.options.input_dir, dir_name)
            tests_path = os.path.join(tests_dir_path, file_name)
            tests_reader = ExcelReader(tests_path)
            return tests_reader
        except Exception, e:
            logger.error("Error in initialization of Excel file: %s" % tests_path)
            logger.error(str(e))
            import traceback
            logger.error(traceback.print_exc())
            return None
                    
    def _execute_excel_tests(self, file_name, dir_name):
        tests_reader = self._get_tests_reader(file_name, dir_name)
        if tests_reader is None: raise Exception("Not able to read from Excel File.")
        counter = 0
        while 1:
            begin_timestamp = time.time()
            counter += 1
            try:
                test_info = self._get_test_info(tests_reader, counter)
            except Exception, e:
                # import traceback
                # traceback.print_exc()
                break
            if test_info is None:
                continue
            if not self._include_test_id(test_info):
                logger.debug("Excluding the Test Id: %s" % test_info.id)
                continue
            else:
                logger.debug("Including the Test Id: %s" % test_info.id)
            test_result = self._get_test_result_map(test_info)
            logger.debug("Compare Current test class and test method's class")
            logger.debug("Current Test Class: %s" % ExecutionContext.current_class)
            logger.debug("Test Method Class: %s" % test_info.klass)    
            test_info.parent.current_test_method = test_info.method
            test_info.parent.current_test_id = test_info.id            
            if (ExecutionContext.current_class != test_info.ipath):
                logger.debug("Not same.")
                if ExecutionContext.current_class is not None:
                    logger.debug("Current class not None. So calling teardown.")
                    self._execute_teardown_testclass()
                logger.debug("Calling Setup test class.")                    
                result = self._execute_setup_testclass(test_info, test_result)
                if result is None:
                    logger.debug("Setup test class returned None. Skipping the current test method.")
                    logger.debug("Executing teardown test class.")                    
                    self._execute_teardown_testclass()                
                    test_result["SCREENSHOT"] = test_info.parent.current_screen_shots.get(test_info.method,[])
                    self.reporter.report(test_result)
                    continue
            elif ExecutionContext.last_setup_class_failure:
                logger.debug("Last setup class had failed.")            
                result = self._execute_setup_testclass(test_info, test_result)
                if result is None:
                    logger.debug("Setup test class returned None. Skipping the current test method.")                
                    logger.debug("Executing teardown test class.")                    
                    self._execute_teardown_testclass()                
                    test_result["SCREENSHOT"] = test_info.parent.current_screen_shots.get(test_info.method,[])
                    self.reporter.report(test_result)
                    continue
                    
            self._log_testid_info(test_info)
            self._execute_test(test_info, test_result)
            ExecutionContext.current_test_obj.record = None
            end_timestamp = time.time()
            test_result["DURATION"] = "%.2f" % (end_timestamp - begin_timestamp)
            test_result["SCREENSHOT"] = test_info.parent.current_screen_shots.get(test_info.method,[])
            self.reporter.report(test_result)

        # Tear down the last test class in the queue
        self._execute_teardown_testclass()

        
    def run(self):
        '''
            Runs Tests which are added in the Test_Queue
        '''
        allowed_test_types = []
        if self.config.options.test_types.upper() == "ALL":
            allowed_test_types = ["ui", "api"]
        else:
            allowed_test_types = [self.config.options.test_types.lower()]
        for dd_dir in os.listdir(self.config.options.input_dir):
            if dd_dir in allowed_test_types:
                for dd_file in os.listdir(os.path.join(self.config.options.input_dir, dd_dir)):
                    try:
                        if self._include_input_file(dd_file):
                            logger.debug("Including the Input File: %s" % dd_file)                    
                            self._execute_excel_tests(dd_file, dd_dir)
                        else:
                            logger.debug("Excluding the Input File: %s" % dd_file)
                    except Exception, e:
                        print "Exception occured in TestRunner"
                        import traceback
                        traceback.print_exc()

        
    def tearDown(self):
        '''
            Tear Down for Test Runner
        '''
        for dev in self.aObjectRef.values():
            logger.info(dev)
            dev.disconnect()
        self.reporter.tearDown()    

        
class TestInfo:
    def __init__(self):
        id = None
        record = None
        parent = None
        ipath = None
        klass = None
        method = None

        
class ExecutionContext:
    current_class = None
    current_test_obj = None
    last_setup_class_failure = False
