n = int(input())

for i in range(n + 1):
    for j in range(i):
        print(" ", end=' ')
    for j in range((n - i) * 2 - 1):
        print('*', end=' ')
    print()