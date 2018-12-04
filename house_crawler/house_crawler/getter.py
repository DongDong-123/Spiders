from .crawler import Crawler
from .setting import *
import sys
from .db_save import Connect_mysql


class Getter:
    def __init__(self):
        # self.redis = RedisClient()
        self.crawler = Crawler()
        self.mysql = Connect_mysql()
    
    def process_error(self, callback):
        """
        捕获链接异常，重新连接
        :param callback:
        :return: list
        """
        try:
            house_data = self.crawler.get_data(callback)
        except Exception as e:
            print('E:', e)
            house_data = self.process_error(callback)

        return house_data

    def run(self):
        print('获取器开始执行')

        for callback_label in range(self.crawler.__CrawlFuncCount__):

            print('callback_label', callback_label, type(callback_label))
            callback = self.crawler.__CrawlFunc__[callback_label]
            print('callback', callback, type(callback))
            # 获取数据
            house_data = self.process_error(callback)
            print('house_data', len(house_data), type(house_data))
            sys.stdout.flush()
            for data in house_data:
                self.mysql.inserts(data)
