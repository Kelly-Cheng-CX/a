import os


class Config:
    # 得到当前项目路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 测试数据文件夹路径
    data_path = os.path.join(root_path, 'data/cases.xlsx')


class DevConfig(Config):
    # 域名地址
    host = 'https://sso-qa.gaiaworkforce.com'
    host1 = 'http://test.lemonban.com/futureloan/mvc/api/member'


config = DevConfig()
