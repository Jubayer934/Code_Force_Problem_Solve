for _ in range (int(input())):
    n = int(input())

    a = list(map(int,input().split()))



    result = 'YES'
    k = 0
    for i in range (n):

        if k>a[i]:
            result = 'NO'
            break

        d = a[i]//10
        r = a[i]%10

        if k<=d:
            if d<=r:
                k=r
            else:
                k=a[i]
        else:
            k = a[i]
        

    print(result)




