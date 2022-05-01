nm = input().split()
n, m = int(nm[0]), int(nm[1])
ps = []
for x in input().split():
    ps.append(float(x))

for i in range(m):
    n += int(ps[i] * n / (1 - ps[i]) + 1e-6) - 1

print(n)