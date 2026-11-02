t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n + 2):
        if i not in a:
            print(i)
            break

        a.remove(i)
        c = 1
        for j in a[:]:
            if c == k:
                break
            if j <= i:
                a.remove(j)
                c += 1

        if c < k:
            print(i)
            break
