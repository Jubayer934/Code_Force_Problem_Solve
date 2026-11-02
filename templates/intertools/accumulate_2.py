from itertools import accumulate

a = [1, 4, 3, 2]
print(list(accumulate(a)))        # [1, 5, 8, 10]

print(list(accumulate(a, max)))   # [1, 4, 4, 4]  (running maximum)
print(list(accumulate([3, 1, 4, 1, 5], max)))   # [3, 3, 4, 4, 5]
print(list(accumulate(a, lambda x, y: x * y)))  # [1, 4, 12, 24]  (running product)