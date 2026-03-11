for _ in range (int(input())):
    n = int(input())
    x = ["##",".."]

    s = ""
    
    for _ in range (n):
        if _%2 == 0:
            p = 0
        else:
            p = 1
        for i in range (2):  
            k = p         
            for j in range (n):
                print(x[k%2],end="")
                k += 1
            print()
                
