t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    if s.count('1') == 1:
        print(0)
        continue

    if s.count('1') == 2:
        f = s.find('1')
        l = s.rfind('1')

        lz = s.find('0')

        if l < lz:

            print(l-f if l-f >= 0 else 1)
        else:
            print(lz-f if lz-f >= 0 else 1)


        continue

    f = s.find('1')
    l = s.rfind('1')

    f = f + 1
    l = l + 1

    print(l - f)