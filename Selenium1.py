#! /user/bin.python
# -*- coding:UTF-8 -*-
import time
# import random
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains #模拟复杂操作
from selenium.webdriver.common.keys import Keys     #键盘
from selenium.webdriver.support.ui import WebDriverWait     #超时相应操作
from lxml import etree

# proxy = '58.20.234.243:9091'

def title(html_doc):
    html = etree.HTML(html_doc)
    name = html.xpath("//p[@class='u-tt']/text()")
    for item in name:
        print(item)

def sele():
    # 指定调用某个地方的Chrome
    options = webdriver.ChromeOptions()
    # Chrome浏览器的主程序位置  @这里用chromemium是为了防止版本自动更新使程序失效
    location = r"C:\pythonProject\python\pachong\chrome-win\chrome.exe"
    # 在options增加读取位置
    options.binary_location = location
    '''
    使用代理
    options.add_argument('--proxy-server=http://'+proxy)
    options.add_argument('--proxy-server=%s'%'http://58.20.234.243:9091') #这种方法也有效
    '''
    # 之前的executable_path被重构到了Service函数里，所以不加这一条会报错
    s = Service(r"C:\pythonProject\python\pachong\chromedriver.exe")
    chrome = webdriver.Chrome(service=s, options=options)
    driver = chrome
    driver.set_page_load_timeout(5)
    # 使用get方法打开一个网站
    driver.get("http://www.4399dmw.com/search/dh-9-0-0-0-0-0-0/")

    action = ActionChains(driver)
    # 单击搜索框，随后输入“柯南”,点击搜索（三次操作）
    action.move_by_offset(500,80).click().perform()
    action.send_keys("柯南").perform()
    time.sleep(1)
    # sousuo = driver.find_element_by_xpath("//button[@class='banner__btn']/span")这一条版本过时
    sousuo = driver.find_element(by=By.XPATH, value="//button[@class='banner__btn']/span")
    action.move_to_element(sousuo).click().perform()

    # 获取网页源代码
    html_doc = driver.page_source
    title(html_doc)

    time.sleep(10)
    driver.quit()

def main():
    try:
        sele()
    except:
        print("加载页面超时")

if __name__ == '__main__':
    main()