n = int(input())
arr = list(map(int, input().split()))
new = []

for i in arr:
    if i % 2 == 0:
        new.append(i)

print(" ".join(map(str, new)))