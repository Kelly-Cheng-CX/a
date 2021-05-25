from d1_unittest.logger_handler.d1_demolog import main
from d1_unittest.logger_handler.logger_handler02 import logger

# logger = LoggerHandler('python', file='demo_log.txt')


def h():
    print("d")
    logger.info('12345')
    main()


if __name__ == '__main__':
    h()
