def result(d, i):
    n = d[i][0][0]
    f = d[i][0][1]
    a = d[i][0][2]
    b = d[i][0][3]

    prev = 0

    s = 0

    for _ in range(n):
        cal = (d[i][1][_] - prev)*a
        prev = d[i][1][_]
        
        t = cal if cal < b else b

        s = s + t

    return str("Yes" if f>s else "No")

        



def user_input(i):
    d = {}
    a = tuple(map(int, input().split()))

    b = tuple(map(int, input().split()))

    c = (a, b)

    d[i] = c

    return (result(d, i))
    


"""
Start Coding
"""
i = int(input())
print("\n".join(user_input(_) for _ in range(i)))    
