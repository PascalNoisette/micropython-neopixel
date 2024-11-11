
class NeoPixel(object):
    def __init__(self, pin, pixels):
        pass

    def __setitem__(self, key, value):
        setattr(self, str(key), value)

    def __getitem__(self, key):
        return getattr(self, str(key))
    
    def write(self):
        pass