import requests
import urllib3
urllib3.disable_warnings()
from selenium import webdriver
import sql
driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://www.xiaohongshu.com/discovery/item/5ab4c71cb538bf3b7b7f4a92')
html = driver.page_source
print(html)




