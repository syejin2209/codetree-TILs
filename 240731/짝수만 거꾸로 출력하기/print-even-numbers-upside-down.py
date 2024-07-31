n = int(input()) #정수 개수
arr = list(map(int, input().split())) #n개 입력받은 정수 리스트
val = [] #빈 리스트 생성

for i in arr:
    if i % 2 == 0:
        val.append(i)

reversed_val = val[::-1]
for j in reversed_val:
    print(j, end=" ")