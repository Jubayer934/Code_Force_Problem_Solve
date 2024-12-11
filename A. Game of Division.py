import sys

def solve():
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    results = []
    i = 1
    for _ in range (t):
        a,b = map(int, data[i].split())
        i += 1
        nums = list(map(int,data[i].split()))
        i += 1

        w2 = True
        for __ in range(a):
            w1 = True
            for ___ in range(a):
                if __ != ___:
                    if ( abs(nums[__] - nums[___]) % b == 0):
                        w1 = False
                        break
            if w1:
                results.append("Yes")
                results.append(str(__+1))
                w2 = False
                break
        if w2:
            results.append("No")    
    
    sys.stdout.write("\n".join(results) + "\n")


# জুবায়ের আল মাহমুদ
if __name__ == "__main__":
    solve()