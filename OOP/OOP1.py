"""
class Kedi:
    tur = "Memeli"
    familya = "Felis"

    def __init__(self,adi,yas):
        self.adi = adi
        self.yas = yas
        
    def Miyavla(self):
        print(self.adi,"Miyavladi")

    def Costu(self):
        print(self.adi,"Costu")

    def __del__(self):
        print(self.adi,"RIP")


kedi1 = Kedi("Melek",5)
kedi1.Miyavla()
kedi1.Costu()
del kedi1
"""

class Balik:
    tur = "moli"
    familya = "Balon Moli"

    def Swim(self):
        print(self.adi,"bıcı_bıcı")

    def Costu(self):
        print(self.adi,"Costu")
    
    def __del__(self):
        print(self.adi,"boguldu")

balik1 = Balik("Balik","Erkek")
del balik1
