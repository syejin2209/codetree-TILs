n = int(input())
x = 0

while True:
    x += 1
    if n == 2 ** x:
        print(x)
        break
    else:
        continue