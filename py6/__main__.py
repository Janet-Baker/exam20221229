from collections import OrderedDict

if __name__ == '__main__':
    n = input()
    n = int(n)
    alist = []
    for i in range(n):
        r = input()
        r = r.lower().split(" ")
        alist.extend(r)
    adic = OrderedDict()
    maxcount = 0
    for s in alist:
        if adic.get(s) == None:
            adic[s] = 1
        else:
            adic[s] = adic.get(s) + 1
        maxcount = max(adic[s], maxcount)
    printkeys = []
    for s in adic.keys():
        if adic.get(s) == maxcount:
            printkeys.append(s)
    print(maxcount)
    for s in printkeys:
        print(s)
