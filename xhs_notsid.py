import requests
import re
import sql
import hashlib
import random
import miproxy
import pprint
import json
import csv
import emoji
import time
import urllib.parse

class search_notes(object):
    def __init__(self):
        self.headers = {
            'Host':'www.xiaohongshu.com',
            'Content-Type':'application/json',
            'Accept':'*/*',
            'Accept-Language':'zh-cn',
            'Accept-Encoding':'gzip, deflate, br',
            'Connection':'keep-alive',
            'X-Sign':'',
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.12(0x17000c26) NetType/WIFI Language/zh_CN',
            # 'Device-Fingerprint':'WHJMrwNw1k/E3hW4woFdm+iP6Pr+de2PUr/aWwLwJ8zZc1aIKN8UjpRKj1zmuC4gXzT1n4PzGm/U94HEdBEAOMOdvzdYetZqfdCW1tldyDzmauSxIJm5Txg==1487582755342',
            # 'Authorization':'3bf8faaf-4607-44bb-9664-f59095d24950',
            'Referer':'https://servicewechat.com/wxffc08ac7df482a27/333/page-frame.html'
        }
        self.host ='http://www.xiaohongshu.com'
        self.url = '/fe_api/burdock/weixin/v2/search/notes?keyword={0}&sortBy=hot_desc&page={1}&pageSize=20&sid=session.1585025706938961885852'

    def sign(self, kw, page):
        x_sign = hashlib.md5((self.url.format(kw, page)+ 'WSUDD').encode(encoding='UTF-8')).hexdigest()
        # print(x_sign)
        return x_sign

    def search_id(self, kw, page):
        proxy = miproxy.get_proxy()
        proxies = {'https':proxy}
        print(proxies)
        self.headers['X-Sign'] = 'X' + str(self.sign(urllib.parse.quote(kw), page))
        url = self.host + self.url.format(kw, page)
        # s.keep_alive = False

        res = requests.get(url, headers = self.headers, proxies = proxies).text
        print(res)
        res = json.loads(res)
        return res


    def id2sql(self, res, kw):
        print(res)
        notes = res['data']['notes']
        for item in notes:
            note_id = item['id']
            title = emoji.demojize(item['title'])
            uid = item['user']['id']
            nickname = emoji.demojize(item['user']['nickname'])
            print(note_id, uid, kw)
            sql.insert_notes_id(note_id, uid, kw)
            with open('./notes_id.csv','a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([note_id, title, uid, nickname, kw])

if __name__ == '__main__':
    id_gen = search_notes()
    kws = ['夏士莲雪花', '凌仕','炫诗','凡士林','力士',
           '卫宝','多芬','旁氏','舒耐','夏士莲','清扬']
    with open('./notes_id.csv','a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['note_id', 'title', 'uid','nickname', 'kw'])
    for kw in kws:
        for page in range(1, 6):

            res = id_gen.search_id(kw, page)
            id_gen.id2sql(res, kw)
            time.sleep(3)






