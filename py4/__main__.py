class ComplexNumber:
    rr = 0
    ll = 0

    def __init__(self, rr, ll):
        self.rr = rr
        self.ll = ll

    def __add__(self, other):
        return ComplexNumber(self.rr + other.rr, self.ll + other.ll)

    def __sub__(self, other):
        return ComplexNumber(self.rr - other.rr, self.ll - other.ll)


if __name__ == '__main__':
    a = input()
    a = a.replace('i', '')
    if '+' in a:
        a = a.split('+')
        a = list(map(int, a))
    else:
        a = a.split('-')
        a = list(map(int, a))
        a[1] = -a[1]
    ca = ComplexNumber(a[0], a[1])
    b = input()
    b = b.replace('i', '')
    if '+' in b:
        b = b.split('+')
        b = list(map(int, b))
    else:
        b = b.split('-')
        b = list(map(int, b))
        b[1] = -b[1]
    cb = ComplexNumber(b[0], b[1])
    cc = ca + cb
    print(cc.rr, end='')
    if cc.ll > 0:
        print('+', end='')
    print(cc.ll, end='')
    print('i')
    cd = ca - cb
    print(cd.rr, end='')
    if cd.ll > 0:
        print('+', end='')
    print(cd.ll, end='')
    print('i')
