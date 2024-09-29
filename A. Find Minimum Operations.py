def solve(n, k):
    dq = []
    
    if k == 1:
        print(n)
    else:
        while n:
            dq.append(n % k)
            n //= k
        cnt = sum(dq)
        print(cnt)



t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    solve(n, k)
