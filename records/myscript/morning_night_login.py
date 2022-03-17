import requests


class Morning_punch:
    """晨午晚检"""
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def run(self):
        try:
            headers = {
                'user-agent': '#',
            }
            login_url = 'https://xxcapp.xidian.edu.cn/uc/wap/login/check'
            url = 'https://xxcapp.xidian.edu.cn/xisuncov/wap/open-report/save'
            session = requests.session()
            login_data = {
                'username': self.username,
                'password': self.password,
            }
            session.post(url=login_url, data=login_data, headers=headers)

            data = {
                'sfzx': '1',
                'tw': '1',
                'area': '陕西省 西安市 长安区',
                'city': '西安市',
                'province': '陕西省',
                'address': '陕西省西安市长安区韦曲街道学而思培优(西长安街校区)',
                'geo_api_info': '{"type":"complete","position":{"Q":34.158996853299,"R":108.90904676649399,"lng":108.909047,"lat":34.158997},"location_type":"html5","message":"Get ipLocation failed.Get geolocation success.Convert Success.Get address success.","accuracy":8094.548535841807,"isConverted":true,"status":1,"addressComponent":{"citycode":"029","adcode":"610116","businessAreas":[{"name":"韦曲","id":"610116","location":{"Q":34.162202,"R":108.93736899999999,"lng":108.937369,"lat":34.162202}}],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"西长安街","streetNumber":"599号","country":"中国","province":"陕西省","city":"西安市","district":"长安区","towncode":"610116001000","township":"韦曲街道"},"formattedAddress":"陕西省西安市长安区韦曲街道学而思培优(西长安街校区)","roads":[],"crosses":[],"pois":[],"info":"SUCCESS"}',
                'sfcyglq': '0',
                'sfyzz': '0',
                'qtqk': '',
                'ymtys': '0',
            }
            res_data = session.post(url=url, data=data).json()
            return res_data['m']
        except:
            return '失败'


if __name__ == '__main__':
    demo = Morning_punch('', '')
    print(demo.run())
