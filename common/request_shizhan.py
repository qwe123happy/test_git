from common.do_excel import DoExcel
from ddt import ddt,data
import unittest
from common import constants
from common.request_1 import Request
from common import config_class
from common.mysql import DoMysql




@ddt
class TestCase(unittest.TestCase):
    '这是一个测试类'
    ##方法一: 利用初始化函数和超继承 来实例化一个session对象
    # def __init__(self,methodName):
    #     super(TestCase,self).__init__(methodName)   #超继承，继承TestCase中的属性
    #     self.session= requests.session() # 实例一个session对象,使用 Session 对象发送请求时，所有请求都将共享相同的会话信息（例如 Cookie、认证等）
    ##方法二：
    @classmethod   #类方法，在每个类执行前执行一次
    def setUpClass(cls):
        cls.request=Request()# 实例一个session对象,使用 Session 对象发送请求时，所有请求都将共享相同的会话信息（例如 Cookie、认证等）

    login_data = DoExcel(constants.datas_path).read('Sheet')  ##此处对表单名做了参数处理，好处是可以在一个测试类里，添加多个表单测试多个接口
    # regition_data = DoExcel(r'..\datas\test.xlsx').read('Sheet2')
    # regition_data = DoExcel(constants.datas_path).read('Sheet')  ##此处对文件路径做出优化
    def setUp(self):
        self.t = DoExcel(constants.datas_path)
        # self.t=DoExcel(r'..\datas\test.xlsx', 'Sheet')




    @data(*login_data)
    def test_testcase(self,safer):
        # #用例一  正常登录
        # datas={'username':'陈彬','pwd':'123456!'}  #请求参数
        # resp = session.request('post','www.baidu.com',data=datas) ##发起请求，并用变量resp接收响应信息
        # print(resp.text)  ##打印响应信息
        #
        # #用例二  密码错误登录
        # datas={'username':'陈彬','pwd':'1234111!'}  #请求参数
        # resp = session.request('post','www.baidu.com',data=datas) ##发起请求，并用变量resp接收响应信息
        # print(resp.text)  ##打印响应信息

        # 用例三   参数化设置 从excel中取值
        datas=eval(safer.datas) #请求参数
        mysql_test=DoMysql() ##引用数据库类，作用:1.可以用数据库中的数据做测试用例的参数化 2.可以验证测试用例执行结束后，数据库中结果是否与预期一致
        result_phone=mysql_test.select('select email from javamall.es_member where member_id=9')[0]
        datas['phone']=result_phone

        new_url=config_class.url+safer.url   ##拼接url路径，url的部分路径配置化，后半部分取值excel
        print(new_url)
        try:
            if safer.method=='post':  ##判断请求方式是get还是post
                # resp = self.session.request(safer.method,safer.url,data=datas)  ##方法一对应写法
                # resp = requests.post(new_url) ##发起请求，并用变量resp接收响应信息   访问百度，域名访问只有一个url
                resp = self.request.session.request(safer.method,new_url)  ##方法二对应写法
                expected=safer.expected
                print(resp.text)  ##打印响应信息
                self.assertEqual(expected,resp.text)
                Testresult = 'pass'
            # else:
            #     resp = self.session.request(safer.method, safer.url, params=datas)
            #     # resp = requests.post(safer.url) ##发起请求，并用变量resp接收响应信息   访问百度，域名访问只有一个url
            #     expected = safer.expected
            #     print(resp.text)  ##打印响应信息
            #     self.assertEqual(expected, resp.text)
            #     Testresult = 'pass'
        except AssertionError as e:
            print('断言错误，与预期结果不符{}'.format(e))
            Testresult = 'failed'
            raise e
        finally:
            self.t.input_data(safer.case_id+1,7,value=resp.text,sheetname='Sheet')
            self.t.input_data(safer.case_id+1,8,value=Testresult,sheetname='Sheet')

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()   ##关闭实例对象






# if __name__ == '__main__':
#     TestCase('test_testcase').test_testcase()
