def result(d, i):
    n = d[i][0][0]
    m = d[i][0][1]
    k = d[i][0][2]

    c = 0

    bL = tuple(d[i][1][_] for _ in range (n) if d[i][1][_]<k)

    cR = tuple(d[i][2][_] for _ in range (m) if d[i][2][_]<k)

    for __ in range (len(bL)):
        for ___ in range (len(cR)):
            sum = bL[__] + cR[___]

            c = c+1 if sum <= k else c + 0



    return str(c)



def user_input(i):

    d = {}

    a = tuple(map(int, input().split()))

    b = tuple(map(int, input().split()))

    c = tuple(map(int, input().split()))

    t = (a, b, c)

    d[i] = t

    return result(d, i)
"""
Start Code
"""

print("\n".join(user_input(_) for _ in range(int(input()))))