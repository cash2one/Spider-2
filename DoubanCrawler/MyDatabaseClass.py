
# coding: utf-8
__author__ = 'luyang'  

import pymysql

class MyDatabase(object):
    def __init__(self,host,user,passwd,db,port,charset):
        try:
            self.conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db,port=port,charset=charset)
            self.cur = self.conn.cursor()
        except:
            print("Mysql connects error!")
        
    def showData(self,table_name_string):
        sql =  'select * from ' + table_name_string
        self.cur.execute(sql)
        data = self.cur.fetchall()
        for element in data:
            print(element)
        
    def exeUpdate(self, sql):  # 更新语句，可执行Update，Insert语句
        staus = self.cur.execute(sql);
        self.conn.commit()
        print('Execute SQL sentence returns code : ',staus)
    
    def exeDelete(self, table_name_string ,IDs):  # 删除语句，可批量删除
        for eachID in IDs.split(' '):
            try:
                sql = 'delete from ' + table_name_string + ' where Id=' + eachID
                self.cur.execute(sql)
                self.conn.commit()
                print('id:',eachID,' has deleted successfully!')
            except:
                print('id:',eachID,"deleted error!")
    
    def connClose(self):  # 关闭所有连接
        self.cur.close()
        self.conn.close()
    '''
    在这里，基本的增删改查的函数基本完成，这里要讲一下exeUpdate函数，也许在别人的源码中也看到过这一个函数，但参数只有两个：
    cur与sql，没有conn，如果函数内不加上conn.commit()
    这一行代码，在新增时不会报错，也会提示成功，但数据库中是不会看到自己新加的数据的，这一句代码的作用，就类似于保存当前修改，
    不加上当前这一行代码，当前修改或者新增操作就没有实现。
    '''  
