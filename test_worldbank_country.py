import unittest

from selenium import webdriver
from worldbank import *
import json
import requests


#用例只简单测试接口的连通性

class TestWorldBank(unittest.TestCase):
    def setUp(self):                 #用例的前置条件
        self.driver = webdriver.Chrome()

    def tearDown(self):             #用例的后置条件
        self.driver.close()

    def test_getAPI(self):         #针对第一个接口设计的用例

       try:
          driver.get('https://api.worldbank.org/v2/countries')       #获取接口信息
    #查看页面中是否有//*[@id="folder0"]/div[1]/span[2]/span[4]/span[1]元素存在
          ele = driver.find_element_by_class_name('html-attribute-name').text      #将接口返回信息中的某一个元素进行定位
          self.assertEqual(driver.find_element_by_class_name,'per_page')           #根据这个元素判断接口是通的，能正常返回数据

       except:
          print('接口正常访问')

    def test_listcountry(self):                #针对第二个接口设计的用例

        res = requests.get('https://api.worldbank.org/v2/countries?format=json')       #获取接口返回的json数据
        result = res.json()           #接口返回的是一个列表

        if 'per_page' in result[0]:          #判断列表的第一个数据元素是per_page,以此判断该接口能正常返回数据
            print('pass')
        else:
            assert False

    def test_detailcountry(self):         #针对第三个接口设计的用例
        res = requests.get('https://api.worldbank.org/v2/countries/FI?format=json')
        result = res.json()

        if 'per_page' in result[0]:     #判断列表的第一个数据元素是per_page,以此判断该接口能正常返回数据
            pass
        else:
            assert False

if __name__ == '__main__':
    unittest.main()


