#coding:utf-8
from TexasPokerClass import *
from stringHandleByMyself import match_str_slice
import csv
from funcs import *

seat_get_cot_dict = {
        1:      0,
        2:      0,
        3:      0,
        4:      0,
        5:      0,
        6:      0,
        }

seat_fold_cot_dict  = {
        1:      0,
        2:      0,
        3:      0,
        4:      0,
        5:      0,
        6:      0,
        }

global total_play_cot
total_play_cot = 0

def parse_txt(bodog_hand_txt,file_route):
    element_str = ''
    play_cot = 0
    chip_trend = []
    for line in bodog_hand_txt:
        if line[:4] != 'Bodo':
            element_str += ( line + '\n' )
        else:
            pokerObj = TexasPoker(element_str)
            play_cot += 1
            pokerObj.main_parse()
            seat_get_cot_dict[role_index(pokerObj.my_role)] += 1
            if match_str_slice(pokerObj.my_result, 'before'):
                #没到翻后数量
                seat_fold_cot_dict[role_index(pokerObj.my_role)] += 1
            #pokerObj.show_in_cmd()
            chip_trend.append(pokerObj.mychips)
            element_str = ''
            element_str += line
            print("----------")
    print(chip_trend)
    if play_cot>100:
        show_in_matplot(chip_trend,file_route[:-4]+'.png')
    file_name = file_route[:-4] + 'chip_trend.csv'
    csvfile = file(file_name, 'wb')
    writer = csv.writer(csvfile)
    writer.writerow(['chips'])
    for row in chip_trend:
        writer.writerow([row])
    global total_play_cot
    total_play_cot += play_cot
'''
file_route = 'HH20160421-220253 - 544924 - ZONE - $0.02-$0.05 - HOLDEMZonePoker - NL - ZonePoker No.661.txt'
file_route = 'hand_history/' + file_route
bodog_hand_txt = open(file_route,'r')
parse_txt(bodog_hand_txt,file_route)
for i in range(1,7): 
    temp = int(seat_fold_cot_dict[i]*1.0/seat_get_cot_dict[i]*1000)
    temp *= 0.001
    print(seat_dict[i],seat_fold_cot_dict[i],seat_get_cot_dict[i],temp)
print('total_play_cot:',total_play_cot)
'''
#------------main-----------------

rootdir = 'Q:\Spider\BodogAnalyse\src\hand_history'
file_route_list = get_file_list(rootdir)
print(file_route_list)
for file_route in file_route_list:
    file_route = 'hand_history/' + file_route
    bodog_hand_txt = open(file_route,'r')
    parse_txt(bodog_hand_txt,file_route)
    for i in range(1,7): 
        temp = int(seat_fold_cot_dict[i]*1.0/seat_get_cot_dict[i]*1000)
        temp *= 0.001
        print(seat_dict[i],seat_fold_cot_dict[i],seat_get_cot_dict[i],temp)
    print('total_play_cot:',total_play_cot)