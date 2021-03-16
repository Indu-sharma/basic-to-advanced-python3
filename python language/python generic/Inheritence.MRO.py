class A:
    def do(self):
        print("From the class: A")


class B(A):
    def do(self):
        print("From the class: B")


class C(A):
    def do(self):
        print("From the class: C")


class D(C):
    pass


class E(D, B):
    pass


class F(E):
    pass


inst = F()
inst.do()

# F->E->D->C ->B ->A

# F->E->D->C->B->A

print(F.mro())

