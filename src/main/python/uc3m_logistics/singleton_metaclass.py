
class SingletonMeta(type):
    _instances = {}
    def __call__(self, *args, **kwargs):

        if self not in self._instances:
            instance = super().__call__(*args,**kwargs)