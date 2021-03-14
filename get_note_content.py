import requests
import miproxy
import hashlib
import urllib3
urllib3.disable_warnings()

class get_content(object):
    def __init__(self):
        self.headers = {
            'Host': 'www.xiaohongshu.com',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'X-Sign': '',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.12(0x17000c26) NetType/WIFI Language/zh_CN',
            # 'Device-Fingerprint':'WHJMrwNw1k/E3hW4woFdm+iP6Pr+de2PUr/aWwLwJ8zZc1aIKN8UjpRKj1zmuC4gXzT1n4PzGm/U94HEdBEAOMOdvzdYetZqfdCW1tldyDzmauSxIJm5Txg==1487582755342',
            'Authorization':'3bf8faaf-4607-44bb-9664-f59095d24950',
            'Referer': 'https://servicewechat.com/wxffc08ac7df482a27/334/page-frame.html'
        }
        self.host = 'https://www.xiaohongshu.com'
        self.url = '/fe_api/burdock/weixin/v2/note/{0}/single_feed?sid=session.1585025706938961885852'
    def sign(self, note_id):
        x_sign = hashlib.md5((self.url.format(note_id)+ 'WSUDD').encode(encoding='UTF-8')).hexdigest()
        print(x_sign)
        return x_sign

    def get_note_details(self, note_id):
        proxy = miproxy.get_proxy()
        print(proxy)
        proxies = {'https':proxy}
        self.headers['X-Sign'] = 'X' + str(self.sign(note_id))
        print(self.headers['X-Sign'])
        url = self.host + self.url.format(note_id)
        print(url)
        res = requests.get(url, verify = False).text
        print(res)

if __name__ == '__main__':
    details_gen = get_content()
    details_gen.get_note_details('5ad85cce910cf6724f51bba4')

# https://www.xiaohongshu.com/fe_api/burdock/weixin/v2/note/5ad85cce910cf6724f51bba4/single_feed?sid=session.1585025706938961885852
# https://www.xiaohongshu.com/fe_api/burdock/weixin/v2/note/5ad85cce910cf6724f51bba4/single_feed?sid=session.1585025706938961885852