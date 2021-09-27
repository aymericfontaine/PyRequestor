import configparser

class Ini:
    __fichier = 'ini.ini'

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(Ini.__fichier)
        
        self.db = IniDB(config['DB'])
        self.table = IniTable(config['TABLE'])


class IniDB:
    def __init__(self, config):
        self.label = config['LABEL']
        self.user = config['USER']
        self.password = config['PASSWORD']
        self.host = config['HOST']
        self.database = config['DATABASE']
        self.type = config['TYPE']


class IniTable:
    def __init__(self, config):
        self.request = config['REQUEST']
        self.requestparam = config['REQUEST_PARAM']

