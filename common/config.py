import os


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_PATH)
# 定义测试数据的路径
TESTCASE_PATH =  os.path.join(BASE_PATH,'testDae')
print(TESTCASE_PATH)
# 定义测报告的路径
REPORT_PATH =  os.path.join(BASE_PATH,'reports')
print(REPORT_PATH)
# 定义日志文件的路径
LOG_PATH = os.path.join(BASE_PATH,'logs')