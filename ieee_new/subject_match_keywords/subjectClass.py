#coding:utf-8

class Subject(object):
    def __init__(self,name):
        self.name = name
        self.maxKeyword = ''
        self.keyword_buffer_list = []
        self.keyword_buffer_list.append({'keyword_name':'sample_keyword_name','cot':0})
        
    def update_keyword(self,keyword_name):
        isExist = False
        for item in self.keyword_buffer_list:
            if item['keyword_name'] == keyword_name:
                isExist = True
                item['cot'] += 1
                break
        if not isExist:
            self.keyword_buffer_list.append({'keyword_name':keyword_name,'cot':1})
    
    def get_max_keyword(self):
        max_item = self.keyword_buffer_list[0]
        max = 0
        for item in self.keyword_buffer_list:
            if item['cot'] > max:
                max = item['cot']
                max_item = item
        self.maxKeyword = max_item
        
    def show_result(self):
        print('name:',self.name)
        print('maxKeyword:',self.maxKeyword)
        print('-----------')