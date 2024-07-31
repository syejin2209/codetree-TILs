arr = list(map(int, input().split()))
new = []

for i in arr:
    if i % 2 == 1:
        a = i + 3
        new.append(a)
    if i % 2 == 0:
        b = i // 2
        new.append(b)
    if i == 0:
        new.pop()

print(*new)