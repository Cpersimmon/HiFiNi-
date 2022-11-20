import wxpush
import hifini
import time
import statistics
import logging
# import get_cookies
import resoulve_config
import time_order

# 云函数下无法统计运行次数
statistics_or_not = False
# 配置文件路径
path = 'data\\config.json'
# 登录方式
login_type = 0


def get_variable_cookies(rc):
    global login_type
    cookies = rc.get_cookies()
    # 若直接获取到的cookies可用
    if hifini.HiFiNi(cookies).getName() != '':
        login_type = 1
        print("本次使用cookies登录")
        return cookies
    else:
        # 2022.9.8 该方法已失效，网站更改了验证方法
        # # 直接获取到的cookies不可用
        # print("cookies登录失败，本次将使用账号密码登录")
        # name = rc.get_name()
        # pwd = rc.get_password()
        # if pwd == '' or name == '':
        #     logging.error('未获取到账号和密码，程序无法运行')
        #     return {}
        # gck = get_cookies.LoginWithName(name, pwd)
        # if gck.get_state():
        #     login_type = 2
        #     return gck.get_cookies()
        # 账号密码有误
        return {}


def main_handler(event, content):
    print('开始运行时间为{}'.format(time.strftime("%H:%M:%S", time.localtime())))
    # 程序开始计时
    start = time.time()
    # 实验性功能：先尝试cookies登录，若失败，则切换到账号密码登录
    rc = resoulve_config.GetConfig(path)
    # 企业微信推送id
    corpid = rc.get_corpid()
    secret = rc.get_secret()
    agentid = rc.get_agentid()
    # 至此
    m1 = time.time()
    print('△读取config.json耗时{:.2f}秒'.format(m1 - start))
    # 尝试获取有用的cookies，并开始第一次登录
    cookies = get_variable_cookies(rc)
    if cookies != {}:
        # 该cookies可用
        hifi = hifini.HiFiNi(cookies)
        # 等到23:59:59再开始签到
        t0 = -1
        while time_order.if_time_in(50, 59):
            time.sleep(0.001)
            # 打印倒计时信息
            t1 = time_order.only_second()
            if t1 != t0:
                print('倒计时:{}'.format(t1))
                t0 = t1
        print('退出倒计时，现在时间为{}'.format(time.strftime("%H:%M:%S", time.localtime())))
        # 至此
        # 暂停1.01秒
        if time_order.only_second() == 59:
            time.sleep(1.5)
            print('主动暂停程序1.5秒')
            # print('开始正式签到，现在时间为{}'.format(time.strftime("%H:%M:%S", time.localtime())))
        # 避免倒计时对统计时间的影响
        m1 = time.time()
        code, msg = hifi.signIn()
    else:
        logging.error('通过账号密码获取cookies出错，运行终止')
        wxpush.Wxpush(result=-1, name='null', email='null', group='null',
                      jinbi='-1', desp='账号密码有误，或者出现其他错误',
                      corpid=corpid, secret=secret, agentid=agentid).push()
        return

    # 至此
    # 登录耗时提醒
    m2 = time.time()
    print('△登录并初次尝试签到耗时{:.2f}秒'.format(m2 - m1))

    # 重复开始签到
    for i in range(1,6):
        time.sleep(0.5)# 每次间隔0.5s
        if code == 1:
            # 签到成功
            if hifi.ifSignInOrNot() == 0:
                # 还没签到，即签到是昨天的
                code, msg = hifi.signIn()
            else:
                # 今天已经签到成功了
                break
        elif code==-1:
            # 签到失败，再尝试签一次
            code, msg = hifi.signIn()
            print('第{}次尝试签到'.format(i+1))
        else:
            # 重复签到，退出循环
            break
    # 签到耗时提醒
    m3 = time.time()
    print('△再次尝试签到耗时{:.2f}秒，其中主动暂停了0.5秒'.format(m3 - m2))
    # 企业微信推送数据准备。
    # 注意，由于server酱超过5条收费且详情需点进去查看，因此强烈建议使用企业微信推送
    name = hifi.getName()
    email = hifi.getEmail()
    group = hifi.getGroup()
    jinbi = hifi.getJinbi()
    wp = wxpush.Wxpush(result=code, name=name, email=email, group=group,
                       jinbi=jinbi, desp=msg, corpid=corpid, secret=secret, agentid=agentid)
    wp.set_login_type(login_type)
    # 设置登录方式提醒
    wp.push()
    # 至此
    # 推送耗时提醒
    m4 = time.time()
    print('△推送耗时{:.2f}秒'.format(m4 - m3))
    # 实验性功能，统计运行次数，只在本地运行时开启
    if statistics_or_not:
        print('本次统计运行次数', end='')
        try:
            t1 = statistics.Sta()
            if code == -1 or code == 0:
                t1.count(False)
            else:
                t1.count(True)
            #
        except Exception as e:
            logging.error("统计出错")
            logging.error(e.__class__.__str__)
            logging.error(e.__str__)
        # 统计耗时提醒
        m5 = time.time()
        print('△统计耗时{:.2f}秒'.format(m5 - m4))
    end = time.time()
    print('△本次运行耗时{:.2f}秒'.format(end - start))
    print('现在的时间是{}'.format(time.strftime("%H:%M:%S", time.localtime())))
    print('运行完毕')


if __name__ == '__main__':
    statistics_or_not = True
    # 在非云函数环境下运行，开启统计功能
    main_handler(None, None)
