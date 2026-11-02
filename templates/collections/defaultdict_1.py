from collections import defaultdict

d = defaultdict(int)  # missing keys start at 0
d["x"] = 10
d["x"] += 1
d["y"] += 1
print(dict(d))        # {'x': 11, 'y': 1}

for _ in range(len(d)):
    print(list(d.keys())[_])          # x, y
    print(list(d.values())[_])        # 11, 1
    print(list(d.items())[_])         # ('x', 11), ('y', 1)
