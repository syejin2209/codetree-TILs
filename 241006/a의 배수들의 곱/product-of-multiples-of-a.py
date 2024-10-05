inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

prod = 1

for i in range(1, 10):
    v = a * i
    if v <= b:
        prod *= v

print(prod)