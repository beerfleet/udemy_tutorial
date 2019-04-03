class A:
    def action(self):
        print("Defined in A")

class B(A):
    def action(self):
        print("Defined in B")

class C(A):
    def action(self):
        print("Defined in C")

class D(B, C):    
    def action(self):
        print("Defined in D")        
        C.action(self)
        B.action(self)

thing = D()
thing.action()