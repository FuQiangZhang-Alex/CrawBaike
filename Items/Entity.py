
class Entity(dict):
    """
    get class name
    :return name of this class
    """
    @classmethod
    def name(cls):
        return cls.__name__

    def __getitem__(self, item):
        return self.get(item, None)

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
        pass

    def save(self, db_helper=None, tbl_name=None):
        """
        save person entity into specified database
        :param db_helper: db helper instance used to write person entity into specified database
        :param tbl_name: full quanlified table name
        :return: True if success else False
        """
        status = db_helper(entity=self, tbl_name=tbl_name)
        if status:
            return True
        else:
            return False

    def delete(self, db_helper=None, tbl_name=None):
        pass
