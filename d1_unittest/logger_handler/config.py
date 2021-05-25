"""
字典：
key:value,  声音：80，  亮度：20

变量：
声音 = 50
亮度 = 20
灵活管理 不同的环境 不同的配置
"""


class LoggerConfig:
    logger_name = 'python01'
    logger_file = 'python01.txt'
    level = 'DEBUG'


class ProductLoggerConfig(LoggerConfig):
    level = 'WARNING'


# if sys.platform == 'linux':
#     config = ProductLoggerConfig
# else:
#     config = LoggerConfig
