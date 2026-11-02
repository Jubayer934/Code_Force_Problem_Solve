t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    if a < b:
        print(-1)
        continue

    if a == b:
        print(-1)
        continue

    if b == 1:
        print(b)
        continue

    if a/b >= 2:
        print(b)
        continue

    k = a % b

    if k > b:
        print(b)
    else:
        print(k)