import configparser
import os
from pytest_lianxi.selenium_shizha.contents import base_path


class Configs:

    def base_envir(self):
        self.config=configparser.ConfigParser()
        self.config.read(os.path.join(base_path.conf_paths,'confs.conf'),encoding='utf-8')
        envir=self.config.get('environment','envir')
        if envir == 'uat':
            return self.uat()
        else:
            return self.sit()

    def uat(self):
        self.config.read(os.path.join(base_path.conf_paths,'uat-conf.conf'), encoding='utf-8')
        level= self.config.get('logs','level')
        formater=self.config.get('logs','formater')
        return (level,formater)

    def sit(self):
        self.config.read(os.path.join(base_path.conf_paths,'sit-conf.conf'),encoding='utf-8')
        level = self.config.get('logs', 'level')
        formater = self.config.get('logs', 'formater')
        return (level,formater)


if __name__ == '__main__':
    print(Configs().base_envir())