class WorldBank(object):   #将三个接口封装到类

    def __init__(self, lang = 'en', per_page = 50):
        self.lang = lang
        self.per_page = per_page

    def get_country(self, code='all', indicator='', **kwargs):
        pass

    def get_listcountry(self, code='all', indicator='', **kwargs):
        pass

    def get_detailcountry(self, code='all', indicator='', **kwargs):
        pass
