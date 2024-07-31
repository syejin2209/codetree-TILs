arr = list(map(int, input().split()))
cnt = 0

for i in range(1, 9):
    arr.append(2*arr[cnt] + arr[cnt + 1])
    cnt += 1

for elem in arr:
    print(elem, end=" ")