#coding:utf-8
__author__ = 'Administrator'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from mytools.emailClass import Email
import time

class SeleniumWeiboCatch(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self,username,password):
        browser = self.driver
        browser.get("http://weibo.com/login.php")
        time.sleep(1)
        browser.maximize_window()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[1]/div/a[2]').click()
        username_input = browser.find_element_by_xpath('//*[@id="loginname"]')
        username_input.send_keys(username)
        password_input = browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        print('login success')


    def catch_info(self,userid):
        info = []
        browser = self.driver
        browser.get("http://weibo.com/u/"+ userid +"?is_all=1")
        weibo_list = browser.find_elements_by_class_name('WB_cardwrap')
        for weibo in weibo_list:
            content = weibo.find_elements_by_class_name('WB_text')
            if len(content)==1:
                info.append(self.parse_original_weibo(weibo))
            elif len(content)==2:
                info.append(self.parse_transmit_weibo(weibo))
            else:
                pass
        return info

    def parse_original_weibo(self,weiboEle):
        weibo_id = weiboEle.get_attribute('mid')
        content = weiboEle.find_element_by_class_name('WB_text').text
        #print weibo_id,content
        return content

    def parse_transmit_weibo(self,weiboEle):
        weibo_id = weiboEle.get_attribute('mid')
        content = weiboEle.find_elements_by_class_name('WB_text')[0].text
        #print weibo_id,content
        return content

    def send_mail(self,subject,content,log):
        local_time = time.strftime("%H:%M:%S  %Y-%m-%d",time.localtime(time.time()))
        emailAI = Email(
            receiver='965606089@qq.com',
            sender='luyangaini@vip.qq.com',
            host = 'smtp.qq.com',
            port = 587,
            subject=subject+local_time,
            content=content,
            logObj=log
        )
        emailAI.conn_server()
        emailAI.login(username='luyangaini@vip.qq.com',password='fcgiwomzdbkjbaij')
        emailAI.send()
        emailAI.close()

    def get_png(self,userID):
        local_time = time.strftime("%H:%M:%S  %Y-%m-%d",time.localtime(time.time()))
        self.driver.save_screenshot(local_time+".png")


    def tearDown(self):
        self.driver.close()