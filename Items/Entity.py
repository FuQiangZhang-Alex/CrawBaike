
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
