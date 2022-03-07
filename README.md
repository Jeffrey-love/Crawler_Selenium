---
categories:
  - 知识积累
author: JeffreyLove
copyright: true
date: '2022/3/4 11:00:00'
description: 一个神奇的爬虫程序
tags:
  - python
  - 爬虫
  - Selenium
---
# Crawler_Selenium  

### 使用selenium框架进行一个搜索操作  

并且配合Xpath输出搜索出来的所有动漫名（如果想要实现其它功能可以自行添加，我只是做一个演示如何将二者融合起来使用，从而能搭配出无限可能:kissing_heart:）    
这一次的代码使用的框架比较多，包含了各种功能，比如：  
- 模拟键盘操作
- 模拟鼠标点击等复杂操作
- 超时相应

使用这个框架之前有个前提，必须搭配ChromeDriver使用，而且其版本要与Chrome浏览器版本一致，为了避免Chrome自动跟新造成的困扰，所以可以使用Chromemium来进行实验，效果是一样的。  
[Chromemium下载地址](https://vikyd.github.io/download-chromium-history-version/#/)

下面一行代码的作用是先定位搜索框的位置，然后鼠标左击一次，随后模拟键盘输入柯南二字，睡眠一秒的作用是为了让使用者观察到，最后点击搜索按钮，这里搜索使用了xpath  
```python
# 单击搜索框，随后输入“柯南”,点击搜索（三次操作）
    action.move_by_offset(500,80).click().perform()
    action.send_keys("柯南").perform()
    time.sleep(1)
    # sousuo = driver.find_element_by_xpath("//button[@class='banner__btn']/span")这一条版本过时
    sousuo = driver.find_element(by=By.XPATH, value="//button[@class='banner__btn']/span")
    action.move_to_element(sousuo).click().perform()
```  
效果如下图：  
<img src="https://github.com/Jeffrey-love/Crawler_Selenium/blob/main/Pictures/1.jpg" width = "650" height = "400" alt="" align=center />    
另外，webdriver模块也有获取网页源码等等操作，例如  
`html_doc = driver.page_source`    

成功运行  
<img src="https://github.com/Jeffrey-love/Crawler_Selenium/blob/main/Pictures/2.jpg" width = "550" height = "400" alt="" align=center />    
爬虫的基本模块其实就这么些，至于更多要深入研究的是反爬虫，以及反反爬虫，Cookie、session的处理等。  

感谢阅读！文中若有错误欢迎各位大佬指出！
