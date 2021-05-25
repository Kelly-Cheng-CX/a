import requests
import unittest


class RequestsHandler:

    def __init__(self):
        self.session = requests.Session()
        """
        访问一个接口，可以使用get/post/put/...请求
        请求方法：method
        请求参数:json,data,params
        请求地址：url
        """

    def visit(self, url, method, params=None, data=None, json=None, **kwargs):
        res = self.session.request(method, url, params=params, data=data, json=json, **kwargs)
        try:
            return res.json()
        except ValueError:
            print("NOT JSON error")
