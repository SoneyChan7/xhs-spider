from __future__ import print_function
import requests
import sql
import emoji
import csv
import time

class get_note_content(object):
    def __init__(self):
        self.headers = {
            "Accept-Encoding": "gzip",
            "Connection": "close"
        }
        self.apikey = 'NtGi6shJ9JbchhYcud4yOqXpSgxVV83M5jOcHPIXm84J9AIWgosFy2UWLv3rVEhk'
        self.url = 'http://api01.idataapi.cn:8000/post/xiaohongshu_ids?id='
    def get_content(self):
        notes_ids = sql.get_note_id()
        # print(notes_ids)
        for item in notes_ids:
            attemps = 0
            success = False
            note_id = item['note_id']
            kw = item['kw']
            print()
            # print(notes_id)
            url = self.url + str(note_id) + '&apikey=' + self.apikey
            while attemps < 3 and not success:
                try:
                    res = requests.get(url, headers = self.headers, timeout = 2)
                    time.sleep(1)
                    # print(res.status_code)
                    res = res.json()
                    # print(res)
                    data = res['data'][0]
                    content = emoji.demojize(data['content'])
                    likes = data['likeCount']
                    share = data['shareCount']
                    star = data['favoriteCount']
                    comment = data['commentCount']
                    uid = data['posterId']
                    print(note_id, '录入')
                    sql.insert_notes_info(note_id, content, uid, likes, share, star, comment, kw)
                    with open('./notes_content.csv', 'a', newline='', encoding='utf-8') as f:
                        writer = csv.writer(f)
                        writer.writerow([note_id, content, uid, likes, share, star, comment, kw])
                    success = True
                except:
                    attemps += 1
                    if attemps == 3:
                        break

if __name__ == '__main__':
    with open('./notes_content.csv','a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['note_id', 'content', 'uid', 'likes', 'share', 'star', 'comment','kw'])
    content_gen = get_note_content()
    content_gen.get_content()





# http://api01.idataapi.cn:8000/post/xiaohongshu_ids?id=5a5f1ea9c8e55d32cbe96617&apikey=NtGi6shJ9JbchhYcud4yOqXpSgxVV83M5jOcHPIXm84J9AIWgosFy2UWLv3rVEhk

