import pymysql
#先安装pymysql模块   pip install pymysql
#1.建立与数据库的链接
host='127.0.0.1'  ##数据库地址
user='root'  ##链接数据库的用户名
password='123456' ##密码
port=3306  #端口号
# database='TestOa'  #选择要操作的数据库
mysql=pymysql.connect(host=host, user=user, password=password, port=port)
##2. 新建一个查询页面
cursor=mysql.cursor()
##3.编写sql
sql='select * from javamall.es_member where member_id=1'
##4.执行sql
cursor.execute(sql)
##5.查看结果
# result=cursor.fetchmany(size=2)   #返回结果是一个元组  ,size=2指返回前两行数据
result=cursor.fetchone() #只返回一个数据
# result=cursor.fetchone() #返回全部数据
print(result)
##6.关闭查询页面
cursor.close()
##7.关闭数据库链接
mysql.close()


