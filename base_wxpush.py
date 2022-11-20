import requests
import json
import logging
import get_pictures


class WxPush:
    __corpid = ""
    __secret = ""
    __agentid = ""

    def __init__(self, corpid, secret, agentid):
        self.__corpid = corpid
        self.__secret = secret
        self.__agentid = agentid

    def __get_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        value = {
            'corpid': self.__corpid,
            'corpsecret': self.__secret
        }
        response = (requests.get(url, params=value)).json()
        token = response['access_token']
        return token

    def push_text(self, msg):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + self.__get_token()
        value = self.__construct_text(msg)
        r = requests.post(url=url, data=json.dumps(value))
        result = json.loads(r.text)
        if not result["errcode"] == 0:
            print(result)
            logging.error("企业微信推送失败")
        else:
            print("企业微信推送成功")

    def __construct_text(self, msg):
        values = {
            "touser": '@all',
            "toparty": "",
            "totag": "",
            "msgtype": "text",
            "agentid": self.__agentid,
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800,
            "text": {"content": msg}
        }
        return values

    def push_news(self, msg, title, pic_url_enable=True, pic_url=None, jump_url=None):
        # 默认随机图片，不填写跳转网址
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + self.__get_token()
        value = self.__construct_news(msg=msg, title=title,
                                      pic_url_enable=pic_url_enable, pic_url=pic_url, jump_url=jump_url)
        r = requests.post(url=url, data=json.dumps(value))
        result = json.loads(r.text)
        if not result["errcode"] == 0:
            print(result)
            logging.error("企业微信推送失败")
        else:
            print("企业微信推送成功")

    def __construct_news(self, msg, title, pic_url_enable, pic_url, jump_url):
        value = {
            "touser": '@all',
            "msgtype": "news",
            "agentid": self.__agentid,
            "news": {
                "articles": [
                    {
                        "title": title,
                        "description": msg,
                        "url": jump_url,
                        # "picurl": "https://iknow-pic.cdn.bcebos.com/b151f8198618367a3d076ac228738bd4b31ce527"
                        "picurl": pic_url
                    }
                ]
            }

        }
        if pic_url_enable:
            if pic_url is None:
                value["news"]["articles"][0]["picurl"] = get_pictures.get()
        else:
            del value["news"]["articles"][0]["picurl"]
        if jump_url is None:
            del value["news"]["articles"][0]["url"]
        return value

# wp = WxPush("", "", "")
# s = wp.construct_news(msg="123", title="标题", pic_url_enable=True, pic_url="pu", jump_url="123")
# print(s)
