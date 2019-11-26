#coding:utf-8
from appium import webdriver
# import yaml
import logging
import logging.config
import os
import json

CON_LOG = '../config/log.conf' #../表示上一级目录
logging.config.fileConfig(CON_LOG)
logging =logging.getLogger()

def appium_desired(port=4223):
    logging.info("准备启动APP")
    # deviceName = os.popen('adb shell getprop ro.product.model').read().strip()
    platformVersion = os.popen('adb shell getprop ro.build.version.release').read().strip()
    # device = os.popen('adb shell getprop ro.product.name ').read().strip()
    adb_device = os.popen('adb devices ').read().strip()
    a = adb_device.find('attached', 0, len(adb_device)) + 9
    b = adb_device.find('device', a, len(adb_device)) - 1
    udid = adb_device[a:b].strip()
    logging.info('版本号:' + platformVersion)
    logging.info('UDID:' + udid)
    with open('../Config/caps.json','rb') as file:
        data = json.load(file)
        print(data)
    app_path = os.path.dirname(os.path.dirname(__file__)) #查询当前文件所属目录的上一级目录路径
    app_dir=os.path.join(app_path,'Appbakage',data['devices_msg'][0]['appname'])
    desired_caps = {}
    desired_caps['platformName'] = data['devices_msg'][0]['platformName']
    desired_caps['platformVersion'] = data['devices_msg'][0]['platformVersion']
    desired_caps['deviceName'] = data['devices_msg'][0]['deviceName']
    # desired_caps['appname'] = data['devices_msg'][0]['appname']
    desired_caps['noReset'] = data['devices_msg'][0]['noReset']
    desired_caps['unicodeKeyboard'] = data['devices_msg'][0]['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['devices_msg'][0]['resetKeyboard']
    desired_caps['appPackage'] = data['devices_msg'][0]['appPackage']
    desired_caps['appActivity'] = data['devices_msg'][0]['appActivity']
    desired_caps['uiautomator'] = data['devices_msg'][0]['uiautomator']
    desired_caps['ip'] = data['devices_msg'][0]['ip']
    desired_caps['port'] = data['devices_msg'][0]['port']
    desired_caps['autoGrantPermissions'] = data['devices_msg'][0]['autoGrantPermissions']
    desired_caps['chromedriverExecutable'] = data['devices_msg'][0]['chromedriverExecutable']
    desired_caps['app'] = app_dir
    if platformVersion >= str(8):
        desired_caps['automationName'] = data['devices_msg'][0]['uiautomator2']
        logging.info('本次使用UI2')

    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(port)+'/wd/hub',desired_caps)
    driver.implicitly_wait(8)
    return driver

# def appium_desired_wework(port=4725):
#     logging.info("准备启动APP")
#     # deviceName = os.popen('adb shell getprop ro.product.model').read().strip()
#     platformVersion = os.popen('adb shell getprop ro.build.version.release').read().strip()
#     # device = os.popen('adb shell getprop ro.product.name ').read().strip()
#     adb_device = os.popen('adb devices ').read().strip()
#     a = adb_device.find('attached', 0, len(adb_device)) + 9
#     b = adb_device.find('device', a, len(adb_device)) - 1
#     udid = adb_device[a:b].strip()
#     logging.info('版本号:' + platformVersion)
#     logging.info('UDID:' + udid)
#
#     #读入yaml配置文件
#     with open('../Config/caps.json', 'rb') as file1:
#         data = json.load(file1)
#         print(data)
#     app_path = os.path.dirname(os.path.dirname(__file__)) #查询当前文件所属目录的上一级目录路径
#     app_dir=os.path.join(app_path,'Appbakage',data['appname'])
#     desired_caps = {}
#     desired_caps["chromedriverExecutable"] = "C:\\Users\\liling\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\appium-chromedriver\\chromedriver\\win\\chromedriver.exe"
#     desired_caps['chromeAndroidPackage']='com.tencent.wework'
#     # desired_caps['recreateChromeDriverSessions'] = True
#     desired_caps['platformName'] = data['platformName']
#     desired_caps['platformVersion'] = platformVersion
#     desired_caps['deviceName'] = udid
#     desired_caps['app'] = app_dir
#     desired_caps['appPackage'] = 'com.tencent.wework'
#     desired_caps['appActivity'] = 'com.tencent.wework.launch.LaunchSplashActivity'   #aapt dump badging xxxx.apk | find "launchable-activity"
#
#     desired_caps['noReset'] = data['noReset']
#     desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
#     desired_caps['resetKeyboard'] = data['resetKeyboard']
#     desired_caps['autoGrantPermissions'] = data['autoGrantPermissions'] # 处理安卓系统弹窗，自动管理授权
#     if platformVersion >= str(8):
#         desired_caps['automationName'] = data['uiautomator2']
#         logging.info('本次使用UI2')
#
#     driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(port)+'/wd/hub',desired_caps)
#     driver.implicitly_wait(8)
#     return driver

def install_packages():
    package_name = os.system('adb shell pm list packages |  grep com.mbox.cn ')
    app_version = os.system('adb shell dumpsys package com.mbox.cn |grep  versionName')
    print(package_name)
    print(app_version)
    if package_name != 'package:com.mbox.cn' and app_version == 'versionName=2.8.4':
        os.system('adb install -r "../app-packages/youzhihui_sc1.apk"')
    else:
        logging.info('该app已经安装')


# install_packages()
