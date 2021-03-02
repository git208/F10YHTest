import logging

class LogCustom():
    def
    logger = logging.getLogger('myLog')
    fmt = logging.Formatter(fmt='%(asctime)s [%(pathname)s:%(lineno)d 行]| %(levelname)s | %(message)s | %(funcName)s',
                            datefmt='%Y/%m/%d/%X')
    myHandler = logging.StreamHandler()
    logger.addHandler(myHandler)
    myHandler.setFormatter(fmt)
    logger.level = logging.DEBUG
    logger.debug('我是你们的女王!')



if __name__ == '__main__':
