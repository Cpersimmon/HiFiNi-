import requests

url_home = "https://music.163.com"
url_dailyTask = "http://interface3.music.163.com/eapi/point/dailyTask"
url_msg='http://mam.netease.com/api/v1/getconfig'
cookies = {
    'buildver': '1561972804',
    'resolution': '2158x1080',
    'liteversioncode': '1',
    'osver': '10',
    'deviceId': 'bnVsbAkwMjowMDowMDowMDowMDowMAk5YzlmN2RhMzY1ZDk2M2VkCXVua25vd24%3D',
    'appver': '6.2.4',
    'liteappver': '1.0.0',
    'MUSIC_U': 'e358cc9187d186b818c305ff2d7cb02aaeed15242a3be053211c313db3889fe533a649814e309366',
    'ntes_kaola_ad': '1',
    'apptype': 'lite',
    '__csrf': 'ea24862fe132f93769010f8451752c6f',
    'NMTID': '00O1LSzGVDn2zsRm03bsWSRfVSr0vEAAAF1mLPWPA',
    'versioncode': '146',
    'mobilename': 'MI8SE',
    'os': 'android',
    'channel': 'google'
}
headers = {
    'User-Agent': 'NeteaseMusic/6.2.4(146);NeteaseMusicLite/1.0.0.1561972804(1);Dalvik/2.1.0 (Linux; U; Android 10; '
                  'MI 8 SE MIUI/V12.5.1.0.QEBCNXM)',
    'Host': 'interface3.music.163.com'
}
params = "04F1A0AB8150EFD085BC839891D19E2E488A2D6C2924C5589260A62E82B1A0D37AECDCBFE49300E20BB3185109C797F8891A7596B2CD0DC5A51F68C95C3448E1ECA1140D7D60B22CC73D9ECF513560E9937188730433751F3B684FEA12A761E19C2C759599D1044A00B460A476643B3AA51F90E9A86FB83894B66E6D6BE3614E3621FE168F004E82F5A9551380E4B64CC7F2FCEDD973E2E58F9ECC0D8FA9BFCD2DE9197D67545CAC957207545EF7A820825AA8BC2B662128C21E54A8C5A6E90E28AEC83A16D860833EF1B19B3D1386467B7580431B827FA09412ECC24023EAF09AB3127671C83D673378EDBC3A75EF956069BED7E8E7DE6B8309A9A28892A04E568C7CB0E6126C7D691AC03108CAF1BC296E8DDCF17258BC973FECCBBD304062F3DF75B7250069591103A8A2692F708611EBD64EB7AFA60921402B9402E5D6047F90F1858F79377AECBDEDEA11C7F284F6622309A7F02A6A04364DC1D6D084A7DA9D33DA17C7C4800E70DE465588B269A2102E01198ED9E4AAACA3F8434425FF "


def main():
    # print("1")
    r = requests.post(url_msg, headers=headers, cookies=cookies)
    print(r.status_code)
    print(r.text)


if __name__ == '__main__':
    main()
