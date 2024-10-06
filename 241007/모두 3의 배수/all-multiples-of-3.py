n = int(input())

satisfied = False

for i in range(n):
    if i % 3 == 0:
        satisfied = True

if satisfied == True:
    print('1')
else:
    print('0')