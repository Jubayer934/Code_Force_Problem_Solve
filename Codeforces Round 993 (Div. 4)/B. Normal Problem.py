import sys

def solve():
    input = sys.stdin.read
    data = input().splitlines()
    results = []
    t = int(data[0])
    i = 0
    for _ in range(t):
        i += 1
        s = data[i]
        s = s.replace("p",".")
        s = s.replace("q","p")
        s = s.replace(".","q")
        s = s[::-1]

        results.append(s)

    
    sys.stdout.write("\n".join(results) + "\n")


# জুবায়ের আল মাহমুদ
if __name__ == "__main__":
    solve()
