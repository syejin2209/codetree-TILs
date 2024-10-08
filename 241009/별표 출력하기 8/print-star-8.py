n = int(input())

for i in range(n):
    if i % 2 == 1:
        print((i + 1) * '* ', end=' ')
    else:
        print('* ', end=' ')
    print()