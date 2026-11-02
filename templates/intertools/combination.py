from itertools import combinations

print(list(combinations([1, 2, 3, 4], 2)))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

print(list(combinations([1, 2, 3, 4], 3)))
# [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]

print(list(combinations("abc", 2))) 
# [('a', 'b'), ('a', 'c'), ('b', 'c')]

a = [3, 8, 5, 2]
target = 10

for x, y in combinations(a, 2):
    if x + y == target:
        print(x, y)               # 8 2