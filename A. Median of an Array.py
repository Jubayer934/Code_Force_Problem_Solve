t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    
    median_index = (n + 1) // 2 - 1
    median = a[median_index]

    print(median)
    print(median_index)
    
    count = a[median_index:].count(median)
    
    print(count)
