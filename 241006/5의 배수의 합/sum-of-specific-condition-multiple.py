inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

sum_val = 0

if a <= b:
    for i in range (a, b + 1):
        if i % 5 == 0:
            sum_val += i
else:
    for j in range (b, a + 1):
        if j % 5 == 0:
            sum_val += j

print(sum_val)