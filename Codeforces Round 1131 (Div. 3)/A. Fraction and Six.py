t = int(input())

for _ in range(t):
    p, q = map(int, input().split())

    p_s = input()
    q_s = input()

    c = 1

    for _ in q_s:
        if _ in p_s:
            p_s = p_s.replace(_, "", 1)
        else:
            c = 0
            break
        
        
    result = "".join(sorted(p_s))

    if c == 0:
        print("No")
        continue
    print("Yes" if result == "isx" else "No")