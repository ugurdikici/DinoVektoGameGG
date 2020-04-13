"""
class Personel:
    isim = ""
    yas = 0
    def __init__(self, personelIsim,personelYas):
        self.isim = personelIsim
        self.yas = personelYas

    def __repr__(self):
        return "{isim:"+self.isim+",yas:"+str(self.yas)+"}"
    
    def __str__(self):
        return "Personel(isim="+self.isim+", yas="+str(self.yas)+")"

P1 = Personel("Ali",25)
P2 = Personel("Veli",35)
"""
class Araba:
    model = ""
    yıl = 0
    def __init__(self, arabaModel,arabaYıl):
        self.model = arabaModel
        self.yıl = arabaYıl

    def __repr__(self):
        return "{model:"+self.model+",yıl:"+str(self.yıl)+"}"

    def __str__(self):
        return "Araba(isim="+self.model+", yıl="+str(self.yıl)+")"

P1 = Araba("Dacia",2005)
P2 = Araba("Ford",2018)
print(repr(P1))