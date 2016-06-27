#coding:utf-8

class Subject(object):
    def __init__(self,name):
        '''
                    为每一个学科建类，包括名字和最强关键词（次数出现最多）
                    类方法包括更新模型，以及统计模型
        '''
        self.name = name
        self.maxKeyword = ''
        self.keyword_buffer_list = []
        self.keyword_buffer_list.append({'keyword_name':'sample_keyword_name','cot':0})
        
    def update_keyword(self,keyword_name):
        '''
                    更新模型：
                    包括关于关键词的两种情况：file
                    一是已经存过，则给其计数加一
                    二是未存过，则新创建一个keyword字典
        '''
        isExist = False
        for item in self.keyword_buffer_list:
            if item['keyword_name'] == keyword_name:
                isExist = True
                item['cot'] += 1
                break
        if not isExist:
            self.keyword_buffer_list.append({'keyword_name':keyword_name,'cot':1})
    
    def get_max_keyword(self):
        '''
                    数据全部注入更新模型后 ，进入统计模型，统计最大次数出现的关键词
                    作为主关键词   
        '''
        max_item = self.keyword_buffer_list[0]
        max = 0
        for item in self.keyword_buffer_list:
            if item['cot'] > max:
                max = item['cot']
                max_item = item
        self.maxKeyword = max_item
        
    def show_result(self):
        '''
                    展示统计结果
        '''
        print('subjectName:',self.name)
        print('maxKeyword:',self.maxKeyword)
        print('-----------')