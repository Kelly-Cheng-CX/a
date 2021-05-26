import os

"""
     abspath（__file__）  获取当前文件的绝对路径  
     dirname()  返回path路径最后一个\\之前的内容
     join(path+path)    拼接
 testloader.discover(文件夹路径，‘匹配模式默认test_*.py开头’)发现测试用例

"""
class Config:
    # 得到当前项目路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 测试数据文件夹路径
    data_path = os.path.join(root_path, 'data/cases.xlsx')

    # 测试用例路径
    case_path = os.path.join(root_path, 'test_case01')

    # 测试报告路径
    # 如果没有report文件夹 就创建一个report文件夹
    report_path = os.path.join(root_path, "report")
    # try:
    #     if os.path.exists(report_path):
    #         os.makedirs(report_path)
    #         print("a")
    # except Exception as err:  # 如果某个异常不知道，且不是前面两个异常，可以用这个必杀技解决
    #     pass

class DevConfig(Config):
    # 域名地址1
    host = 'https://sso-qa.gaiaworkforce.com'
    host1 = 'http://test.lemonban.com/futureloan/mvc/api/member'


config = DevConfig()
