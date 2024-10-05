inp = input()
arr = inp.split()
c = arr[0]
n = int(arr[1])

if c == 'A':
    for i in range(1, n + 1):
        print(i, end=' ')
        i += 1
else:
    i = n
    while i >= 1:
        print(i, end=' ')
        i -= 1