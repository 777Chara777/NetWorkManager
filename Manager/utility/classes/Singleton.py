class Singleton(type):
    _instanses = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instanses:
            cls._instanses[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instanses[cls]
