import requests
import hashlib
# import time
import ocr_code

headers = {
    "Accept": "",
    "referer": "https://hifini.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Content-Type": "application/x-www-form-urlencoded",
    "DNT": "1"
}


def passwordHex(password):
    return hashlib.md5(password.encode("utf-8")).hexdigest()


class LoginWithName:
    __name = ''
    __pwd = ''
    __url = 'https://hifini.com/'
    __url_login = 'https://hifini.com/user-login.htm'
    __url_verify = 'https://hifini.com/vcode.htm'
    __state = False
    __session = None
    __cookies = {}
    __pwd_err = False

    def __init__(self, name, pwd):
        self.__name = name
        self.__pwd = passwordHex(pwd)
        self.__session = requests.session()
        self.__circulate()

    def __main(self):
        self.__session.get(url=self.__url, headers=headers)
        # time.sleep(0.5)
        self.__session.get(url=self.__url_login, params={"referer": 'https://hifini.com/user-login.htm',
                                                         'origin': 'https://hifini.com',
                                                         'x-requested-with': 'XMLHttpRequest'}, headers=headers)
        # time.sleep(0.5)
        img = self.__session.get(self.__url_verify, params={
            'referer': 'https://hifini.com/user-login.htm'
        }, headers=headers)
        vcode = ocr_code.GetVerifyCode(img.content).get()
        print('获取到验证码结果为：{}'.format(vcode))
        if vcode == -1:
            print('本次获取验证码失败')
            return
        # 若vcode为-1，则说明验证码识别出错，下面步骤无需再执行
        post_data = {
            'email': self.__name,
            'password': self.__pwd,
            'vcode': vcode
        }
        r = self.__session.post(url=self.__url_login,
                                params={"referer": 'https://hifini.com/user-login.htm',
                                        'origin': 'https://hifini.com',
                                        'x-requested-with': 'XMLHttpRequest'},
                                data=post_data, headers=headers)
        if '登录成功' in r.text:
            self.__state = True
            ck = self.__session.cookies
            keys = list(ck.keys())
            values = list(ck.values())
            # 构建cookies
            for i in range(0, len(keys)):
                self.__cookies[keys[i]] = values[i]
        else:
            str1 = '<i class="icon-ok"></i>'
            str2 = '</h4>'
            if str1 in r.text:
                err = r.text.split(str1)
                err = err[1].split(str2)[0].strip()
                print('账号密码登录出错，提示：{}。'.format(err))
                # 多次密码错误可能导致登录限制，所以发现密码错误后停止尝试
                if err == '密码错误':
                    self.__pwd_err = True
            else:
                print('账号密码登录出现未知错误')

    def __circulate(self):
        i = 0
        # 由于ocr识别的不确定性，所以最多循环5次
        while i < 6 and self.__state is False and not self.__pwd_err:
            self.__main()
            i += 1

    def get_state(self):
        return self.__state

    def get_cookies(self):
        return self.__cookies
