def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    max_sub_array = max_sum = 0
    
    for i in range(n):
        max_sum += a[i]
        max_sub_array = max(max_sub_array, max_sum)
        max_sum = max(max_sum, 0)

    sum_of_array = sum(a)
    ans = max_sub_array
    
    for i in range (k):
        ans = (ans * 2)
    
    ans -= max_sub_array
    ans += sum_of_array 
    ans = ans % (10**9 + 7)

    print(ans)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solve()
