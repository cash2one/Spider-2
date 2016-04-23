import csv
from subjectClass import Subject


def isExistSubject(subjectObj_list,subject_name):
    for subjectObj in subjectObj_list:
        if subject_name == subjectObj.name:
            return True
    return False

def parse_csv(subjectObj_list):
    reader = csv.reader(open("output.csv"))
    cot = 0
    for row in reader:
        if cot>21735:
            break
        csv_subject_name = row[-2]
        csv_keyword = row[-1]
        print(csv_subject_name,csv_keyword,cot)
        if isExistSubject(subjectObj_list, csv_subject_name):
            for subjectObj in subjectObj_list:
                if csv_subject_name == subjectObj.name:
                    subjectObj.update_keyword(csv_keyword)
                    break
        else:
            new_subject_obj = Subject(csv_subject_name)
            subjectObj_list.append(new_subject_obj) 
        cot += 1    
        
'-------------main--------'        
subjectObj_list = []
first_subject_obj = Subject('fist_sample')
subjectObj_list.append(first_subject_obj)
parse_csv(subjectObj_list)
for subjectObj in subjectObj_list:
    subjectObj.get_max_keyword()
    subjectObj.show_result()