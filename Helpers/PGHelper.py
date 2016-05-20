
import postgresql
from Helpers import *


class PG:
    """
    PostgreSQL helper
    communicate with PostgreSQL database
    select, insert, update, delete operation
    """
    def __init__(self, config_path='../config.ini', section_name='postgresql'):
        """
        initialize PostgreSQL helper
        :param config_path: configuration file in which the database connection information stored
        :param section_name: section name in the configuration file where the db connection information stored
        :return: nothing
        """
        self.host = config[section_name]['host']
        self.port = config[section_name]['port']
        self.db = config[section_name]['db']
        self.user = config[section_name]['user']
        self.password = config[section_name]['password']
        self.connection = postgresql.open('pq://' + self.user + ':' + self.password + '@' + self.host + ':' +
                                          self.port + '/' + self.db)

    def prepare(self, sql):
        ps = self.connection.prepare(sql)
        return ps

    def save(self, entity=None, tbl_name=None):
        if entity is None or tbl_name is None:
            return -1
        sql = r'INSERT INTO ' + tbl_name + '('
        values = 'VALUES('
        columns = entity.keys()
        para_number = 1
        parameters = []
        for column in columns:
            if column in entity:
                parameters.append(entity[column])
            else:
                parameters.append(None)
            sql += str(column) + ','
            values += '$' + str(para_number) + ','
            para_number += 1
        parameters = tuple(parameters)
        values = values.rstrip(',') + ')'
        sql = sql.rstrip(',') + ') ' + values
        print(sql)
        print(parameters)
        ps = self.connection.prepare(sql)
        rs = ps(*parameters)
        return rs

    def load(self, entities=None, tbl_name=None):
        for entity in entities:
            print(entity)

        ps = self.connection.prepare('')

# pg = PG()
# pp = pg.prepare('select * FROM CRAWL.TEST')
# print(pp())


# insert_test = pg.statement('INSERT INTO CRAWL.TEST VALUES($1, $2)')
# persons = [{'name': 'Alice', 'role': 'AA'}, {'name': 'Bob', 'role': 'AA'}, {'name': 'Cindy', 'role': 'AA'}]
# for person in persons:
#     insert_test(person['name'], person['role'])
# pp = pg.statement('select * FROM CRAWL.TEST')
# print(pp())
