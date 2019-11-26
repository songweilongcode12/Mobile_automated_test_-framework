#!/usr/bin/python
# -*- coding:utf-8 -*-

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# from setting_updata_handpwd import setting_updata_handpwd
from common.desired_caps import appium_desired
import unittest
import time,logging
import warnings
from common import common_func

class StartEnd(unittest.TestCase):

    def setUp(self):
        logging.info("=====start test=====")
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = appium_desired()
    def tearDown(self):
        logging.info('====tearDown====')
        time.sleep(2)
        self.driver.close_app()

