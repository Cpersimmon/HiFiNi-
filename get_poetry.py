import json
import requests
import random
import logging


def get():
    try:
        url = __get_poetry_url()
        r = requests.get(url)
        s = json.loads(r.text)
        # print(s['content']+'\n'+'\t\t\t——'+s['author']+'（'+s['origin']+')')
        return s['content'] + '\t\t——' + s['author'] + '《' + s['origin'] + '》'
    except Exception as e:
        static_poetry = "人面不知何处去，桃花依旧笑春风。    ——崔护《题都城南庄》"
        logging.error(e.__class__.__name__)
        logging.error(e.__str__())
        return static_poetry


def __get_poetry_url():
    url = "https://v1.jinrishici.com/"
    r = requests.get(url)
    data = json.loads(r.text)
    long = len(data['list'])
    i = random.randint(0, long - 1)
    return list(data['list'][i].values())[0]

# print(get_poetry())
# r = requests.get("https://baidu.com")
# print(r.text)
