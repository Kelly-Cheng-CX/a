"""
收集测试用例 TestLoader 加载器 加载测试用例
testloader.discover(文件夹路径，‘匹配模式默认test_*.py开头’)发现测试用例

放到测试套件中（集合）Testsuite

"""
# encoding:utf-8
# !/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import unittest
import time

from common.HTMLTestRunner import HTMLTestRunner
from config.setting import config

"""
1，初始化 testloader
"""
testloader = unittest.TestLoader()

"""
 2,查找加载测试用例 
     abspath（__file__）  获取当前文件的绝对路径  
     dirname()  返回path路径最后一个\\之前的内容
     join(path+path)    拼接
 testloader.discover(文件夹路径，‘匹配模式默认test_*.py开头’)发现测试用例



dir_path = os.path.dirname(os.path.abspath(__file__))  # 当前文件的目录地址
case_path = os.path.join(dir_path, 'test_case01')

加载指定模块 将测试用例 合并到一个总的测试套件里
suite = testloader.loadTestsFromModule(test_register)
suite2 = testloader.loadTestsFromModule(test_recharge)

suite_total = unittest.TestSuite()

suite_total.addTests(suite)

suite_total.addTests(suite2)

"""

# 跑哪个路径文件下的case
suite_total = testloader.discover(config.case_path)

print(suite_total)
"""
生成测试报告
"""
if not os.path.exists(config.report_path):
    os.mkdir(config.report_path)

ts = str(int(time.time()))

file_name = 'test_result{}.html'.format(ts)

file_path = os.path.join(config.report_path, file_name)

# TODO ：一定要使用二进制的方式打开
with open(file_path, 'w', encoding='utf-8') as f:
    # 初始化运行器，是以普通文本生成测试报告 TextTestRunner
    runner = HTMLTestRunner(f, verbosity=2, title="史上最帅的测试报告",
                            description='真的帅')
    # 运行测试用例
    runner.run(suite_total)

if __name__ == '__main__':
    unittest.main()