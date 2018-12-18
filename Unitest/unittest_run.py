#coding=utf-8

import unittest
import HTMLTestRunner




if __name__ == '__main__':

    suit = unittest.TestSuite()
    testcase = unittest.defaultTestLoader.discover('D:\\PyTest\\test_case')
    suit.addTests(testcase)

    log_path = 'D:\\PyTest\\logfile\\1.html'

    with open(log_path,'w') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='AutoTestResult')
        runner.run(suit)