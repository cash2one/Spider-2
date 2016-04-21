#coding:utf-8

from stringHandleByMyself import match_str_slice

seat_dict = {
    1:       'Small Blind',
    2:       'Big Blind',
    3:       'UTG',
    4:       'UTG+1',
    5:       'UTG+2',
    6:       'Dealer',
     }

def role_index(role):
    for i in range(1,7):
        if seat_dict[i] == role:
            return i

class TexasPoker(object):
    def __init__(self,txt_slice):
        '''
                    用txt每局的片段初始化对象，并非整个txt
        '''
        self.txt_str = txt_slice
        self.play_id = ''
        self.session_id = ''
        self.time = ''
        self.my_seat_number = ''
        self.my_role = ''
        self.my_operation = []
        self.myhands = ''
        self.my_result = ''
        self.mychips = 0.1
        self.fold = False
        self.flop = ''
        self.turn = ''
        self.river = ''
        self.total_pot = ''
        
    def main_parse(self):
        info_list = self.txt_str.split('\n')
        handled_list = []
        for info in info_list:
            if info:
                handled_list.append(info)
        open_info_list = []
        process_info_list = []
        summary_info_list = []
        open_flag = True
        process_flag = False
        summary_flag = False
        line_number = 0
        for info in handled_list:
            if info=='*** HOLE CARDS ***':
                process_flag = True
                open_flag = False
            if info=='*** SUMMARY ***':
                summary_flag = True
                process_flag = False
            if open_flag:
                open_info_list.append(info)
            if process_flag:
                process_info_list.append(info)
            if summary_flag:
                summary_info_list.append(info)  
        #try:
        '''
        print(open_info_list)
        print(process_info_list)
        print(summary_info_list)
        '''
        self.parse_open(open_info_list)
        self.parse_process(process_info_list)
        self.parse_summary(summary_info_list)
        '''except Exception as e:
            print(e)
            print('return line code:',line_number)
        '''
        line_number += 1
            
    
    def get_play_id(self,first_line):
        flag = False
        buffer = ''
        for i in first_line:
            if flag:
                if i!=' ':
                    buffer += i
                else:
                    flag = False
            if i=='#':
                flag = True
        self.play_id = buffer[:-3]
        self.session_id = buffer[-3:]
        
    def parse_open(self,open_info_list):
        for info in open_info_list:
            if info[:4]=='Bodo':
                self.get_play_id(info)
                self.time = info[-19:]
            if match_str_slice(info,'[ME]'):
                print('my_info:',info)
                if info[:4]=='Seat':
                    self.my_seat_number = info[5]
                    start = False
                    chip_temp = ''
                    for i in info:
                        if start:
                            if i==' ':
                                start = False
                            else:
                                chip_temp += i
                        if i=='$':
                            start = True
                    self.mychips = float(chip_temp)
                            
    def parse_process(self,process_info_list):
        for info in process_info_list:
            if match_str_slice(info,'[ME]'):
                self.my_operation.append(info)
            if match_str_slice(info, 'FLOP'):
                self.flop = info[13:]
            if match_str_slice(info, 'TURN'):
                self.turn = info[13:]
            if match_str_slice(info, 'RIVE'):
                self.river = info[14:]
        self.myhands = self.my_operation[0][-8:-1]
        temp = ''
        for i in self.my_operation[0]:
            if i!='[':
                temp += i
            else:
                break
        self.my_role = temp[:-2]
        if self.flop=='':
            #river不为空，则看到了river，说明没有fold
            self.fold = True
        
        
    def parse_summary(self,summary_info_list):
        for info in summary_info_list:
            if match_str_slice(info,'[ME]'):
                print('my_info:',info)
            if match_str_slice(info, 'Seat+'+self.my_seat_number):
                self.my_result = info   
            if match_str_slice(info, 'Total Pot'):
                self.total_pot = info[-6:-1]
            
                     
    def show_in_cmd(self):
        print('flop:',self.flop)
        print('turn:',self.turn)
        print('river:',self.river)
        print('play_id:',self.play_id)
        print('play_time:',self.time)
        print('session_id:',self.session_id)
        print('my_seat_number:',self.my_seat_number)
        print('my_operation:',self.my_operation)
        print('my_role:',self.my_role)
        print('my_hands:',self.myhands)
        print('my_result:',self.my_result)
        print('total_pot:',self.total_pot)
        print('my_chips:',self.mychips)
        