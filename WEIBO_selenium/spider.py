#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,csv,sys
from selenium.webdriver.support.select import Select
from MyDatabaseClass import MyDatabase

class CatchSchoolName:
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.data = []
        
    def login(self,username,password):
        browser = self.driver
        browser.get("http://weibo.com/login.php")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="pl_login_form"]/div[2]/div[1]/div/a[2]').click()
        username_input = browser.find_element_by_xpath('//*[@id="loginname"]')
        username_input.send_keys(username)
        password_input = browser.find_element_by_xpath('//*[@id="pl_login_form"]/div[2]/div[3]/div[2]/div/input')
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        print('login success')
        
    def enter_school_page(self):
        browser = self.driver
        time.sleep(1)
        browser.get("http://account.weibo.com/set/index")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="pl_personalInfo_education"]/ul/li[3]/a').click()
        time.sleep(1)       
        browser.find_element_by_xpath('//*[@id="pl_personalInfo_education"]/div/div/div/div[1]/a').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="pl_personalInfo_education"]/div/div/div/div/div/div[1]/div[2]/div[3]/input').click()
        time.sleep(1)
        print('enter page success')

    def select_to_catch_info(self,file):
        browser = self.driver
        school_kind_select = browser.find_element_by_xpath("/html/body/div[5]/div/table/tbody/tr/td/div/div[2]/div[1]/div[1]/div[2]/select")
        school_S = Select(school_kind_select)
        province_select = browser.find_element_by_xpath("/html/body/div[5]/div/table/tbody/tr/td/div/div[2]/div[1]/div[2]/div[2]/select[1]")
        prov_S = Select(province_select)
        city_select = browser.find_element_by_xpath('/html/body/div[5]/div/table/tbody/tr/td/div/div[2]/div[1]/div[2]/div[2]/select[2]')
        city_S = Select(city_select)
        
        school_kind_select.click()
        school_S.select_by_index(1)#只选大学
        i = 0
        while(1):
            time.sleep(1)
            province_select.click()
            try:
                prov_S.select_by_index(i)
            except:
                break
            option_list = city_select.find_elements_by_tag_name('option')
            city_list = []
            for opt in option_list:
                index = opt.get_attribute('value')
                city = opt.text
                city_list.append({'city_name':city,'index':index})
            j = 0
            while(2):
                time.sleep(0.5)
                city_select.click()
                try:
                    city_S.select_by_visible_text(city_list[j]['city_name'])
                except:
                    break
                info = self.get_info_in_school_container(browser)
                info = info.encode("utf-8")
                print(info)
                city = city_list[j]['city_name'].encode("utf-8")
                file.write( '---'+ city +'\n' + info + '\n')
                self.data.append((0,info))
                j += 1
            i += 1
    
            
    def get_info_in_school_container(self,browser):
        info = browser.find_element_by_xpath('/html/body/div[5]/div/table/tbody/tr/td/div/div[2]/div[2]/div[2]').text
        return info

    def tearDown(self):
        self.driver.close() 
        
        
def save_to_db(db,data):
    city_name = data['city_name']
    print('city_name',city_name,len(city_name))
    db.cur.execute('select id from sp_cities where title = %s',(city_name))
    city = db.cur.fetchall()
    if not city:
        return
    city_id = -1
    print(city)
    for i in city:
        for j in i:
            city_id = j
    print(city_id)
    for i in data['school_list']:
        school_name = i
        db.cur.execute(
            "insert into base_seniorhighschool(city_id,school_name)"
            "values (%s,%s)",
            (city_id,school_name)
        )
        db.conn.commit()
            
def parse_txt(file,db):
    dict = { 'city_name':'' , 'school_list':[]   }
    pre_city_name = '合肥'
    while(1):
        line = file.readline()
        if not line:
            break
        if line[0]=='-':
            print('city:'+pre_city_name)
            for i in dict['school_list'][:3 ]:
                print(i)
            if pre_city_name[-1:]=='\n':
                pre_city_name = pre_city_name[:-1]
            if pre_city_name[-3:]=='xe5\x8c\xba':
                pre_city_name = pre_city_name[:-3]
            data = {'city_name':pre_city_name,'school_list':dict['school_list']}
            save_to_db(db,data)
            pre_city_name = dict['city_name']
            dict['city_name'] = line[3:]
            dict['school_list'] = []
        else:
            dict['school_list'].append(line)
        
        
        
if __name__ == "__main__":
    '''
    spider = CatchSchoolName()
    spider.login('15262057539','kidlin')
    spider.enter_school_page()
    '''
    db = MyDatabase(host='localhost',user='root',passwd='',db='findmentor',port=3306,charset='utf8')
    file = open('record.txt','r')
    #spider.select_to_catch_info(file)
    db.conn.commit()
    parse_txt(file,db)
    file.close()