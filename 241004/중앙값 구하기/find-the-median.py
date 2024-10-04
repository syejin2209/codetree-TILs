inp = input()
arr = inp.split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

if a <= b:
    if b <= c:
        print(b)
    elif c <= a:
        print(a)
    else:
        print(c)
else:
    if a <= c:
        print(a)
    elif b <= c:
        print(c)
    else:
        print(b)