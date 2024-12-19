import sys
def solve():
    input = sys.stdin.read
    data = input().splitlines()
    results = []

    t = int(data[0])
    i = 0
    for _ in range(t):
        i += 1
        n = int(data[i])
        results.append(str(n-1))
        
     
    
    sys.stdout.write("\n".join(results) + "\n")


# জুবায়ের আল মাহমুদ
if __name__ == "__main__":
    solve()