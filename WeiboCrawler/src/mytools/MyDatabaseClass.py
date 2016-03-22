
# coding: utf-8

import pymysql

class MyDatabase(object):
    '''
             基于pymysql做数据库的简易封装
            增删改查的函数基本完成，
            如果函数内不加上conn.commit()，当前修改或者新增操作就没有实现。
    '''  
    def __init__(self,host,user,passwd,db,port,charset):
        try:
            self.conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db,port=port,charset=charset)
            self.cur = self.conn.cursor()
        except:
            print("Mysql connects error!")
        
    def getData(self,table_name_string,row_name,limit=-1,order_by_row_name=''):
        #展示某表
        sql =  'select '+ row_name +' from ' + table_name_string
        if order_by_row_name != '':
            sql += ( ' order by ' + order_by_row_name )
        if limit != -1:
            sql +=( ' limit ' + str(limit) )
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data
        
    def exeUpdate(self, sql):  
        # 更新语句，可执行Update，Insert语句
        staus = self.cur.execute(sql);
        self.conn.commit()
        print('Execute SQL sentence returns code : ',staus)
    
    def exeDelete(self, table_name_string ,IDs):  
        # 删除语句，可批量删除
        for eachID in IDs.split(' '):
            try:
                sql = 'delete from ' + table_name_string + ' where Id=' + eachID
                self.cur.execute(sql)
                self.conn.commit()
                print('id:',eachID,' has deleted successfully!')
            except:
                print('id:',eachID,"deleted error!")
    
    def isExist(self,table_name_string,row_name,obj):
        data = self.getData(table_name_string, row_name)
        for item in data:
            if obj==item[0]:
                return True
        return False
    
    def connClose(self):  
        # 关闭所有连接
        self.cur.close()
        self.conn.close()