import requests
import json

default_url = "https://iknow-pic.cdn.bcebos.com/b151f8198618367a3d076ac228738bd4b31ce527"


# def get():
#     url = "https://acg.toubiec.cn/random.php?ret=json"
#     pic_url = default_url
#     try:
#         r = requests.get(url, timeout=2)
#         # 该网站不稳定，设置2秒超时
#         data = json.loads(r.text)
#         data = data[0]
#         # print(data)
#         if data["mes"] == "ok":
#             pic_url = data["imgurl"]
#             print("获取到图片url：{}".format(pic_url))
#     except Exception as e:
#         print("获取图片url出错")
#         print(e.__class__)
#         print(e.__str__())
#     return pic_url

def get():
    url = 'https://tuapi.eees.cc/api.php?category=fengjing&type=302&px=pc'
    pic_url = default_url
    try:
        r = requests.get(url)
        # 该网站不稳定，设置2秒超时
        if r.status_code == 200:
            pic_url = r.url
            print("获取到图片url：{}".format(pic_url))
    except Exception as e:
        print("获取图片url出错")
        print(e.__class__)
        print(e.__str__())
    return pic_url

# get()
# a = get()
# print(a)
