#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 作者：grant
import unittest
from common.common_func import Common
from common.my_unitest import StartEnd


class Testcases(StartEnd):
    '''
    '''

    def test_login(self):
        '''
        login
        '''
        Common.Login(self.driver)
        # self.assertEquals()



if __name__ == '__main__':
    unittest.main()
