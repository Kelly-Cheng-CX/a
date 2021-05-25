import logging


class LoggerHandler:
    def __init__(self,
                 name='root',
                 level='DEBUG',
                 file=None,
                 format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        logger = logging.getLogger(name)

        # 设置级别
        logger.setLevel(level)
        # 设置log格式
        fmt = logging.Formatter(format)
        # 初始化处理器 如果传了file那就是FileHandler
        if file:
            file_handler = logging.FileHandler(file)
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            logger.addHandler(file_handler)

        steam_handler = logging.StreamHandler()
        # 设置handler级别
        steam_handler.setLevel(level)
        steam_handler.setFormatter(fmt)
        logger.addHandler(steam_handler)

        self.logger = logger

    def debug(self, msg):
        return self.logger.debug(msg)

    def info(self, msg):
        return self.logger.info(msg)

    def warning(self, msg):
        return self.logger.warning(msg)

    def error(self, msg):
        return self.logger.error(msg)

    def critical(self, msg):
        return self.logger.error(msg)


if __name__ == '__main__':
    logging = LoggerHandler()
    logging.debug('hello')
