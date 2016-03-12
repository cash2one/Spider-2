#codingL:utf-8

import pymysql

class Weibo(object):
    def __init__(self,dbObj):
        self.author = ''
        self.database = dbObj
        self.content = ''
        self.time = ''
        #包括评论作者和时间及内容组成的大字符串
        self.comment = ''
        