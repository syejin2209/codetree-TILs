inp = input()
arr = inp.split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

sum = a + b + c
ave = (a + b + c) // 3

print(sum)
print(ave)
print(sum - ave)