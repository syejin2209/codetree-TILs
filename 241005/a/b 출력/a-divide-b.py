inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

print(f"{a//b}.", end="") # 정수. 부분을 먼저 출력

a %= b #a를 b로 나눈 나머지
for _ in range(20):
    a *= 10
    print(a // b, end="")

    a %= b