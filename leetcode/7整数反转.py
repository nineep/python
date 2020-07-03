
def f(num):
    ls = []
    if num < 0:
        num = num * -1
        for n in str(num):
            ls.append(n)
        ls.reverse()

        a = 0
        for i, b in enumerate(ls):
            a += int(b) * 10**i
        a = a * -1

    else:
        for n in str(num):
            ls.append(n)
        ls.reverse()

        a = 0
        for i, b in enumerate(ls):
            a += int(b) * 10**i

    return a


r = f(123)
print(r)