def has_1100_pattern(s, start):
    if start < 0 or start + 3 >= len(s):
        return False
    return s[start] == '1' and s[start + 1] == '1' and s[start + 2] == '0' and s[start + 3] == '0'
 
t = int(input())
 
for _ in range(t):
    s = list(input().strip())
    n = len(s)
    
    pattern_positions = set()
    for i in range(n - 3):
        if has_1100_pattern(s, i):
            pattern_positions.add(i)
    
    q = int(input())
    
    for _ in range(q):
        i, v = map(int, input().split())
        i -= 1  
        
        s[i] = str(v)
        
 
        for j in range(i - 3, i + 1):
            if j >= 0 and j + 3 < n:
                if has_1100_pattern(s, j):
                    pattern_positions.add(j)
                else:
                    pattern_positions.discard(j)
        
        if pattern_positions:
            print("YES")
        else:
            print("NO")