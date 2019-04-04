class A:
    def __init__(self):
        print("INIT A")

    def action(self):
        print("Defined in A")

class B(A):
    def __init__(self):
        super().__init__()

    def action(self):
        print("Defined in B")

class C(A):
    def __init__(self):
        print("INIT C")

    def action(self):
        print("Defined in C")

class D(B, C):

    def __init__(self):
        super().__init__()

    def action(self):
        print("Defined in D")        
        C.action(self)
        B.action(self)

thing = D()
