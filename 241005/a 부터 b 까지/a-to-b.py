inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

while a <= b:
    if a % 2 == 1:
        print(a, end=' ')
        a *= 2
    else:
        print(a, end=' ')
        a += 3