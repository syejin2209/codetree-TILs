n = int(input())
arr = list(map(float, input().split()))

print(f"{sum(arr)/n:.1f}")

if sum(arr) >= 4.0 * n:
    print("Pefrect")
elif sum(arr) >= 3.0 * n:
    print("Good")
else:
    print("Poor")