def result(n):
    arr = [[0] * n for _ in range(2)]

    s = input()
    for _ in range (n):
        arr[0][_] = s[_]

    s = input()
    for _ in range (n):
        arr[1][_] = s[_]

    if arr[1][n-2] == '<':
        return False

    x = 1
    y = n - 2

    while (y>0):
        if (arr[(x+1)%2][y-1] == '>'):
            x = (x+1)%2
            y = y - 1
        elif (y>=2 and (arr[x][y-2]=='>')):
            y = y-2

        else:
            return False
    return True

for _ in range (int(input())):
    R = result(int(input()))
    print("YES" if R else "NO")
