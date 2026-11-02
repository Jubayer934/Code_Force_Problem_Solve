t = int(input())

for _ in range(t):
    s = input()
    if s[0] == s[-1]:
        if len(s) == 3:
            print(2)
            continue

        