sum_val = 0
ave_val = 0
cnt = 0

for i in range(10):
    n = int(input())
    if n >= 0 and n <= 200:
        sum_val += n
        cnt += 1
ave_val = sum_val / cnt

print(sum_val, f'{ave_val:.1f}')