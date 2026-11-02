from collections import Counter

a = [1, 2, 2, 3, 3, 3]
c = Counter(a)

print(c)              # Counter({3: 3, 2: 2, 1: 1})
print(c[1])           # 1  (1 appears once)
print(c[99])          # 0  (missing item gives 0, no error)
print(c.most_common(1))  # [(3, 3)]  (most frequent item and its count)