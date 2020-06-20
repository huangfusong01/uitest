import logging
from logging import handlers
import os


#  日志的文件路径包
log_path =os.path.dirname(os.path.dirname(os.path.abspath(__name__)))
print(os.path.dirname(__name__))



class Logger():
    leval_relation = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self, fileName='{}/logs/all.log'.format(log_path), when='D', backCount=5,level='info', frm='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.Logger(fileName)  #实例化一个logger的文件对象
        format_str = logging.Formatter(frm)   #定义日志输出格式
        self.logger.setLevel(self.leval_relation.get(level))  #设置日志输出等级
        stream_handler = logging.StreamHandler()  # 实例化日志控制台输出对象
        stream_handler.setFormatter(format_str)  # 设置控制台日志输出格式
        file_handler = handlers.TimedRotatingFileHandler(filename=fileName, when=when, backupCount=backCount, encoding= 'utf-8')  #实例化文件输出对象
        file_handler.setFormatter(format_str)
        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)


if __name__ == '__main__':
    test = "test"
    logger = Logger()
    logger.logger.info(test)
