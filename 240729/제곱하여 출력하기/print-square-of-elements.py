n = int(input())
arr = list(map(int, input().split()))

new_arr = [item * item for item in arr]

for item in new_arr:
    print(item, end=" ")