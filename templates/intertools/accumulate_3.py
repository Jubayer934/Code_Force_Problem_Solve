from itertools import accumulate

a = [5, 2, 7, 1, 3]
pre = [0] + list(accumulate(a))   # [0, 5, 7, 14, 15, 18]

# sum of a[1..3] (elements 2, 7, 1)
l, r = 1, 3
print(pre[r + 1] - pre[l])        # 10