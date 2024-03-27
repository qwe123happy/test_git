import pymysql
class DoMysql:

    def __init__(self):
        host='127.0.0.1'
        user='root'
        password='123456'
        port=3306
        self.mysql=pymysql.connect(host=host, user=user, password=password, port=port)
        cursor = self.mysql.cursor()
        cursor.execute("ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456'")
        cursor.close()
        self.cursor=self.mysql.cursor()


    def select(self,sql):
       self.cursor.execute(sql)
       result=self.cursor.fetchone()   ##fetchone 只查看一个
       return result

    def insert(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result

    def updata(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result

    def delete(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result

    def close(self):
        self.cursor.close()
        self.mysql.close()

