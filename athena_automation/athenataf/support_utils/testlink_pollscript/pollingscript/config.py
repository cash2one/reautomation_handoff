import os
#Connection string to Testlink DB
TESTLINK_HOST_NAME='10.1.1.153'
TESTLINK_USER_NAME='readonly'
TESTLINK_PWD='readonly'
TESTLINK_DB_NAME='testlink'


#DB QUERY
SELECT_QUERY="select tc.tc_external_id as TestcaseID, MAX(tc.modification_ts) as LastUpdatedDate from testlink.nodes_hierarchy n,testlink.keywords k, testlink.testcase_keywords tk ,testlink.nodes_hierarchy n2 ,testlink.tcversions tc  where k.id = tk.keyword_id and tk.testcase_id = n.id and k.keyword = 'automated' and n.node_type_id = 3 and  n2.parent_id = n.id and tc.id = n2.id and k.testproject_id = 235213 Group by tc.tc_external_id"

#DATA PATH
TESTLINK_XLS_PATH=os.path.dirname(os.path.realpath(__file__))+'\\automatedTestCases_testlink'
TESTLINK_XLS_NAME=os.path.dirname(os.path.realpath(__file__))+'\\automatedTestCases_testlink.xls'
FRAMEWORK_XLS_NAME=os.path.dirname(os.path.realpath(__file__))+'\\automatedTestCases_framework.xls'
FRAMEWORK_TESTDATA_PATH = "D:\\test_data"