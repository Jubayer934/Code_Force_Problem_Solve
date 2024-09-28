def solve(a,b):
    print(b-a)


n = int(input())
while(n):
    n = n-1
    a, b = map(int, input().split())
    solve(a,b)