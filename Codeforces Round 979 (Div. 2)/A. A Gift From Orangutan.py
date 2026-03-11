import math
def solve(k):
    a = list(map(int,input().split()))
    mx = max(a)
    mn = min(a)
    sum = mx - mn

    sum *= (k-1)

    print(sum)



t = int(input())

for _ in range (t):
    k = int(input())
    solve(k)