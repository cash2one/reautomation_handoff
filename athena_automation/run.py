import sys
import os
import logging
import time

fwork_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(fwork_path)
from athenataf.config import fwork
sys.path.append(fwork.THIRD_PARTY_DIR)
from athenataf.lib.util.command import *
config = get_options()

# Set up the logger for the framework
from athenataf.config import fwork
config.results_dir = os.path.abspath(os.path.join(config.options.output_dir, config.options.run_id))
if not os.path.isdir(config.results_dir): os.makedirs(config.results_dir)
config.screenshots_dir = os.path.join(config.results_dir, "screenshots")
os.makedirs(config.screenshots_dir)
config.html_report_dir = os.path.join(config.results_dir, "htmlReports")
os.makedirs(config.html_report_dir)
config.html_frame_dir = os.path.join(config.html_report_dir, "htmlFrames")
os.makedirs(config.html_frame_dir)
if not config.options.ignore_device:
	config.device_verification_dir = os.path.join(config.results_dir, "device_verification")
	os.makedirs(config.device_verification_dir)

# Check whether logging should be directed to a file instead of console
if config.options.log_to_file:
	# [%(pathname)s]:
    logging.basicConfig(format='[%(levelname)s]%(asctime)s:%(module)s:%(funcName)s:Line-%(lineno)s:: %(message)s', filename=os.path.join(config.results_dir,"_athenataf.log"))
else:
    logging.basicConfig(format='[%(levelname)s]%(module)s:%(funcName)s:Line-%(lineno)s:: %(message)s')
	
# Check whether debug messages should be included or not (Default is enabled)
logger = logging.getLogger('athenataf')
if config.options.quiet:
	logger.setLevel(logging.INFO)
else:
	logger.setLevel(logging.DEBUG)
	
logger.info("Results directory: %s" % config.results_dir)	
logger.debug("Initializing variables")

from athenataf.lib.test.TestRunner import TestRunner
logger.info("="* 30)
logger.info("TestRunner: Initialization")
tr = TestRunner(config)            
logger.debug("TestRunner: Discover Tests")
tr.discover()
logger.debug("TestRunner: Set Up")
tr.setUp()
logger.debug("Test Run:: Begin")
tr.run()
logger.debug("Test Run:: Finish")
logger.debug("TestRunner: Tear Down")
tr.tearDown()
logger.debug("="* 30)