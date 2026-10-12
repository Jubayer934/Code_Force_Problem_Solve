t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    c = [0] * (n + 2)
    for __ in a:
        c[__] += 1

    a = "No"
    for v in range(n + 2):
        if c[v] < 2 * k:
            if c[v] == 2 * k - 1:
                a = "Yes"
            break

    print(a)