import unittest

import ddt

from common.excel_handler import ExcelHandler
from common.requests_handler import RequestsHandler


# test_data = [
#     {"url": "http://test.lemonban.com/futureloan/mvc/api/member/login",
#      "method": "post",
#      "headers": {"X-Lemonban-Media-Type": "lemonban.v2"},
#      "data": {"mobilephone": "18111111111", "pwd": "123456"},
#      "expected": "hello world"},
#     {"url": "http://test.lemonban.com/futureloan/mvc/api/member/login",
#      "method": "post",
#      "headers": {"X-Lemonban-Media-Type": "lemonban.v2"},
#      "data": {"mobilephone": "asv", "pwd": "123456"},
#      "expected": "hello world2"}
# ]
test_data = ExcelHandler(r"H:\a\d1_unittest\data\cases.xlsx").read('Sheet1')
print(test_data)


@ddt.ddt
class TestLogin(unittest.TestCase):
    # 前置条件当中 每个用例方法之前会运行的代码

    def setUp(self):
        print("前置条件")

    def tearDown(self):
        print("后置条件测试用例执行完毕")

    # 将*test_data当中的一组测试数据 赋予到data_info这个参数 相当于for循环1
    @ddt.data(*test_data)
    def test_login_success(self, data_info):
        res = RequestsHandler().visit(data_info['url'],
                                      data_info['method'],
                                      data=eval(data_info['data']),
                                      headers=eval(data_info['headers']))
        self.assertEqual(res['code'], eval(data_info['expected'])['code'])


if __name__ == '__main__':
    unittest.main()



