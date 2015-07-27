import optparse
import os
import time
usage = """Usage: %prog [options]"""
from athenataf.config import fwork

class Configuration:
    '''
    Base class for Command Line Interface .
    '''
    def __init__(self, options, args):
        self.options = options
        self.args = args

def get_options():
    parser = optparse.OptionParser(usage=usage)
    # parser.add_option("-h", "--help", action="help")  
    parser.add_option('-d', "--tests_dir", dest='tests_dir',
                  default=fwork.TESTS_DIR,
                  help='Parent directory of test case modules. Default: As per fwork.py')
    parser.add_option('-k', "--input_dir", dest='input_dir',
                  default=fwork.IN_DATA_PATH,
                  help='Parent directory of input files. Default: As per fwork.py')               
    parser.add_option('-o', "--output_dir", dest='output_dir',
                  default=fwork.RESULTS_DIR,
                  help='Directory for results and logs. Default: As per fwork.py')                
    parser.add_option('-x', "--run_id", dest='run_id',
                  default=time.strftime("%d_%b_%Y_%H_%M_%S", time.localtime()),
                  help='Test Run ID. Default: Current Timestamp')
    parser.add_option('-n', "--no_screenshots", dest='no_screenshots', action='store_true',
                  default=False,
                  help='Switch off screenshots')
    parser.add_option('-q', "--quiet", dest='quiet', action='store_true',
                  default=False,
                  help='Switch off debug log messages')           
    parser.add_option('-l', "--log_to_file", dest='log_to_file', action='store_true',
                  default=False,
                  help='Log to file instead of console')
    parser.add_option('-f', "--fake_run", dest='fake_run', action='store_true',
                  default=False,
                  help='Does not execute tests, verifies athenataf structure.')               
    parser.add_option('-r', "--report_format", dest='report_format',
                  default='html',
                  help='Report Format. Supprter: html. Default: html')                
    parser.add_option('-b', "--browser", dest='browser',
                  default='Firefox',
                  help='Target Browser (Supported:Firefox) Default:Firefox')                  
    parser.add_option('-i', "--input_files", dest='input_files',
                  default="ALL",
                  help='Input Test Files to be executed.(, separated) Default:All')
    parser.add_option('-t', "--test_ids", dest='testlink_ids',
                  default="ALL",
                  help='TestLink IDs to be executed.(, separated) Default:All')
    parser.add_option('-c', "--test_classes", dest='test_classes',
                  default="ALL",
                  help='Test Classes to be executed.(, separated) Default:All')
    parser.add_option('-m', "--test_methods", dest='test_methods',
                  default="ALL",
                  help='Test Methods to be executed.(, separated) Default:All')
    parser.add_option('-e', "--exclude_filter", dest='exclude_filter', action='store_true',
                  default=False,
                  help='The Column level filter in input files works in exclude mode for the value Y.') 
    parser.add_option("--ignore_device", dest='ignore_device', action='store_true',
                  default=False,
                  help='Ignore Device Verification functionality.')
    parser.add_option("--switch", dest='switch', action='store_true',
                  default=False,
                  help='Device under test is Switch.')
    parser.add_option("--test_types", dest='test_types',
                  default="ui",
                  help='Test Types to be executed(ui, api, or all).(, separated) Default:UI')
    parser.add_option("--mail_report", dest='mail_report', action='store_true',
              default=False,
              help='send html report after execution is complete to receipent given in globalvars.props')
    cmd, args = parser.parse_args()
    config  = Configuration(cmd, args)
    return config