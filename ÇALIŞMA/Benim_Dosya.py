class A:
    def __init__(self):
        self.a = "a"

    def Func(self):
        print("Merhaba A")

class B:
    def __init__(self):
        A.__init__(self)
        self.b ="a"
        self.Func()

    def Func(self):
        print("Merhaba B")

nesne1 = B()