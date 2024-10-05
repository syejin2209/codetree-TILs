inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

sum_val = 0
ave_val = 0
val = 0

for i in range(a, b + 1):
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i
        val += 1
ave_val = sum_val / val

print(sum_val, f'{ave_val:.1f}')