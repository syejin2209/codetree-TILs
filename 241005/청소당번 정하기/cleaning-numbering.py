n = int(input())

c1 = 0
c2 = 0
c3 = 0

for i in range(1, n + 1):
    if i % 12 == 0:
        c1 += 1
    elif i % 3 == 0:
        c2 += 1
    elif i % 2 == 0:
        c3 += 1
print(c3, c2, c1)