#ԭ�ַ������ܺ���strip������ȥĳ��ĸ������ĳ�ַ�������ʽ��ȥ���βα仯��
def stripWithParamString(string_origin,strip_string):
    temp_string = string_origin
    for char in strip_string:
        temp_string = temp_string.strip(char)
    filter_string = temp_string
    return filter_string
        