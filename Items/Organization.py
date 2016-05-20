
from Items.Entity import Entity


class Organization(Entity):

    def keys(self):
        return ['ORGANIZATIONNAME', 'ALIAS', 'TYPEID', 'REGLOC', 'REGDATE', 'ENDDATE', 'TAG', 'IPOCODE', 'IPODATE',
                'REMARK', 'CREATOR', 'CREATEDATE', 'LASTMODIFYDATE', 'MODIFIER', 'AUDITUSER', 'AUDITDATE']
