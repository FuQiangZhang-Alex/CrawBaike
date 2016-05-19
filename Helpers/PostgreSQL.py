
import postgresql


apilevel = '1.0'
threadsafety = 0
paramstyle = ''


def connect(self, user=None, password=None, host=None, port=None, db_name=None):
    if None in [user, password, host, port, db_name]:
        return None
    else:
        return postgresql.open()
    pass


class Connection:
    def __init__(self):
        pass

    def close(self):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass

    def cursor(self):
        pass


class Cursor:
    description = ('name', 'type_code')
    rowcount = 0

    def __init__(self):
        pass

    def close(self):
        pass

    def execute(self, operation, parameters=None):
        pass

    def executemany(self, operation, seq_of_parameters):
        pass

    def fetchone(self):
        pass

    def fetchmany(self, size):
        pass

    def fetchall(self):
        pass

    def nextset(self):
        pass

    def arraysize(self):
        pass

    def setinputsizes(self):
        pass

    def setoutputsize(self):
        pass
