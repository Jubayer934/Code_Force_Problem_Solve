def solve():
    n = int(input())
    s = list(map(int, input().split()))[:2*n]
    c1 = s.count(1)
    c2 = s.count(0)
    if c1%2 == 0:
        mn = 0
    else:
        mn = 1
    if c1 == 0:
        mx = 0
    elif c1 < n:
        mx = c1
    elif c1 == 2*n:
        mx = 0
    else:
        mx = c2
    print(f"{mn} {mx}")
t = int(input())
 
for _ in range (t):
    solve()