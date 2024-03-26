class Error:
    def msg(self):
        print("Error")


class NI(Error): pass


class NG(Error): pass


class NN(Error): pass


class Success:
    def msg(self):
        print("Success")


class L(Success): pass


class N(Success): pass


class I(L, N, NN): pass


class G(I, NI): pass


class E(NG, G): pass


class NE(Error): pass


class B(E, NE): pass


class H(I): pass


class R(I): pass


class W(H, R): pass


class Begin(W, B): pass


begin = Begin()
begin.msg()

b = B()
b.msg()
