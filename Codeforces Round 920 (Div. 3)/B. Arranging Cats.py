def result(a, b):

    l = len(a)

    same = 0
    for _ in range(l):
        if a[_] == b[_] and a[_] == 1 and b[_] == 1:
            same = same + 1
    
    max1 = max(a.count(1), b.count(1))
    
    print(max1 - same)


n = {}

i = int(input())
for _ in range(i):
    n[_+1] = {}

    
    a = int(input())
    n[_+1][a] = {}

    b = tuple(map(int, input()))
    c = tuple(map(int, input()))

    x = (b, c)

    n[_+1][a] = x

    result(n[_+1][a][0], n[_+1][a][1])