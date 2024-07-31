arr = list(map(int, input().split()))
cnt = 0
sum_val = 0

for i in arr:
    sum_val += i
    if i == 0:
        break
    cnt += 1

avg = sum_val/cnt

print(f"{sum_val} {avg:.1f}")