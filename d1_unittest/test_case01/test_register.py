import unittest

import ddt

from common.excel_handler import ExcelHandler
from common.requests_handler import RequestsHandler
from config.setting import config


@ddt.ddt
class TestRegister(unittest.TestCase):
    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('register')

    def setUp(self):
        # 实例化request库
        self.req = RequestsHandler()

    def tearDown(self) -> None:
        self.req.close_session()
        pass

    @ddt.data(*data)
    def test_register_success(self, test_data):
        # print(test_data)
        # 访问接口
        res = self.req.visit(config.host + test_data['url'],
                             test_data['method'],
                             json=eval(test_data['data']),
                             headers=eval(test_data['headers']))

        # 断言
        self.assertEqual(res['error'], test_data['expected'])

if __name__ == '__main__':
    unittest.main()