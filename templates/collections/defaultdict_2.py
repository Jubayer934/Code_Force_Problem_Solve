from collections import defaultdict

g = defaultdict(list)

edges = [(1, 2), (1, 3), (2, 3)]
for u, v in edges:
    print(u, v)
    g[u].append(v)
    g[v].append(u)
    print(dict(g))
    print()

print(dict(g))        # {1: [2, 3], 2: [1, 3], 3: [1, 2]}
print(g[4])           # []  (missing item gives empty list, no error)   