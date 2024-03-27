import re  ##正则表达式

# from common.do_excel import DoExcel
# import constants
##用例依赖如何解决？ 使用re模块，使用正则查找并替换参数化数据
def replace(s,d): #s是要查找的字符串，d是要取值的字典
    p = "\$\{(.+?)}"  # 元字符与限定符  ()代表组
    while re.search(p,s) is not None:
        m = re.search(p,s)  # 在字符串excel_data里面匹配p
        r = m.group(1)  # 组  只有正则使用到()时才可以用group函数  1代表取一个组的匹配字符串，可以取多组2，3，4.....
        value = d[r]
        s = re.sub(p, value,s, count=1)  # p:正则表达式  value：要替换后的数据  excel_data 匹配的字符串
                                                  # count默认为0，替换全部  count=1指替换1组
    return s
    # l = re.findall(p,excel_data)   #查找全部，返回一个列表
    # print('查找全部，返回一个列表{}'.format(l))
    # value=datas[l[0]]
    # print(value)

datas = {'admin_phone': '15639986754', 'password': '123456'}
excel_data = '{"mobil_phone":"${admin_phone}","pwd":"${password}"}'
qq=replace(excel_data,datas)
print(qq)
# 1.如何利用python反射来解决不同测试方法之间数据的传递？
##同一个类或者module里面，不同方法之间的数据传递？  数据变量设置为全局变量  global
# class Nv:
#     global_var=0
#     def set_global_variable(self):
#         global global_var
#         global_var = 100
#     # 调用函数设置全局变量
#     set_global_variable(self=global_var)
#     def fff(self):
#         print(global_var)
# if __name__ == '__main__':
#     Nv().set_global_variable()
##如何解决多个module或者不同测试类之间的数据传递？
# class Woman:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def features(self):
#         print(self.name+'喜欢炒饭')
# setattr(Woman,'hobby','singing')   ##动态的给类或这类的实例化对象添加属性值   也可以动态的添加方法
# # getattr()   ##动态的获取类或这类的实例化对象的属性值
# # hasattr()   ##判断类或类的实例化对象中有没有当前属性值
# # delattr()   ##动态的删除类或类的实例化对象中的属性值
# if __name__ == '__main__':
#     print(getattr(Woman,'hobby'))
#     print(hasattr(Woman,'dh'))
#     print(delattr(Woman,'hobby'))
#     print(getattr(Woman,'hobby'))
