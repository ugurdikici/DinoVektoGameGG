from DosyaTool import DosyaTool as DT
class KasaDefteri(DT):
    def __init__(self):
        super().__init__(adres="OrnekProje",dosyaadi="kasadefteri",
        uzanti=".csv",ayrac=";",
        alanlar=["Cari Ünvan:","Vergi Kimlik No:","Borç:","Alacak:"])

    def __del__(self):
        print("Kasa Defteri Kapanıyor")
        super().__del__()
    
    def Listele(self):
        for i in range(len(self.kayitlar)):
            fark = int(self.kayitlar[i].split(";")[3])-int(self.kayitlar[i].split(";")[2])
            print(f"{i+1}-{self.kayitlar[i].replace(self.ayrac,'  ')}-{fark}")


KasDef = KasaDefteri()
KasDef.Menu()