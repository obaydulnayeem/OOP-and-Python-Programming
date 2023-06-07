N, M = map(int, input().split())
numbers = list(map(int, input().split()))

frequency = [0] * (M + 1)

for num in numbers:
    frequency[num] += 1

for i in range(1, M + 1):
    print(frequency[i])