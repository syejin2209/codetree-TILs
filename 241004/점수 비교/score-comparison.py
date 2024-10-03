inp1 = input()
arr1 = inp1.split()
Am = int(arr1[0])
Ae = int(arr1[1])

inp2 = input()
arr2 = inp2.split()
Bm = int(arr2[0])
Be = int(arr2[1])

if Am > Bm and Ae > Be:
    print('1')
else:
    print('0')