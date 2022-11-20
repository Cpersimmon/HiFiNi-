import json
import os
import logging
import time


class Sta:
    base_path = "statistics"
    file = "log.json"
    max_size = 3

    def __init__(self):
        self.exit_check()
        self.size_check()
        self.check_today()

    def exit_check(self):
        if not os.path.exists(self.base_path):
            os.mkdir(self.base_path)
        path = os.path.join(self.base_path, self.file)
        if not os.path.exists(path) or not os.path.isfile(path):
            content = {
                "总次数": 0,
                "成功次数": 0,
                "失败次数": 0,
                "详情": {}
            }
            self.__write(content)

    def __write(self, content):
        msg = json.dumps(content)
        path = os.path.join(self.base_path, self.file)
        try:
            with open(path, 'w') as f:
                f.seek(0)
                f.write(msg)
        except Exception as e:
            logging.error("写入文件出错")
            logging.error(e.__class__.__name__)
            logging.error(e.__str__())

    def __read(self):
        path = os.path.join(self.base_path, self.file)
        try:
            with open(path, 'r') as f:
                f.seek(0)
                con = json.loads(f.read())
                return con
        except Exception as e:
            logging.error("读取文件出错")
            logging.error(e.__class__.__name__)
            logging.error(e.__str__())

    def reset(self):
        # 将文件重置为初始状态
        if not os.path.exists(self.base_path):
            os.mkdir(self.base_path)
        path = os.path.join(self.base_path, self.file)
        if not os.path.exists(path):
            os.remove(path)
        content = {
            "总次数": 0,
            "成功次数": 0,
            "失败次数": 0,
            "详情": {}
        }
        self.__write(content)

    def check_today(self):
        # 检查今天有没有加进去
        origin = self.__read()
        t = time.strftime("%Y-%m-%d", time.localtime()).__str__()
        # t = "2022-02-01"
        try:
            origin["详情"][t]
        except KeyError:
            origin["详情"].update({t: 0})
            self.__write(origin)

    def size_check(self):
        # 检查文件大小是否超过阈值并修正
        try:
            origin = self.__read()
            if len(origin["详情"]) > self.max_size:
                tk = list(origin["详情"].keys())[0]
                del origin["详情"][tk]
                self.__write(origin)
                if len(origin["详情"]) > self.max_size:
                    self.size_check()
        except Exception as e:
            logging.error("size_check出错")
            logging.error(e.__class__.__name__)
            logging.error(e.__str__())

    def count(self, state=True):
        # 记录今天的结果
        origin = self.__read()
        origin["总次数"] += 1
        t = time.strftime("%Y-%m-%d", time.localtime()).__str__()
        origin["详情"][t] += 1
        if state:
            origin["成功次数"] += 1
            print(origin["成功次数"])
        else:
            origin["失败次数"] += 1
            print()
        self.__write(origin)

    def get_all(self):
        # 获取总的执行情况
        data = self.__read()
        return data['总次数'], data["成功次数"], data["失败次数"]

    def get_today(self):
        # 获取今天执行次数
        data = self.__read()
        t = time.strftime("%Y-%m-%d", time.localtime()).__str__()
        return data['详情'][t]


# c = Sta()
# # c.reset()
# c.count()
# text = c.read()
# print(text)
# print(c.get_all())
# # c.reset()
