#coding:utf-8
def stripWithParamString(string_origin,strip_string):
    #原字符串功能函数strip可以褪去某字母，现以某字符串的形式褪去（形参变化）
    temp_string = string_origin
    for char in strip_string:
        temp_string = temp_string.strip(char)
    filter_string = temp_string
    return filter_string
        
def match_str_slice(origin_str,match_str):
    matching = False
    origin_index = 0
    match_index = 0
    for ele in origin_str:
        if match_index==len(match_str):
            return True
        if matching:
            if ele==match_str[match_index]:
                match_index += 1
            else:
                matching = False
        if ele==match_str[0]:
            matching = True
            match_index = 1
        origin_index += 1
    return False