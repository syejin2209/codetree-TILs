n = int(input())
sum_val = 0
cnt = 0

for i in range(n):
    m = int(input())
    sum_val += m
    cnt += 1
avg = sum_val / cnt

print(f'{sum_val} {avg:.1f}')