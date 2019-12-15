class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type']
        self._name = kwargs['name']
        self._sound = kwargs['sound']

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound
