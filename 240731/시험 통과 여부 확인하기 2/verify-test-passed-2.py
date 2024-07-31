cnt = int(input())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))
arr_3 = list(map(int, input().split()))

avg_1 = 0
avg_2 = 0
avg_3 = 0

avg_1 = sum(arr_1)/4
avg_2 = sum(arr_2)/4
avg_3 = sum(arr_3)/4

list_val = [avg_1, avg_2, avg_3]
cnt_val = 0

for i in list_val:
    if i >= 60:
        print('pass')
        cnt_val += 1
    else:
        print('fail')

print(cnt_val)