import base_wxpush
import get_poetry


class Wxpush:
    __name = ''
    __email = ''
    __group = ''
    __jinbi = ''
    __result = -1
    __desp = ''
    __corpid = ''
    __secret = ''
    __agentid = ''
    __login_type = 0

    def __init__(self, result, name, email, group, jinbi, desp, corpid, secret, agentid):
        self.__result = result
        self.__name = name
        self.__email = email
        self.__group = group
        self.__jinbi = jinbi
        self.__desp = desp
        self.__corpid = corpid
        self.__secret = secret
        self.__agentid = agentid

    def __construct(self):
        if self.__result == 1:
            t = "成功签到"
        elif self.__result == -1:
            t = "签到失败"
        else:
            t = "重复签到"
        z = "任务结果：" + t
        a = "用户名：" + self.__name
        b = "email：" + self.__email
        c = "用户组：" + self.__group
        d = "金币数目：" + self.__jinbi
        e = "任务详情："
        f = self.__desp
        g = "今日诗词：\n\t" + get_poetry.get()
        # 登录方式提示，若login_type为0，则不输出登录信息
        log = ''
        if self.__login_type == 1:
            log = '登录方式：cookies\n'
        elif self.__login_type == 2:
            log = '登录方式：账号及密码\n'
        # 至此

        msg = z + '\n' + log + a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n\t' + f + '\n' + g
        return msg

    def push(self):
        bwp = base_wxpush.WxPush(corpid=self.__corpid, secret=self.__secret, agentid=self.__agentid)
        msg = self.__construct()
        #
        print('本推送详情长度为{}字节'.format(len(msg.encode('utf8'))))
        #
        title = "HiFiNi签到"
        url = "https://hifini.com/my.htm"
        bwp.push_news(msg=msg, title=title, jump_url=url)

    def set_login_type(self, login_type):
        self.__login_type = login_type
