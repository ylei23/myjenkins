import logging
class MyLoger:
    def __init__(self):
        self.filename=r'C:\Users\he\PycharmProjects\woniu233\hh\loglog\aa.txt'
    def logger(self,fmt='%(asctime)s-%(filename)s-%(lineno)s-%(message)s'):
        logger=logging.getLogger()
        #设置日志级别
        logger.setLevel(level=logging.DEBUG)
        #创建一个日志格式器
        myfmt=logging.Formatter(fmt=fmt)
        #创建一个日志处理器
        f=logging.FileHandler(filename=self.filename,mode='a',encoding='utf-8')
        #给日志记录器添加一个处理器
        logger.addHandler(f)
        #给日志处理器添加一个格式器
        f.setFormatter(fmt=myfmt)
        s=logging.StreamHandler()
        logger.addHandler(s)
        s.setFormatter(fmt=myfmt)
        return logger
loger=MyLoger().logger()

        # print(logger)
if __name__ == '__main__':

    MyLoger().logger().info('这是信息')
