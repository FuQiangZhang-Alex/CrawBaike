
import postgresql
from Helpers import *


class PG:
    """
    PostgreSQL helper
    communicate with PostgreSQL database
    execute select, insert, update, delete operation(s)
    """
    def __init__(self, section_name='postgresql'):
        """
        initialize PostgreSQL helper
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
        """
        prepare a statement based on the input sql statement
        :param sql: sql statement
        :return: a Statement object which is callable
        """
        ps = self.connection.prepare(sql)
        return ps

    def execute(self, sql=None, parameters=None):
        """
        execute specified sql
        :param sql: sql statement
        :param parameters: sql parameter(s)
        :return: status of the execution
        """
        if sql is None:
            return False
        ps = self.prepare(sql)
        rs = False
        if parameters:
            parameters = tuple(parameters)
            rs = ps(*parameters)
        else:
            rs = ps()
        if rs:
            return True
        else:
            return False

    def save(self, entity=None, tbl_name=None):
        """
        save an entity into database
        :param entity: entity to save
        :param tbl_name: table name associate with the entity
        :return: execution results list
        """
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
        ps = self.connection.prepare(sql)
        rs = ps(*parameters)
        return rs

    def load(self, entities=None, tbl_name=None):
        """
        load entities into database
        :param entities: entities to load
        :param tbl_name: table name associate with these entities
        :return: execution results list
        """
        for entity in entities:
            print(entity)

        ps = self.connection.prepare('')
