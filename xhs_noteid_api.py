from __future__ import print_function
import requests
import sql
import re
import emoji
import csv
class get_notes_id_api(object):
    def __init__(self):
        self.url = 'http://api01.idataapi.cn:8000/post/xiaohongshu?apikey=NtGi6shJ9JbchhYcud4yOqXpSgxVV83M5jOcHPIXm84J9AIWgosFy2UWLv3rVEhk&sort=popularity_descending&kw='
        self.headers = {
            "Accept-Encoding": "gzip",
            "Connection": "close"
        }
    def get_info(self, kw, page):
        url = self.url + kw + '&pageToken={0}'.format(page)

        r = requests.get(url , headers=self.headers)
        json_obj = r.json()
        data = json_obj['data']
        for item in data:
            note_id = item['id']
            title = emoji.demojize(item['description'])
            uid = item['uid']
            print('note_id:{0}, title:{1}, uid:{2}'.format(note_id, title, uid))
            sql.insert_notes_id(note_id, uid, kw)
            with open('./notes_id.csv', 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([note_id, title, uid, kw])


if __name__ == '__main__':
    kwlist = ['炫诗','凡士林','力士','卫宝','多芬','旁氏','舒耐','清扬']
    with open('./notes_id.csv','a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['note_id', 'title', 'uid', 'kw'])
    for keyword in kwlist:
        pagetokens = [i for i in range(1, 51)]
        notes_generator = get_notes_id_api()
        for page in pagetokens:
            attemps = 0
            success = False
            while attemps < 3 and not success:
                try:
                    notes_generator.get_info(keyword,page)
                    success = True
                except:
                    attemps += 1
                    if attemps == 3:
                        break



