import logging

from d1_unittest.logger_handler import config




class LoggerHandler(logging.Logger):
    def __init__(self,
                 name='root',
                 level='DEBUG',
                 file=None,
                 format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        super().__init__(name)
        # 设置级别
        self.setLevel(level)
        # 设置log格式
        fmt = logging.Formatter(format)
        # 初始化处理器 如果传了file那就是FileHandler
        if file:
            file_handler = logging.FileHandler(file)
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)

        steam_handler = logging.StreamHandler()
        # 设置handler级别
        steam_handler.setLevel(level)
        steam_handler.setFormatter(fmt)
        self.addHandler(steam_handler)


logger = LoggerHandler(config.LoggerConfig.logger_name, file=config.LoggerConfig.logger_file)

if __name__ == '__main__':
    logger = LoggerHandler()
    logger.debug('hello')
