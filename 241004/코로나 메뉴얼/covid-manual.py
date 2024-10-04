inp = input()
arr = inp.split()
a_symp = arr[0]
a_temp = int(arr[1])

inp = input()
arr = inp.split()
b_symp = arr[0]
b_temp = int(arr[1])

inp = input()
arr = inp.split()
c_symp = arr[0]
c_temp = int(arr[1])

if a_symp == 'Y':
    if a_temp >= 37:
        if (b_symp == 'Y' and b_temp >= 37) or (c_symp == 'Y' and c_temp >= 37):
            print('E')
        else:
            print('N')
    else:
        if (b_symp == 'Y' and b_temp >= 37) and (c_symp == 'Y' and c_temp >= 37):
            print('E')
        else:
            print('N')
else:
    if (b_symp == 'Y' and b_temp >= 37) and (c_symp == 'Y' and c_temp >= 37):
        print('E')
    else:
        print('N')