import sys
import os

FRAMEWORK_NAME = "athenataf"
FWORK_PARENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..",".."))
FWORK_CONTENT_DIR = os.path.join(FWORK_PARENT_DIR, FRAMEWORK_NAME)
TEMP_DIR =  os.path.join(FWORK_PARENT_DIR, "temp")
THIRD_PARTY_DIR = os.path.join(FWORK_PARENT_DIR, "3rdparty")
IN_DATA_PATH = os.path.join(FWORK_PARENT_DIR, FRAMEWORK_NAME, "test_data")
RESULTS_DIR = os.path.join(FWORK_PARENT_DIR, "results")
TESTS_DIR = os.path.join(FWORK_CONTENT_DIR, "tests")
MAPS_DIR = os.path.join(FWORK_CONTENT_DIR, "map")
CONFIG_DIR = os.path.join(FWORK_CONTENT_DIR, "config")
DEVICE_VERIFICATION_DIR = os.path.join(IN_DATA_PATH, "device_verification")
CONFIG_VARS_DIR = os.path.join(IN_DATA_PATH, "config_vars")

class DataPaths:
	Configuration = os.path.join(IN_DATA_PATH, "Configuration.xls")
	GroupManagement = os.path.join(IN_DATA_PATH, "GroupManagement.xls")
	Management = os.path.join(IN_DATA_PATH, "Management.xls")
	Configuration_e2e = os.path.join(IN_DATA_PATH, "Configuration_e2e.xls")
	single_rule = os.path.join(IN_DATA_PATH, "single_rule.xls")