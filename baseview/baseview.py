#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 作者：grant

import os
import datetime
from pathlib import Path
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from common.desired_caps import logging
import sys
import inspect
import uiautomator2 as u2

class BaseView(object):

    def __init__(self, driver):
        self.driver = driver

    def get_current_function_name(self):
        # return inspect.stack()[2][4],inspect.stack()[2][2]
        return inspect.stack()[2][1:5]
        # return inspect.stack()

    def wait_element_click(self, time, *element):
        try:
            WebDriverWait(self.driver, time).until(lambda x: x.find_element(*element))
        except TimeoutException:
            self.photo("方法%s().第%s行.%s"%(sys._getframe().f_back.f_code.co_name,
                                            str(sys._getframe().f_back.f_lineno),
                                            sys._getframe().f_code.co_name))
            logging.info("error"+str(self.get_current_function_name()))
        except NoSuchElementException:
            self.photo("方法%s().第%s行.%s"%(sys._getframe().f_back.f_code.co_name,
                                            str(sys._getframe().f_back.f_lineno),
                                            sys._getframe().f_code.co_name))
            logging.info("error"+str(self.get_current_function_name()))
        else:
            self.find_element(*element).click()


    def wait_elements_click(self, time, num, *element):
        try:
            WebDriverWait(self.driver, time).until(lambda x: x.find_element(*element))

        except TimeoutException:
            self.photo("方法%s().第%s行.%s"%(sys._getframe().f_back.f_code.co_name,
                                            str(sys._getframe().f_back.f_lineno),
                                            sys._getframe().f_code.co_name))
            logging.info("error"+str(self.get_current_function_name()))
        except NoSuchElementException:
            self.photo("方法%s().第%s行.%s"%(sys._getframe().f_back.f_code.co_name,
                                            str(sys._getframe().f_back.f_lineno),
                                            sys._getframe().f_code.co_name))
            logging.info("error"+str(self.get_current_function_name()))
        else:
            self.driver.find_elements(*element)[num].click()


    def wait_element_sendkeys(self, time, text, *element):
        try:
            WebDriverWait(self.driver, time).until(lambda x: x.find_element(*element))
        except TimeoutException:
            self.photo("方法%s().第%s行.%s"%(sys._getframe().f_back.f_code.co_name,
                                            str(sys._getframe().f_back.f_lineno),
                                            sys._getframe().f_code.co_name))
            logging.info("error" + str(self.get_current_function_name()))
        except NoSuchElementException:
            self.photo("方法%s().第%s行.%s"%(sys._getframe().f_back.f_code.co_name,
                                            str(sys._getframe().f_back.f_lineno),
                                            sys._getframe().f_code.co_name))
            logging.info("error"+str(self.get_current_function_name()))
        else:
            self.find_element(*element).clear().send_keys(text)

    def wait_element(self, time=10, *element):
        return WebDriverWait(self.driver, time).until(lambda x: x.find_element(*element))


    def photo(self, dir_name):
        def getpath():
            path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'screenshot_Ubox', dir_name)
            return path
        if Path(getpath()).is_dir():  # 判断文件夹路径是否已经存在
            pass
        else:
            Path(getpath()).mkdir()  # 如果不存在，创建文件夹

        self.driver.save_screenshot(getpath() + '\\' + self.time() + '.png')

    def time(self):
        time = datetime.datetime.now().strftime('%Y%m%d_%H-%M-%S')
        return time

    def get_name(self, name):
        return self.driver.find_element_by_name(name)


    def find_element(self, *loc):
        return self.driver.find_element(*loc)


    def find_elements(self, *loc):
            return self.driver.find_elements(*loc)


    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(self, start_x, start_y, end_x, end_y, duration)

    def get_elenment_count(self,*element):
        count = 0
        while (count >= 0):
            try:
                self.driver.find_elements(*element)[count]
            except:
                break
            else:
                count = count + 1
        logging.info('检测到' + str(count) + '个元素')
        return count

    # 向下滑动
    def swipe_down(self, t=500, n=1):
        s = self.driver.get_window_size()
        logging.info("swipe-down")
        x1 = s['width'] * 0.5  # x坐标
        y1 = s['height'] * 0.25  # 起点y坐标
        y2 = s['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    #想上滑动
    def swipe_up(self, t=2000, n=1):
        s = self.driver.get_window_size()
        logging.info("swipe-up")
        x1 = s['width'] * 0.34  # 起点x坐标
        y1 = s['height'] * 0.84  # 起点y坐标
        y2 = s['height'] * 0.099075  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)


