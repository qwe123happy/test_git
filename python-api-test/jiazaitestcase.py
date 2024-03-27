import HTMLTestRunnerNew
import unittest
from common.request_shizhan import TestCase
import HTMLTestRunnerNew
from common import constants

suite=unittest.TestSuite()
loads=unittest.TestLoader()
suite.addTest(loads.loadTestsFromTestCase(TestCase))

# runner=unittest.TextTestRunner()
# runner.run(suite)
with open(constants.reports_path+r'\report.html','wb') as file:
# with open(r'..\reports\report.html','wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,
                                         title='单元测试报告标题', description='单元测试报告描述',tester='陈彬')
    runner.run(suite)