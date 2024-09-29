def solve(n, k):
    cnt = 0
    if k == 1:
        print(n)
    else:
        while n:
            cnt += n % k
            n //= k
        
        print(cnt)



t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    solve(n, k)
