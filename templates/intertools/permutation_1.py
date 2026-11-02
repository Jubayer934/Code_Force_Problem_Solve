from itertools import permutations

print(list(permutations([1, 2, 3])))
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

for p in permutations("abc"):
    print("".join(p))
# abc acb bac bca cab cba