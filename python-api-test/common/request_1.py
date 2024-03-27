import requests

class Request:
    def __init__(self):
        self.session=requests.sessions.session()  ##实例化一个session对象


    # def request(self,url,methob,data):
    #     self.session.request(url=url,method=methob,data=data)
