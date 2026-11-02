t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    m = max(a, b, c)
    n = a + b + c

    if m == a:
        r = 'P'*n
        print(r)
    elif m == b:
        r = 'R'*n
        print(r)
    else:
        r = 'S'*n
        print(r)