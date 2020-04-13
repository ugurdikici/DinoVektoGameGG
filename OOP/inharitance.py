class A:
    def __init__(self):
        self.a = "A"

    def degiskenVer(self):
        return self.a

    def Func(self):
        print("A dan çalıştı")

class B(A):
    def __init__(self):
        super().__init__()
        self.b = "B"

nesne1 = A()
nesne2 = B()
print(nesne2.a)
