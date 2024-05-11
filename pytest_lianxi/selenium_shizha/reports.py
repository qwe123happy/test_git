import HTMLTestRunnerNew
import unittest
from selenium_shizha.login_testcases import TestLogin

suite=unittest.TestSuite()
loder=unittest.TestLoader()
suite.addTest(loder.loadTestsFromTestCase(TestLogin))
with open('shizhan.html','wb') as file:
    runner= HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,
        title='单元测试报告标题', description='单元测试报告描述')
    runner.run(suite)