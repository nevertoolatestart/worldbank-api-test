import unittest
from test_worldbank_country import TestWorldBank


from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()

    #使用TestLoader的方法传入Testcase
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestWorldBank))


    with open('HTMLReport.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f,title=u'测试报告',
                                description=u'测试用例的执行情况',
                                verbosity=2)
        runner.run(suite)

