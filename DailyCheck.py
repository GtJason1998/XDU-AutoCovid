import requests
import json
import sys

class DailyCheck:
    def __init__(self, username, password):
        loginData = {}
        loginData['username'] = username
        loginData['password'] = password
        self.loginData = loginData

    def login(self):
        loginUrl = 'https://xxcapp.xidian.edu.cn/uc/wap/login/check'
        loginHeaders = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Content-Length': '39',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'DNT': '1',
            'Host': 'xxcapp.xidian.edu.cn',
            'Origin': 'https://xxcapp.xidian.edu.cn',
            'Referer': 'https://xxcapp.xidian.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fxxcapp.xidian.edu.cn%2Fsite%2Fncov%2Fxidiandailyup',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
            'X-Requested-With': 'XMLHttpRequest'
        }
        session = requests.Session()
        response = session.post(url = loginUrl, headers = loginHeaders, data = self.loginData)
        loginResult = json.loads(response.text)
        if loginResult['m'] != '操作成功':
            print('密码错误!!! 请检查填报的学号和密码')
            exit(0)
        else:
            self.session = session
            return self
        
    def post(self):
        postUrl = 'https://xxcapp.xidian.edu.cn/xisuncov/wap/open-report/save'
        postHeaders = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Content-Length': '2028',
            'Content-Type': 'application/x-www-form-urlencoded',
            'DNT': '1',
            'Host': 'xxcapp.xidian.edu.cn',
            'Origin': 'https://xxcapp.xidian.edu.cn',
            'Referer': 'https://xxcapp.xidian.edu.cn/site/ncov/xidiandailyup',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
            'X-Requested-With': 'XMLHttpRequest'
        }
        postData = {
            'sfzx': '1',  # 是否在校
            'tw': '1',    # 体温
            'area': '陕西省 西安市 雁塔区',  # 地区
            'city': '西安市',               # 城市
            'province': '陕西省',           # 省份
            'address': '陕西省西安市雁塔区电子城街道西安电子科技大学新科技楼西安电子科技大学北校区',    # 地址
            'geo_api_info': '{"type":"complete","position":{"Q":34.230272081164,"R":108.91732259114599,"lng":108.917323,"lat":34.230272},"location_type":"html5","message":"Get ipLocation failed.Get geolocation success.Convert Success.Get address success.","accuracy":149,"isConverted":true,"status":1,"addressComponent":{"citycode":"029","adcode":"610113","businessAreas":[],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"太白南路","streetNumber":"2号","country":"中国","province":"陕西省","city":"西安市","district":"雁塔区","township":"电子城街道"},"formattedAddress":"陕西省西安市雁塔区电子城街道西安电子科技大学新科技楼西安电子科技大学北校区","roads":[],"crosses":[],"pois":[],"info":"SUCCESS"}', # 地理位置API
            'sfcyglq': '0',  # 是否处于隔离器
            'sfyzz': '0',    # 是否有症状
            'qtqk': '',      # 其他情况
            'ymtys': '0'     # 一码通颜色
        }
        response = self.session.post(url = postUrl, headers = postHeaders, data = postData)
        result = json.loads(response.text)
        print(result['m'])

parameters = sys.argv
DailyCheck(parameters[1], parameters[2]).login().post()