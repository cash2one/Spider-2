#codingL:utf-8

import pymysql

class Weibo(object):
    def __init__(self,dbObj):
        self.author = ''
        self.database = dbObj
        self.content = ''
        self.time = ''
        #�����������ߺ�ʱ�估������ɵĴ��ַ���
        self.comment = ''
        