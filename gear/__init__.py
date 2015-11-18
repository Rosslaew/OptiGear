class Gear(object):
    def __init__(self, slot, **attributes):
        self.slot = slot
        for k,v in attributes.items():
            self.__setattr__(k,v)
