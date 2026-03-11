for _ in range (int(input())):
    n = int(input())
    if n%2 == 1:
        print('NO',end='')
    else :
        print('YES')
    if n%2 == 0:
        for i in range (n//2):
            print('BAA',end='')
    print()