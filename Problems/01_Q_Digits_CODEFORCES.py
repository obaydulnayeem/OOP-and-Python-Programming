# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Q

n = int(input())

for i in range(n): 
    num = input()
    for char in reversed(num):
        print(char, end= " ")
    print()