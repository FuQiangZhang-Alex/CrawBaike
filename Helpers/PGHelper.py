
import postgresql
from .. import *


class PG:
    """
    PostgreSQL helper
    communicate with PostgreSQL database
    execute select, insert, update, delete operation(s)
    """
    def __init__(self):
        """
        initialize PostgreSQL helper
        :param section_name: section name in the configuration file where the db connection information stored
        :return: nothing
        """
        self.host = CONFIGURATION[CONFIG_SECTION_PG]['host']
        self.port = CONFIGURATION[CONFIG_SECTION_PG]['port']
        self.db = CONFIGURATION[CONFIG_SECTION_PG]['db']
        self.user = CONFIGURATION[CONFIG_SECTION_PG]['user']
        self.password = CONFIGURATION[CONFIG_SECTION_PG]['password']
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

    def save_entity(self, entity=None, tbl_name=None):
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
        para_number = 1
        parameters = []
        for key in entity.keys():
            parameters.append(entity[key])
            sql += str(key) + ','
            values += '$' + str(para_number) + ','
            para_number += 1
        parameters = tuple(parameters)
        values = values.rstrip(',') + ')'
        sql = sql.rstrip(',') + ') ' + values
        ps = self.connection.prepare(sql)
        rs = ps(*parameters)
        return rs

    def load_entities(self, entities=None, tbl_name=None):
        """
        load entities into database
        :param entities: entities to load
        :param tbl_name: table name associate with these entities
        :return: execution results list
        """
        for entity in entities:
            print(entity)

        ps = self.connection.prepare('')
