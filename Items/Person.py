
from Items.Entity import Entity


class Person(Entity):

    def keys(self):
        return ['NAME', 'ALIAS', 'ENGLISHNAME', 'GENDER', 'BIRTHDAY', 'AGE', 'HOMETOWN', 'TAG', 'AUDITUSER',
                'AUDITDATE', 'CREATOR', 'CREATEDATE', 'LASTMODIFYDATE', 'MODIFIER', 'SOURCEURL']
