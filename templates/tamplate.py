import sys
from collections import defaultdict, deque, Counter
from itertools import accumulate, permutations, combinations
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from bisect import bisect_left, bisect_right, insort_left, insort_right
from math import gcd, isqrt, inf
from functools import reduce

input = sys.stdin.readline

def II():  return int(input())
def MI():  return map(int, input().split())
def LI():  return list(map(int, input().split()))
def LII(): return [list(map(int, input().split())) for _ in range(II())]   

def DD():  return defaultdict(int)
def LD():  return defaultdict(list)
def DQ():  return deque()
def CN():  return Counter()

def LA():  return list(accumulate(LI()))
def LP():  return list(permutations(LI()))
def LC():  return list(combinations(LI(), 2))

def HPH(a, x): return heappush(a, x)
def HPP(a): return heappop(a)
def HPF(a): return heapify(a)
def NSL(a, k): return nsmallest(k, a)
def NLL(a, k): return nlargest(k, a)

def BL(a, x): return bisect_left(a, x)
def BR(a, x): return bisect_right(a, x)
def IL(a, x): return insort_left(a, x)
def IR(a, x): return insort_right(a, x)
def CN(a, x): return bisect_right(a, x) - bisect_left(a, x)

def GCD(a, b): return gcd(a, b)
def GCDN(a): return reduce(gcd, a)
def LCM(a, b): return a // gcd(a, b) * b if a and b else 0        
def LCMN(a): return reduce(LCM, a)
def RT(a): return isqrt(a)
def PS(a): return a >= 0 and RT(a) ** 2 == a     # possible square
def CL(a, b): return -(-a // b)                                  
def FL(a, b): return a // b          
def INF(): return float(inf)      

MOD = 10**9 + 7
# MOD = 998244353
out = []


def solve():
    a = LI()

    a = sorted(a)
    c = CN(a, a[0])

    out.append("YES" if c == 3 or a[0] == a[-1] else "NO")


def main():
    t = II()
    for _ in range(t):
        solve()
    print("\n".join(map(str, out)))


main()