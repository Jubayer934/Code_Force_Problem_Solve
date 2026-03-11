def f(a, b, s):
    x, y = 0, 0
    for _ in range(250):
        for dir in s:
            if dir == 'N':
                y += 1
            elif dir == 'S':
                y -= 1
            elif dir == 'E':
                x += 1
            elif dir == 'W':
                x -= 1
            if x == a and y == b:
                return True
    return False

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    s = input()
    result = f(a, b, s)
    print("YES" if result else "NO")
