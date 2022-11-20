import ddddocr2
import logging


class GetVerifyCode:
    __img = None
    __ocr = None

    def __init__(self, img):
        self.__img = img
        self.__ocr = ddddocr2.DdddOcr()

    def get(self):
        try:
            res = self.__ocr.classification(self.__img)
            print('初次识别到验证码是：{}'.format(res))
            vcode = int(res[0]) + int(res[2])
            return vcode
        except Exception as e:
            logging.error("识别ocr出错")
            logging.error(e.__class__)
            logging.error(e.__str__())
            return -1
