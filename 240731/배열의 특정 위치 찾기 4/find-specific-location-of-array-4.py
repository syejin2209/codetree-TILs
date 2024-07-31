arr = list(map(int, input().split()))
cnt = 0
sum_val = 0

for i in arr:
    if i % 2 == 0:
        sum_val += i
        cnt += 1
    elif i == 0:
        break

print(f"{cnt-1} {sum_val}")