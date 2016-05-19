
from Helpers.PGHelper import PG


class Person(dict):
    # override dict
    def __init__(self):
        pass

    def __str__(self):
        _str = ''
        for key in self.keys():
            if key in self:
                s = str(key) + ': ' + str(self[key]) + '\n'
                _str += s
            else:
                s = str(key) + ': Not Exits\n'
                _str += s
        return _str

    def keys(self):
        return ['NAME', 'ALIAS', 'ENGLISHNAME', 'GENDER', 'BIRTHDAY', 'AGE', 'HOMETOWN', 'TAG', 'AUDITUSER',
                'AUDITDATE', 'CREATOR', 'CREATEDATE', 'LASTMODIFYDATE', 'MODIFIER', 'SOURCEURL']

    def save(self, db_helper=None):
        """
        save person entity into specified database
        :param db_helper: db helper instance used to write person entity into specified database
        :return: True if success else False
        """
        db_helper(entity=self, tbl_name='CRAWL.PERSON')

    def test(self, db_helper=None):
        db_helper(entity=self, tbl_name='CRAWL.PERSON')
