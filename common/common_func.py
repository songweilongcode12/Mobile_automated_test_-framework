# coding:utf-8
from baseview.baseview import BaseView
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
from time import sleep
import json



class Common(BaseView):
    '''
    public testcase
    '''
    with open('../Config/caps.json', 'rb') as file:
        data = json.load(file)
        username = data['login_msg'][0]['uesrname']
        pwd = data['login_msg'][0]['password']
        user_name = ''
        password = ''
        LoginButun = ''
    # @data(*testData)
    def Login(self, Usename = username, Password = pwd):
        logging.info("登录的账号是:"+Usename+ "=====登录密码是："+ Password)
        self.wait_element_sendkeys(5,Usename,*self.user_name)
        self.wait_element_sendkeys(5,Password,*self.password)
        try:
            self.wait_element_click(5, *self.LoginButun)
            sleep(8)
        except:
            logging.info('登录失败')
            self.photo('登录失败')
        else:
            logging.info('登录成功')
            self.photo('登录成功')
        self.GetLoginStatus()




