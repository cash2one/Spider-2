
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
        
    def exeUpdate(self,info_dict_list,filter__dict_list):  
        '''
        info_dict_list = (   {'set_row':'username', 'set_value':"'xgl'"},
                        {'set_row':'area',     'set_value':"'南京'"})
        filter__dict_list = ( {'filter_row':'username','filter_value':"''",'filter_operator':'='},
                        {'filter_row':'area','filter_value':"''",'filter_operator':'='}
                       )
        '''
        sql = 'UPDATE user SET '
        for info_dict in info_dict_list:
            sql += info_dict['set_row']
            sql += ' = '
            sql += info_dict['set_value']
            sql += ','
        sql = sql[:-1]
        sql += ' WHERE '
        for filter_dict in filter__dict_list:
            sql += filter_dict['filter_row']
            sql += filter_dict['filter_operator']
            sql += filter_dict['filter_value']
            sql += ' AND '
        sql = sql[:-4]
        print(sql)
        #UPDATE user SET username = 'xgl',area = '南京' WHERE username='' AND area='' 
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
     
    def exeDelete(self, table_name_string ,row_name_string,value_string,where_operator=' = '):  
        # 删除语句，可批量删除
        for each_value in value_string.split(','):
            try:
                sql = 'delete from ' + table_name_string + ' where '+ row_name_string + where_operator + each_value
                self.cur.execute(sql)
                self.conn.commit()
                print(row_name_string +':',each_value,' has deleted successfully!')
            except Exception as e:
                print('exeDelete():',e)
                print(row_name_string +':',each_value,"deleted error!")
    
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
