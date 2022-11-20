import requests
import logging
import get_headers
import time


class HiFiNi:
    SIGN_IN_URL = "https://www.hifini.com/sg_sign.htm"
    MY_URL = "https://www.hifini.com/my.htm"
    HOME_URL = "https://www.hifini.com"
    post_data = {"x-requested-with": "XMLHttpRequest"}
    cookies = {}
    __name = ''
    __email = ''
    __group = ''

    def __init__(self, cookies):
        self.cookies = cookies

    def __updateUserInformation(self):
        str1 = "<span class=\"hidden-lg\">"
        str2 = "Email：</span>"
        str3 = "<span class=\"text-muted\">用户组：</span>"
        r = requests.get(url=self.MY_URL, data=self.post_data, headers=get_headers.get(), cookies=self.cookies)
        if r.ok:
            txt = r.text
            if str1 in txt:
                n = txt.split(str1)
                n = n[1].split("</span>")
                self.__name = n[0]
                # 获取name
                e = txt.split(str2)
                e = e[1].split("\n")
                self.__email = e[0].strip()
                # 获取email
                u = txt.split(str3)
                u = u[1].split("<br>")
                self.__group = u[0].strip()

    def getName(self):
        if self.__name == '':
            self.__updateUserInformation()
        return self.__name

    def getEmail(self):
        if self.__email == '':
            self.__updateUserInformation()
        return self.__email

    def getGroup(self):
        if self.__group == '':
            self.__updateUserInformation()
        return self.__group

    def signIn(self):
        r = requests.post(url=self.SIGN_IN_URL, data=self.post_data, headers=get_headers.get(), cookies=self.cookies)
        if r.ok:
            txt = r.text
            for line in txt.splitlines():
                if "今天已经签过" in line:
                    logging.debug("今天已经签过")
                    return 0, line.strip()
                if "成功签到" in line:
                    # print(line)
                    logging.debug("成功签到")
                    print('签到时间为{}'.format(time.strftime("%H:%M:%S", time.localtime())))
                    return 1, line.strip()
            # print('可能签到失败')
            logging.error("登录失败，检查cookie是否错误或者失效")
            return -1, "登录失败，检查cookie是否错误或者失效"
        logging.error("未知原因失败")
        return -1, "未知原因失败"

    def getJinbi(self):
        str1 = "font-style: normal;font-weight: bolder;\">"
        r = requests.post(url=self.MY_URL, data=self.post_data, headers=get_headers.get(), cookies=self.cookies)
        if r.ok:
            txt = r.text
            if str1 in txt:
                n = txt.split(str1)
                n = n[1].split("</em>")
                return n[0]
        # 注意，返回的是字符，不是数字
        return '-1'

    def ifSignInOrNot(self):
        str1 = "已签"
        str2 = "请登录后查看"
        r = requests.post(url=self.HOME_URL, data=self.post_data, headers=get_headers.get(), cookies=self.cookies)
        if r.ok:
            txt = r.text
            if str1 in txt:
                # 已经签到过
                return 1
            elif str2 in txt:
                # 登录失败
                return -1
            else:
                # 没有签到
                return 0
        else:
            # 出错了
            return -1
