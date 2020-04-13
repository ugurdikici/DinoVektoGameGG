class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.__c =3
        
    def __init__(self,adi,yas):
        self.adi = adi
        self.yas = yas
        self.__c =3

        @property
        def c(self,c):
            if c.isnumeric():
                self.__c = c
                print("c yi değiştirdim")
            else:
                print("c yanlış değer")
                
    @c.deleter
    def c(self):
        del self.__c