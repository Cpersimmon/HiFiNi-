def get():
    headers = {
        "accept - encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "sec - ch - ua - platform": "\"Windows\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76",
        "Content-Type": "application/x-www-form-urlencoded",
        "DNT": "1",
        # "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Microsoft Edge\";v=\"97\", \"Chromium\";v=\"97\""
    }
    return headers
    # print(headers)
    # if req_type == "get":
    #     return requests.get(url=url, headers=headers, cookies=cookies)
    # else:
    #     return requests.post(url=url, headers=headers, cookies=cookies)

# r = req("https://www.hifini.com/my.htm", cookies1)
# if "cpersimmon@163.com" in r.text:
#     print("cookies成功")
