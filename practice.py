n = int(input())

for j in range(n): 
    a, b = map(int, input().split())

    a = int(a)
    b = int(b)

    _a = min(a, b) + 1
    _b = max(a, b)
    sum = 0

    for i in range(_a, _b):
        if i % 2 == 1:
            sum = sum + i

    print(sum)