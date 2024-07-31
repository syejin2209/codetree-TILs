n = int(input()) #학생수

p = 0 # 통과한사람수

for _ in range(n):
    arr = list(map(int, input().split()))

    sum_val = sum(arr)

    avg = sum_val/4

    if avg >= 60:
        print('pass')
        p += 1
    else:
        print('fail')

print(p)