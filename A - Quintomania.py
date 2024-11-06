import math
def solve():
    n = int(input())
    num = list(map(int, input().split()))[:n]
    t = 0
    for _ in range (n-1):
        sum = abs(num[_]-num[_+1])
        if sum != 7 or sum != 5:
            t += 1
    if t > 0:
        print('NO')
    else:
        print("YES")
 
 
t = int(input())
for _ in range (t):
    solve()