n = int(input())

satisfied = False

for i in range(5):
    if n % 3 == 0:
        satisfied = True

if satisfied == True:
    print('1')
else:
    print('0')