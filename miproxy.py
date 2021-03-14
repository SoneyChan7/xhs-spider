import requests
from bs4 import BeautifulSoup

def get_proxy():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    url = 'http://gec.ip3366.net/api/?key=20200331104100642&getnum=1&area=1&order=1&proxytype=1'
    res = requests.get(url,headers = headers).text
    res = res.strip()

    return res

if __name__ == '__main__':
    proxy = get_proxy()
    proxies = {'https':proxy}
    res = requests.get('http://www.baidu.com/',proxies = proxies).text
    print(res)


