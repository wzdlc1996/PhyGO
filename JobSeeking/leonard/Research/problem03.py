q = int(input())
abcList = []
for i in range(q):
    abcList.append([int(x) for x in input().split()])

def fer(a, b, c):
    def f(x):
        return x ** 3 + a * x ** 2 + b * x - c
    def fp(x):
        return 3 * x ** 2 + 2 * a * x + b
    return f, fp    

def newton(f, fp, e=1e-6):
    x0 = 0
    x_n = x0 - f(x0) / fp(x0)
    while abs(x_n - x0) > e:
        x0 = x_n
        x_n = x0 - f(x0) / fp(x0)
    return x_n

for abc in abcList:
    f, fp = fer(*abc)
    print(newton(f=f, fp=fp))