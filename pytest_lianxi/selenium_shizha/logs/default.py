import logging
from pytest_lianxi.selenium_shizha.conf.confs import Configs

class Mylogs:


    def __init__(self):
        cfg = Configs()
        self.myloger = logging.getLogger('default.log')
        # myloger.setLevel('DEBUG')
        self.myloger.setLevel(cfg.base_envir()[0])

        formater = logging.Formatter(cfg.base_envir()[1])

        file = logging.FileHandler('default.log', encoding='utf-8')
        file.setLevel('DEBUG')
        file.setFormatter(formater)

        self.myloger.addHandler(file)


    def logs(self,level='DEBUG',msg=None):
        if level=='DEBUG':
            self.myloger.debug(msg)
        elif level=='INFO':
            self.myloger.info(msg)
        elif level=='WARNING':
            self.myloger.warning(msg)
        elif level=='ERROR':
            self.myloger.error(msg)
        else:
            self.myloger.critical(msg)

if __name__ == '__main__':
    Mylogs().logs('ERROR',msg='jfhfshjk')

