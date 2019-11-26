#coding=utf-8
import unittest
import time
from HTMLTestRunner import HTMLTestReportCN
import os
import logging
# from Config.config import email


def load_tests(casename):
    pyname =str(casename)+'.py'
    logging.info('本次执行的是:'+ pyname +'文件')
    testunit=unittest.TestSuite()
    #使用discover找出用例文件夹下test_casea的所有用例
    father_path=os.path.abspath(os.path.dirname(__file__)+os.path.sep+"../")
    discover =unittest.defaultTestLoader.discover(father_path+"/testcases", pattern=pyname, top_level_dir=None)
    for suite in discover:  #使用for循环出suite,再循环出case
        for case in suite:
            testunit.addTest(case)
    return testunit

#运行用例并生成suite
def run_testcase(casename):
    #格式化报告名称与路径
    time_format = time.strftime('%Y%m%d_%H-%M-%S',time.localtime())
    report_path = os.path.dirname(os.path.abspath("."))+"/reports"
    file_path = report_path+"/reports"+time_format+".html"
    #生成测试报告
    fp = open(file_path,"wb")
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,title=u"UI自动化测试报告",description=u"用例执行概要")
    runner.run(load_tests(casename))
    fp.close()
    time.sleep(5)
    return file_path

if __name__=="__main__":
    report_path=run_testcase('login*')
    # email().send_mail()
