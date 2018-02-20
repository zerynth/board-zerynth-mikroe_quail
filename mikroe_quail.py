from base import *
from devices import *

class MikroeQuail(Board):

    @staticmethod
    def match(dev):
        return dev["vid"]=="0483" and dev["pid"]=="DF12"
    

    def reset(self):
        pass

    def burn(self,bin,outfn=None):
        return False,"Must be put in DFU mode first!"
