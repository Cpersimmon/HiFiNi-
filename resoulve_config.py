import os
import json
import platform


class GetConfig:
    __path_file = ''
    __name = ''
    __pwd = ''
    __cookies = {}
    __corpid = ''
    __secret = ''
    __agentid = ''

    def __init__(self, path):
        self.__path_file = path
        # 若在linux下运行
        if platform.system() == 'Linux':
            print("正在linux下运行")
            self.__path_file = self.__path_file.replace('\\', '/')
            base = os.path.abspath(os.path.dirname(__file__))
            self.__path_file = os.path.join(base, self.__path_file)
        # 至此
        print('在{}目录下读取配置文件'.format(self.__path_file))
        self.__main()

    def __main(self):
        c_file = self.__path_file
        if os.path.exists(c_file) and os.path.isfile(c_file):
            try:
                with open(c_file, 'r') as f:
                    f.seek(0)
                    cf = json.loads(f.read())
                    self.__name = cf['name']
                    self.__pwd = cf['password']
                    self.__cookies = cf['cookies']
                    self.__corpid = cf['corpid']
                    self.__secret = cf['secret']
                    self.__agentid = cf['agentid']
            except Exception as e:
                print('解析config出错')
                print(e.__class__)
                print(e.__str__())
        else:
            print('似乎不存在config.json')

    def get_name(self):
        return self.__name

    def get_password(self):
        return self.__pwd

    def get_cookies(self):
        return self.__cookies

    def get_corpid(self):
        return self.__corpid

    def get_secret(self):
        return self.__secret

    def get_agentid(self):
        return self.__agentid
