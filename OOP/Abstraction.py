"""
from abc import *

class Hayvan(ABC):
    @abstractmethod
    def ses_cikar(self):
        pass

class Kedi(Hayvan):
    def ses_cikar(self):
        print("Miyav")

nesne1 = Kedi()
"""
from abc import *

class Suclu(ABC):
    @abstractmethod
    def isledigiSuc(self):
        pass

class Kırmızı(ABC):
    def isledigiSuc(self)
    print("Adam Bıcaklama")

nesne1 = Kırmızı()

