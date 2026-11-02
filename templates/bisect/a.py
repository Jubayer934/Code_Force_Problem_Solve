from bisect import bisect_left, bisect_right

a = [1, 3, 3, 3, 5, 7]
#    0  1  2  3  4  5

print(bisect_left(a, 3))     # 1  (position before the first 3)
print(bisect_right(a, 3))    # 4  (position after the last 3)

print(bisect_left(a, 4))     # 4
print(bisect_right(a, 4))    # 4   (4 would go between 3 and 5)

print(bisect_left(a, 0))     # 0   (before everything)
print(bisect_left(a, 10))    # 6   (after everything)

a = [1, 3, 3, 3, 5, 7]
count = bisect_right(a, 3) - bisect_left(a, 3)
print(count)                 # 3


# 3. Check whether a value exists
x = 5
i = bisect_left(a, x)
print(i < len(a) and a[i] == x)    # True

x = 4
i = bisect_left(a, x)
print(i < len(a) and a[i] == x)    # False

# 4. Count items smaller or larger than x
a = [1, 3, 3, 3, 5, 7]
x = 3

print(bisect_left(a, x))                # 1  (items < 3)
print(bisect_right(a, x))               # 4  (items <= 3)
print(len(a) - bisect_right(a, x))      # 2  (items > 3)
print(len(a) - bisect_left(a, x))       # 5  (items >= 3)


l, r = 3, 5
print(bisect_right(a, r) - bisect_left(a, l))    # 4  (3, 3, 3, 5)

print()


# Nearest Values
a = [1, 3, 3, 3, 5, 7]
x = 4


# largest value <= x
i = bisect_right(a, x) - 1
print(a[i] if i >= 0 else None)          # 3

# smallest value >= x
i = bisect_left(a, x)
print(a[i] if i < len(a) else None)      # 5

from bisect import insort

a = [1, 3, 5, 7]
insort(a, 4)
print(a)                     # [1, 3, 4, 5, 7]